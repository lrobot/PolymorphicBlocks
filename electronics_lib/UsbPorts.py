from electronics_abstract_parts import *
from electronics_lib.JlcPart import JlcPart


@abstract_block
class UsbConnector(Connector):
  """USB connector of any generation / type."""
  USB2_VOLTAGE_RANGE = (4.75, 5.25)*Volt
  USB2_CURRENT_LIMITS = (0, 0.5)*Amp


class UsbAReceptacle(UsbConnector, FootprintBlock):
  def __init__(self) -> None:
    super().__init__()
    self.pwr = self.Port(VoltageSink(
      voltage_limits=self.USB2_VOLTAGE_RANGE,
      current_draw=self.USB2_CURRENT_LIMITS
    ), [Power])
    self.gnd = self.Port(Ground(), [Common])

    self.usb = self.Port(UsbDevicePort(), optional=True)
    self.shield = self.Port(Passive(), optional=True)

  def contents(self):
    super().contents()
    self.footprint(
      'J', 'Connector_USB:USB_A_Molex_105057_Vertical',
      {
        '1': self.pwr,
        '4': self.gnd,

        '2': self.usb.dm,
        '3': self.usb.dp,

        '5': self.shield,
      },
      mfr='Molex', part='105057',
      datasheet='https://www.molex.com/pdm_docs/sd/1050570001_sd.pdf'
    )


class UsbCReceptacle(UsbConnector, FootprintBlock, JlcPart):
  @init_in_parent
  def __init__(self, voltage_out: RangeExpr = UsbConnector.USB2_VOLTAGE_RANGE,  # allow custom PD voltage and current
               current_limits: RangeExpr = UsbConnector.USB2_CURRENT_LIMITS,
               cc_pullup_capable: BoolLike = Default(False)) -> None:
    super().__init__()
    self.pwr = self.Port(VoltageSource(voltage_out=voltage_out, current_limits=current_limits), optional=True)
    self.gnd = self.Port(GroundSource())

    self.usb = self.Port(UsbHostPort(), optional=True)
    self.shield = self.Port(Passive(), optional=True)

    self.cc = self.Port(UsbCcPort(pullup_capable=cc_pullup_capable), optional=True)

  def contents(self):
    super().contents()

    self.assign(self.lcsc_part, 'C165948')  # note, many other pin-compatible parts also available
    self.assign(self.actual_basic_part, False)
    self.footprint(
      'J', 'Connector_USB:USB_C_Receptacle_XKB_U262-16XN-4BVC11',
      {
        'A1': self.gnd,
        'B12': self.gnd,
        'A4': self.pwr,
        'B9': self.pwr,

        'A5': self.cc.cc1,
        'A6': self.usb.dp,
        'A7': self.usb.dm,
        # 'A8': sbu1,

        # 'B8': sbu2
        'B7': self.usb.dm,
        'B6': self.usb.dp,
        'B5': self.cc.cc2,

        'B4': self.pwr,
        'A9': self.pwr,
        'B1': self.gnd,
        'A12': self.gnd,

        'S1': self.shield,
      },
      mfr='Sparkfun', part='COM-15111',
      datasheet='https://cdn.sparkfun.com/assets/8/6/b/4/5/A40-00119-A52-12.pdf'
    )


@abstract_block
class UsbDeviceConnector(UsbConnector):
  """Abstract base class for a USB 2.0 device-side port connector"""
  def __init__(self) -> None:
    super().__init__()
    self.pwr = self.Port(VoltageSource.empty(), optional=True)
    self.gnd = self.Port(GroundSource.empty())

    self.usb = self.Port(UsbHostPort.empty(), optional=True)


