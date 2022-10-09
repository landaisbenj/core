"""Constants for the Switcher integration tests."""

from aioswitcher.device import (
    DeviceState,
    DeviceType,
    SwitcherPowerPlug,
    SwitcherThermostat,
    SwitcherWaterHeater,
    ThermostatFanLevel,
    ThermostatMode,
    ThermostatSwing,
)

from homeassistant.components.switcher_kis import (
    CONF_DEVICE_ID,
    CONF_DEVICE_PASSWORD,
    CONF_PHONE_ID,
    DOMAIN,
)

DUMMY_AUTO_OFF_SET = "01:30:00"
DUMMY_AUTO_SHUT_DOWN = "02:00:00"
DUMMY_DEVICE_ID1 = "a123bc"
DUMMY_DEVICE_ID2 = "cafe12"
DUMMY_DEVICE_ID3 = "bada77"
DUMMY_DEVICE_NAME1 = "Plug 23BC"
DUMMY_DEVICE_NAME2 = "Heater FE12"
DUMMY_DEVICE_NAME3 = "Breeze AB39"
DUMMY_DEVICE_PASSWORD = "12345678"
DUMMY_ELECTRIC_CURRENT1 = 0.5
DUMMY_ELECTRIC_CURRENT2 = 12.8
DUMMY_IP_ADDRESS1 = "192.168.100.157"
DUMMY_IP_ADDRESS2 = "192.168.100.158"
DUMMY_IP_ADDRESS3 = "192.168.100.159"
DUMMY_MAC_ADDRESS1 = "A1:B2:C3:45:67:D8"
DUMMY_MAC_ADDRESS2 = "A1:B2:C3:45:67:D9"
DUMMY_MAC_ADDRESS3 = "A1:B2:C3:45:67:DA"
DUMMY_PHONE_ID = "1234"
DUMMY_POWER_CONSUMPTION1 = 100
DUMMY_POWER_CONSUMPTION2 = 2780
DUMMY_REMAINING_TIME = "01:29:32"
DUMMY_TIMER_MINUTES_SET = "90"
DUMMY_THERMOSTAT_MODE = ThermostatMode.COOL
DUMMY_TEMPERATURE = 24.1
DUMMY_TARGET_TEMPERATURE = 23
DUMMY_FAN_LEVEL = ThermostatFanLevel.LOW
DUMMY_SWING = ThermostatSwing.OFF
DUMMY_REMOTE_ID = "ELEC7001"

YAML_CONFIG = {
    DOMAIN: {
        CONF_PHONE_ID: DUMMY_PHONE_ID,
        CONF_DEVICE_ID: DUMMY_DEVICE_ID1,
        CONF_DEVICE_PASSWORD: DUMMY_DEVICE_PASSWORD,
    }
}

DUMMY_PLUG_DEVICE = SwitcherPowerPlug(
    DeviceType.POWER_PLUG,
    DeviceState.ON,
    DUMMY_DEVICE_ID1,
    DUMMY_IP_ADDRESS1,
    DUMMY_MAC_ADDRESS1,
    DUMMY_DEVICE_NAME1,
    DUMMY_POWER_CONSUMPTION1,
    DUMMY_ELECTRIC_CURRENT1,
)

DUMMY_WATER_HEATER_DEVICE = SwitcherWaterHeater(
    DeviceType.V4,
    DeviceState.ON,
    DUMMY_DEVICE_ID2,
    DUMMY_IP_ADDRESS2,
    DUMMY_MAC_ADDRESS2,
    DUMMY_DEVICE_NAME2,
    DUMMY_POWER_CONSUMPTION2,
    DUMMY_ELECTRIC_CURRENT2,
    DUMMY_REMAINING_TIME,
    DUMMY_AUTO_SHUT_DOWN,
)

DUMMY_THERMOSTAT_DEVICE = SwitcherThermostat(
    DeviceType.BREEZE,
    DeviceState.ON,
    DUMMY_DEVICE_ID3,
    DUMMY_IP_ADDRESS3,
    DUMMY_MAC_ADDRESS3,
    DUMMY_DEVICE_NAME3,
    DUMMY_THERMOSTAT_MODE,
    DUMMY_TEMPERATURE,
    DUMMY_TARGET_TEMPERATURE,
    DUMMY_FAN_LEVEL,
    DUMMY_SWING,
    DUMMY_REMOTE_ID,
)

DUMMY_SWITCHER_DEVICES = [DUMMY_PLUG_DEVICE, DUMMY_WATER_HEATER_DEVICE]
