from typing import List, Optional, Any, Dict
import re

from electronics_abstract_parts import *
from .JlcPart import JlcPart, JlcTablePart


class JlcCapacitor(TableDeratingCapacitor, JlcTablePart, FootprintBlock):
  PACKAGE_FOOTPRINT_MAP = {
    '0603': 'Capacitor_SMD:C_0603_1608Metric',
    '0805': 'Capacitor_SMD:C_0805_2012Metric',
    '1206': 'Capacitor_SMD:C_1206_3216Metric',
  }
  DERATE_VOLTCO_MAP = {  # in terms of %capacitance / V over 3.6
    'Capacitor_SMD:C_0603_1608Metric': float('inf'),  # not supported, should not generate below 1uF
    'Capacitor_SMD:C_0805_2012Metric': 0.08,
    'Capacitor_SMD:C_1206_3216Metric': 0.04,
  }

  @classmethod
  def _make_table(cls) -> PartsTable:
    CAPACITOR_MATCHES = {
      'nominal_capacitance': re.compile("(^|\s)(\d+(?:\.\d*)?[GMkmunp]?F)($|\s)"),
      'tolerance': re.compile("(^|\s)(([\u00B1]\d+(?:\.\d*)?%)|([\u00B1]\d+(?:\.\d*)?[GMkmunp]?F))($|\s)"),
      'voltage': re.compile("(^|\s)(\d+(?:\.\d*)?V)($|\s)"),
    }

    def parse_row(row: PartsTableRow) -> Optional[Dict[PartsTableColumn, Any]]:
      if row['First Category'] != 'Capacitors':
        return None

      new_cols: Dict[PartsTableColumn, Any] = {}
      try:
        # handle the footprint first since this is the most likely to filter
        footprint = cls.PACKAGE_FOOTPRINT_MAP[row[cls._PACKAGE_HEADER]]

        extracted_values = cls.parse(row[cls.DESCRIPTION_COL], CAPACITOR_MATCHES)

        nominal_capacitance = PartParserUtil.parse_value(extracted_values['nominal_capacitance'][1], 'F')

        # enforce minimum packages, note the cutoffs are exclusive
        if nominal_capacitance > 10e-6 and footprint not in [
          'Capacitor_SMD:C_1206_3216Metric',
        ]:
          return None
        elif nominal_capacitance > 1e-6 and footprint not in [
          'Capacitor_SMD:C_0805_2012Metric',
          'Capacitor_SMD:C_1206_3216Metric',
        ]:
          return None

        new_cols[cls.KICAD_FOOTPRINT] = footprint
        new_cols[cls.CAPACITANCE] = Range.from_tolerance(
          nominal_capacitance,
          PartParserUtil.parse_tolerance(extracted_values['tolerance'][1])
        )
        new_cols[cls.NOMINAL_CAPACITANCE] = nominal_capacitance
        new_cols[cls.VOLTAGE_RATING] = Range.zero_to_upper(
          PartParserUtil.parse_value(extracted_values['voltage'][1], 'V')
        )
        new_cols[cls.VOLTCO] = cls.DERATE_VOLTCO_MAP[footprint]

        new_cols.update(cls._parse_jlcpcb_common(row))

        return new_cols
      except (KeyError, PartParserUtil.ParseError):
        return None

    return cls._jlc_table().map_new_columns(parse_row).sort_by(
      lambda row: [row[cls.BASIC_PART_HEADER], row[cls.KICAD_FOOTPRINT], row[cls.COST]]
    )

  def _make_footprint(self, part: PartsTableRow) -> None:
    super()._make_footprint(part)
    self.assign(self.lcsc_part, part[self.LCSC_PART_HEADER])
    self.assign(self.actual_basic_part, part[self.BASIC_PART_HEADER] == self.BASIC_PART_VALUE)

  def _parallel_sort_criteria(self, row: PartsTableRow) -> List:
    return [row[self.BASIC_PART_HEADER], row[self.PARALLEL_COUNT]]

  def _make_parallel_footprints(self, part: PartsTableRow) -> None:
    assert part[self.PARALLEL_COUNT] < 10, f"too many parallel capacitors ({part[self.PARALLEL_COUNT]})"
    cap_model = JlcDummyCapacitor(set_lcsc_part=part[self.LCSC_PART_HEADER],
                                  set_basic_part=part[self.BASIC_PART_HEADER] == self.BASIC_PART_VALUE,
                                  footprint=part[self.KICAD_FOOTPRINT],
                                  manufacturer=part[self.MANUFACTURER_COL], part_number=part[self.PART_NUMBER_COL],
                                  value=part[self.DESCRIPTION_COL],
                                  capacitance=part[self.NOMINAL_CAPACITANCE],
                                  voltage=self.voltage)
    self.c = ElementDict[JlcDummyCapacitor]()
    for i in range(part[self.PARALLEL_COUNT]):
      self.c[i] = self.Block(cap_model)
      self.connect(self.c[i].pos, self.pos)
      self.connect(self.c[i].neg, self.neg)

    self.assign(self.lcsc_part, part[self.LCSC_PART_HEADER])
    self.assign(self.actual_basic_part, part[self.BASIC_PART_HEADER] == self.BASIC_PART_VALUE)


class JlcDummyCapacitor(DummyCapacitorFootprint, JlcPart):
  """Dummy capacitor that additionally has JLC part fields
  """
  @init_in_parent
  def __init__(self, set_lcsc_part: StringLike = "", set_basic_part: BoolLike = False,
               footprint: StringLike = "", manufacturer: StringLike = "",
               part_number: StringLike = "", value: StringLike = "", *args, **kwargs) -> None:
    super().__init__(footprint, manufacturer, part_number, value, *args, **kwargs)

    self.assign(self.lcsc_part, set_lcsc_part)
    self.assign(self.actual_basic_part, set_basic_part)