class UsbMicroBReceptacle(UsbDeviceConnector, FootprintBlock):
  def __init__(self) -> None:
    super().__init__()

  def contents(self):
    super().contents()
    self.pwr.init_from(VoltageSource(
      voltage_out=self.USB2_VOLTAGE_RANGE,
      current_limits=self.USB2_CURRENT_LIMITS
    ))
    self.gnd.init_from(GroundSource())
    self.usb.init_from(UsbHostPort())

    self.footprint(
      'J', 'Connector_USB:USB_Micro-B_Molex-105017-0001',
      {
        '1': self.pwr,
        '5': self.gnd,

        '2': self.usb.dm,
        '3': self.usb.dp,

        # '4': TODO: ID pin

        '6': self.gnd,  # actually shield
      },
      mfr='Molex', part='105017-0001',
      datasheet='https://www.molex.com/pdm_docs/sd/1050170001_sd.pdf'
    )


class UsbDeviceCReceptacle(UsbDeviceConnector):
  """Implementation of a USB device using a Type-C receptacle as a upstream-facing port.
  Includes pull-down resistors on the CC pins so a Type-C downstream-facing port can supply the default 5v power.
  High speed pins are left open."""
  def __init__(self) -> None:
    super().__init__()

  def contents(self) -> None:
    # TODO for a UFP we expect a pull-up on the CC lines on the DFP side
    self.port = self.Block(UsbCReceptacle(cc_pullup_capable=True))
    self.connect(self.pwr, self.port.pwr)
    self.connect(self.usb, self.port.usb)

    (self.cc_pull, ), _ = self.chain(self.port.cc, self.Block(UsbCcPulldownResistor()))
    self.connect(self.gnd, self.port.gnd, self.port.shield.as_ground(), self.cc_pull.gnd)


class UsbCcPulldownResistor(Block):
  """Pull-down resistors on the CC lines for a device to request power from a type-C UFP port,
  without needing a USB PD IC."""
  def __init__(self) -> None:
    super().__init__()
    self.cc = self.Port(UsbCcPort.empty(), [Input])
    self.gnd = self.Port(Ground.empty(), [Common])

  def contents(self) -> None:
    super().contents()
    pdr_model = PulldownResistor(resistance=5.1*kOhm(tol=0.01))
    self.cc1 = self.Block(pdr_model).connected(self.gnd, self.cc.cc1)
    self.cc2 = self.Block(pdr_model).connected(self.gnd, self.cc.cc2)


@abstract_block
class UsbEsdDiode(TvsDiode):
  def __init__(self) -> None:
    super().__init__()
    self.gnd = self.Port(Ground(), [Common])
    self.usb = self.Port(UsbPassivePort(), [InOut])


class Tpd2e009(UsbEsdDiode, FootprintBlock):
  def contents(self):
    # Note, also compatible: https://www.diodes.com/assets/Datasheets/DT1452-02SO.pdf
    # PESD5V0X1BT,215 (different architecture, but USB listed as application)
    super().contents()
    self.footprint(
      'U', 'Package_TO_SOT_SMD:SOT-23',
      {
        '1': self.usb.dm,
        '2': self.usb.dp,
        '3': self.gnd,
      },
      mfr='Texas Instruments', part='TPD2E009',
      datasheet='https://www.ti.com/lit/ds/symlink/tpd2e009.pdf'
    )


class Esda5v3l(UsbEsdDiode, FootprintBlock, JlcPart):
  def contents(self):
    super().contents()
    self.assign(self.lcsc_part, 'C87911')
    self.assign(self.actual_basic_part, False)
    self.footprint(
      'U', 'Package_TO_SOT_SMD:SOT-23',
      {
        '1': self.usb.dm,
        '2': self.usb.dp,
        '3': self.gnd,
      },
      mfr='STMicroelectronics', part='ESDA5V3L',
      datasheet='https://www.st.com/content/ccc/resource/technical/document/datasheet/eb/9f/a7/ac/7b/b6/46/7f/CD00002057.pdf/files/CD00002057.pdf/jcr:content/translations/en.CD00002057.pdf'
    )
