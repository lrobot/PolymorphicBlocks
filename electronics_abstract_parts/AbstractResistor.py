import re
from typing import Optional, cast, Dict

from electronics_model import *
from .PartsTable import PartsTableColumn, PartsTableRow
from .PartsTablePart import PartsTableFootprint
from .Categories import *
from .StandardPinningFootprint import StandardPinningFootprint


@abstract_block
class Resistor(PassiveComponent, KiCadInstantiableBlock):
  RESISTOR_REGEX = re.compile("^" + f"([\d.]+\s*[{PartParserUtil.SI_PREFIXES}]?)[RΩ]?" +
                              "\s*" + "((?:\+-|\+/-|±)?\s*[\d.]+\s*%?)?" + "$")
  RESISTOR_DEFAULT_TOL = 0.05  # TODO this should be unified elsewhere

  def symbol_pinning(self, symbol_name: str) -> Dict[str, Port]:
    assert symbol_name == 'Device:R'
    return {'1': self.a, '2': self.b}

  @classmethod
  def parse_resistor(cls, value: str):
    match = cls.RESISTOR_REGEX.match(value)
    assert match is not None, f"could not parse resistor from value '{value}'"
    center = PartParserUtil.parse_value(match.group(1), '')
    if match.group(2) is not None:
      tolerance = PartParserUtil.parse_tolerance(match.group(2))
    else:
      tolerance = (-cls.RESISTOR_DEFAULT_TOL, cls.RESISTOR_DEFAULT_TOL)
    return Range.from_tolerance(center, tolerance)

  @classmethod
  def block_from_symbol(cls, symbol_name: str, properties: Dict[str, str]) -> 'Resistor':
    return Resistor(resistance=cls.parse_resistor(properties['Value']))

  @init_in_parent
  def __init__(self, resistance: RangeLike, power: RangeLike = Default(RangeExpr.ZERO)) -> None:
    super().__init__()

    self.a = self.Port(Passive.empty())
    self.b = self.Port(Passive.empty())

    self.resistance = self.ArgParameter(resistance)
    self.power = self.ArgParameter(power)  # operating power range
    self.actual_resistance = self.Parameter(RangeExpr())
    self.actual_power_rating = self.Parameter(RangeExpr())

    self.description = DescriptionString(
      "<b>resistance:</b> ", DescriptionString.FormatUnits(self.actual_resistance, "Ω"),
      " <b>of spec</b> ", DescriptionString.FormatUnits(self.resistance, "Ω"), "\n",
      "<b>power:</b> ", DescriptionString.FormatUnits(self.actual_power_rating, "W"),
      " <b>of operating:</b> ", DescriptionString.FormatUnits(self.power, "W")
    )


@abstract_block
class ResistorStandardPinning(Resistor, StandardPinningFootprint[Resistor]):
  FOOTPRINT_PINNING_MAP = {
    (
      'Resistor_SMD:R_0201_0603Metric',
      'Resistor_SMD:R_0402_1005Metric',
      'Resistor_SMD:R_0603_1608Metric',
      'Resistor_SMD:R_0805_2012Metric',
      'Resistor_SMD:R_1206_3216Metric',
      'Resistor_SMD:R_1210_3225Metric',
      'Resistor_SMD:R_2010_5025Metric',
      'Resistor_SMD:R_2512_6332Metric',

      'Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal',
      'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal',
      'Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P12.70mm_Horizontal',
      'Resistor_THT:R_Axial_DIN0411_L9.9mm_D3.6mm_P12.70mm_Horizontal',
      'Resistor_THT:R_Axial_DIN0414_L11.9mm_D4.5mm_P15.24mm_Horizontal',

      'Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P1.90mm_Vertical',
      'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P2.54mm_Vertical',
      'Resistor_THT:R_Axial_DIN0309_L9.0mm_D3.2mm_P2.54mm_Vertical',
      'Resistor_THT:R_Axial_DIN0411_L9.9mm_D3.6mm_P5.08mm_Vertical',
      'Resistor_THT:R_Axial_DIN0414_L11.9mm_D4.5mm_P5.08mm_Vertical',
    ): lambda block: {
      '1': block.a,
      '2': block.b,
    },
  }


