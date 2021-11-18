from electronics_abstract_parts.Categories import DummyDevice
from electronics_abstract_parts import *
from .PartsTable import *
import math

class TableDeratingCapacitor(Capacitor):
  _TABLE: type

  DERATE_VOLTCO = {  # in terms of %capacitance / V over 3.6
    #  'Capacitor_SMD:C_0603_1608Metric'  # not supported, should not generate below 1uF
    'Capacitor_SMD:C_0805_2012Metric': 0.08,
    'Capacitor_SMD:C_1206_3216Metric': 0.04,
  }
  DERATE_MIN_VOLTAGE = 3.6  # voltage at which derating is zero
  DERATE_MIN_CAPACITANCE = 1.0e-6
  DERATED_CAPACITANCE = PartsTableColumn(Range)

  PARALLEL_COUNT = PartsTableColumn(int)
  PARALLEL_CAPACITANCE = PartsTableColumn(Range)
  PARALLEL_DERATED_CAPACITANCE = PartsTableColumn(Range)
  PARALLEL_COST = PartsTableColumn(float)

  @init_in_parent
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.part_spec = self.Parameter(StringExpr(""))
    self.footprint_spec = self.Parameter(StringExpr(""))

    # Default that can be overridden
    self.single_nominal_capacitance = self.Parameter(RangeExpr((0, 22)*uFarad))  # maximum capacitance in a single part

    self.generator(self.select_capacitor, self.capacitance, self.voltage, self.single_nominal_capacitance,
                   self.part_spec, self.footprint_spec)

    # Output values
    self.selected_capacitance = self.Parameter(RangeExpr())
    self.selected_derated_capacitance = self.Parameter(RangeExpr())
    self.selected_voltage_rating = self.Parameter(RangeExpr())

  def select_capacitor(self, cls, capacitance: Range, voltage: Range,
                         single_nominal_capacitance: Range,
                         part_spec: str, footprint_spec: str) -> None:
    # Pre-filter out by the static parameters
    # Note that we can't filter out capacitance before derating
    prefiltered_parts = cls._TABLE.table().filter(lambda row: (
            (not part_spec or part_spec == row[cls._TABLE.PART_NUMBER]) and
            (not footprint_spec or footprint_spec == row[cls._TABLE.FOOTPRINT]) and
            voltage.fuzzy_in(row[cls._TABLE.VOLTAGE_RATING]) and
            Range.exact(row[cls._TABLE.NOMINAL_CAPACITANCE]).fuzzy_in(single_nominal_capacitance)
    ))

    def derate_row(row: PartsTableRow) -> Optional[Dict[PartsTableColumn, Any]]:
      if voltage.upper < self.DERATE_MIN_VOLTAGE:  # zero derating at low voltages
        derated = row[cls._TABLE.CAPACITANCE]
      elif row[cls._TABLE.NOMINAL_CAPACITANCE] <= self.DERATE_MIN_CAPACITANCE:  # don't derate below 1uF
        derated = row[cls._TABLE.CAPACITANCE]
      elif row[cls._TABLE.FOOTPRINT] not in self.DERATE_VOLTCO:  # should be rare, small capacitors should hit the above
        return None
      else:  # actually derate
        voltco = self.DERATE_VOLTCO[row[cls._TABLE.FOOTPRINT]]
        factor = 1 - voltco * (voltage.upper - 3.6)
        derated = row[cls._TABLE.CAPACITANCE] * Range(factor, 1)

      return {self.DERATED_CAPACITANCE: derated}

    # If the min required capacitance is above the highest post-derating minimum capacitance, use the parts table.
    # An empty parts table handles the case where it's below the minimum or does not match within a series.
    derated_parts = prefiltered_parts.map_new_columns(
      derate_row
    )
    derated_max_min_capacitance = max(derated_parts.map(lambda row: row[self.DERATED_CAPACITANCE].lower))

    if capacitance.lower <= derated_max_min_capacitance:
      part = derated_parts.filter(lambda row: (
              row[self.DERATED_CAPACITANCE] in capacitance
      )).first(f"no single capacitor in {capacitance} F, {voltage} V")

      self.assign(self.selected_voltage_rating, part[cls._TABLE.VOLTAGE_RATING])
      self.assign(self.selected_capacitance, part[cls._TABLE.CAPACITANCE])
      self.assign(self.selected_derated_capacitance, part[self.DERATED_CAPACITANCE])

      self.footprint(
        'C', part[cls._TABLE.FOOTPRINT],
        {
          '1': self.pos,
          '2': self.neg,
        },
        mfr=part[cls._TABLE.MANUFACTURER], part=part[cls._TABLE.PART_NUMBER],
        value=f"{part['Capacitance']}, {part['Voltage - Rated']}",
        datasheet=part[cls._TABLE.DATASHEETS]
      )
    else:  # Otherwise, generate multiple capacitors
      # Additionally annotate the table by total cost and count, sort by lower count then total cost
      def parallel_row(row: PartsTableRow) -> Optional[Dict[PartsTableColumn, Any]]:
        new_cols: Dict[PartsTableColumn, Any] = {}
        count = math.ceil(capacitance.lower / row[self.DERATED_CAPACITANCE].lower)
        derated_parallel_capacitance = row[self.DERATED_CAPACITANCE] * count
        if not derated_parallel_capacitance.fuzzy_in(capacitance):  # not satisfying spec
          return None

        new_cols[self.PARALLEL_COUNT] = count
        new_cols[self.PARALLEL_DERATED_CAPACITANCE] = derated_parallel_capacitance
        new_cols[self.PARALLEL_CAPACITANCE] = row[cls._TABLE.CAPACITANCE] * count
        new_cols[self.PARALLEL_COST] = row[cls._TABLE.COST] * count

        return new_cols

      part = derated_parts.map_new_columns(
        parallel_row
      ).sort_by(lambda row:
                (row[self.PARALLEL_COUNT], row[self.PARALLEL_COST])
                ).first(f"no parallel capacitor in {capacitance} F, {voltage} V")

      self.assign(self.selected_voltage_rating, part[cls._TABLE.VOLTAGE_RATING])
      self.assign(self.selected_capacitance, part[self.PARALLEL_CAPACITANCE])
      self.assign(self.selected_derated_capacitance, part[self.PARALLEL_DERATED_CAPACITANCE])

      cap_model = DummyCapacitor(capacitance=part[cls._TABLE.NOMINAL_CAPACITANCE],
                                 voltage=self.voltage,
                                 footprint=part[cls._TABLE.FOOTPRINT],
                                 manufacturer=part[cls._TABLE.MANUFACTURER], part_number=part[cls._TABLE.PART_NUMBER],
                                 value=f"{part['Capacitance']}, {part['Voltage - Rated']}")
      self.c = ElementDict[DummyCapacitor]()
      for i in range(part[self.PARALLEL_COUNT]):
        self.c[i] = self.Block(cap_model)
        self.connect(self.c[i].pos, self.pos)
        self.connect(self.c[i].neg, self.neg)


class DummyCapacitor(DummyDevice, Capacitor, FootprintBlock):
  """
  Dummy capacitor that takes in all its parameters (footprint, value, etc) and does not do any computation.
  Used as the leaf block for generating parallel capacitors.
  """

  @init_in_parent
  def __init__(self, footprint: StringLike = "",
               manufacturer: StringLike = "", part_number: StringLike = "", value: StringLike = "",
               *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.footprint(
      'C', footprint,
      {
        '1': self.pos,
        '2': self.neg,
      },
      mfr=manufacturer, part=part_number,
      value=value
    )