@abstract_block
class TableResistor(ResistorStandardPinning, PartsTableFootprint, GeneratorBlock):
  RESISTANCE = PartsTableColumn(Range)
  POWER_RATING = PartsTableColumn(Range)

  @init_in_parent
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.generator(self.select_part, self.resistance, self.power, self.part, self.footprint_spec)

  def select_part(self, resistance: Range, power_dissipation: Range, part_spec: str, footprint_spec: str) -> None:
    parts = self._get_table().filter(lambda row: (
        (not part_spec or part_spec == row[self.PART_NUMBER_COL]) and
        (not footprint_spec or footprint_spec == row[self.KICAD_FOOTPRINT]) and
        row[self.RESISTANCE].fuzzy_in(resistance) and
        power_dissipation.fuzzy_in(row[self.POWER_RATING])
    ))
    part = parts.first(f"no resistors in {resistance} Ohm, {power_dissipation} W")

    self.assign(self.actual_part, part[self.PART_NUMBER_COL])
    self.assign(self.matching_parts, parts.map(lambda row: row[self.PART_NUMBER_COL]))
    self.assign(self.actual_resistance, part[self.RESISTANCE])
    self.assign(self.actual_power_rating, part[self.POWER_RATING])

    self._make_footprint(part)

  def _make_footprint(self, part: PartsTableRow) -> None:
    self.footprint(
      'R', part[self.KICAD_FOOTPRINT],
      self._make_pinning(part[self.KICAD_FOOTPRINT]),
      mfr=part[self.MANUFACTURER_COL], part=part[self.PART_NUMBER_COL],
      value=part[self.DESCRIPTION_COL],
      datasheet=part[self.DATASHEET_COL]
    )


class PullupResistor(DiscreteApplication):
  """Pull-up resistor with an VoltageSink for automatic implicit connect to a Power line."""
  @init_in_parent
  def __init__(self, resistance: RangeLike) -> None:
    super().__init__()

    self.res = self.Block(Resistor(resistance, 0*Watt(tol=0)))  # TODO automatically calculate power

    self.pwr = self.Export(self.res.a.adapt_to(VoltageSink()), [Power])
    self.io = self.Export(self.res.b.adapt_to(DigitalSingleSource.high_from_supply(self.pwr)), [InOut])

  def connected(self, pwr: Optional[Port[VoltageLink]] = None, io: Optional[Port[DigitalLink]] = None) -> \
      'PullupResistor':
    """Convenience function to connect both ports, returning this object so it can still be given a name."""
    if pwr is not None:
      cast(Block, builder.get_enclosing_block()).connect(pwr, self.pwr)
    if io is not None:
      cast(Block, builder.get_enclosing_block()).connect(io, self.io)
    return self


class PulldownResistor(DiscreteApplication):
  """Pull-down resistor with an VoltageSink for automatic implicit connect to a Ground line."""
  @init_in_parent
  def __init__(self, resistance: RangeLike) -> None:
    super().__init__()

    self.res = self.Block(Resistor(resistance, 0*Watt(tol=0)))  # TODO automatically calculate power

    self.gnd = self.Export(self.res.a.adapt_to(Ground()), [Common])
    self.io = self.Export(self.res.b.adapt_to(DigitalSingleSource.low_from_supply(self.gnd)), [InOut])

  def connected(self, gnd: Optional[Port[VoltageLink]] = None, io: Optional[Port[DigitalLink]] = None) -> \
      'PulldownResistor':
    """Convenience function to connect both ports, returning this object so it can still be given a name."""
    if gnd is not None:
      cast(Block, builder.get_enclosing_block()).connect(gnd, self.gnd)
    if io is not None:
      cast(Block, builder.get_enclosing_block()).connect(io, self.io)
    return self


class SeriesPowerResistor(DiscreteApplication):
  """Series resistor for power applications"""
  @init_in_parent
  def __init__(self, resistance: RangeLike) -> None:
    super().__init__()

    self.resistance = self.ArgParameter(resistance)

    self.pwr_out = self.Port(VoltageSource.empty(), [Output])  # forward declaration
    self.pwr_in = self.Port(VoltageSink.empty(), [Power, Input])  # forward declaration
    current_draw = self.pwr_out.link().current_drawn

    self.res = self.Block(Resistor(
      resistance=self.resistance,
      power=(current_draw.lower() * current_draw.lower() * self.resistance.lower(),
             current_draw.upper() * current_draw.upper() * self.resistance.upper())
    ))

    self.connect(self.pwr_in, self.res.a.adapt_to(VoltageSink(
      voltage_limits=(-float('inf'), float('inf')),
      current_draw=self.pwr_out.link().current_drawn
    )))
    self.connect(self.pwr_out, self.res.b.adapt_to(VoltageSource(
      voltage_out=self.pwr_in.link().voltage,  # ignore voltage drop
      current_limits=Range.all()
    )))

  def connected(self, pwr_in: Optional[Port[VoltageLink]] = None, pwr_out: Optional[Port[VoltageLink]] = None) -> \
      'SeriesPowerResistor':
    """Convenience function to connect both ports, returning this object so it can still be given a name."""
    if pwr_in is not None:
      cast(Block, builder.get_enclosing_block()).connect(pwr_in, self.pwr_in)
    if pwr_out is not None:
      cast(Block, builder.get_enclosing_block()).connect(pwr_out, self.pwr_out)
    return self


from electronics_model.VoltagePorts import VoltageSinkAdapterAnalogSource  # TODO dehack with better adapters
class CurrentSenseResistor(DiscreteApplication, GeneratorBlock):
  """Current sense resistor with a power passthrough resistor and positive and negative sense temrinals."""
  @init_in_parent
  def __init__(self, resistance: RangeLike, sense_in_reqd: BoolLike = True) -> None:
    super().__init__()

    self.res = self.Block(SeriesPowerResistor(resistance))
    self.pwr_in = self.Export(self.res.pwr_in, [Input])
    self.pwr_out = self.Export(self.res.pwr_out, [Output])

    self.sense_in = self.Port(AnalogSource.empty(), optional=True)
    self.sense_out = self.Port(AnalogSource.empty())

    # in some cases, the input rail may be the sense reference and this connection is optional
    # but this must be an explicit opt-in
    sense_in_reqd_param = self.ArgParameter(sense_in_reqd)
    self.require(sense_in_reqd_param.implies(self.sense_in.is_connected()))
    self.generator(self.generate, self.sense_in.is_connected())

  def generate(self, sense_in_connected: bool):
    super().contents()

    # TODO dehack with better adapters that also handle bridging
    if sense_in_connected:
      self.pwr_adapter = self.Block(VoltageSinkAdapterAnalogSource())
      self.connect(self.pwr_in, self.pwr_adapter.src)
      self.connect(self.pwr_adapter.dst, self.sense_in)
    self.connect(self.res.pwr_out.as_analog_source(), self.sense_out)

  def connected(self, pwr_in: Optional[Port[VoltageLink]] = None, pwr_out: Optional[Port[VoltageLink]] = None) -> \
      'CurrentSenseResistor':
    """Convenience function to connect both ports, returning this object so it can still be given a name."""
    if pwr_in is not None:
      cast(Block, builder.get_enclosing_block()).connect(pwr_in, self.pwr_in)
    if pwr_out is not None:
      cast(Block, builder.get_enclosing_block()).connect(pwr_out, self.pwr_out)
    return self
