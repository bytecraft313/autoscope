import obd

PARAMETERS = {
    "rpm": {"name": "RPM", "unit": "rpm", "command": obd.commands.RPM},
    "speed": {"name": "Speed", "unit": "km/h", "command": obd.commands.SPEED},
    "coolant_temp": {"name": "Coolant Temp", "unit": "°C", "command": obd.commands.COOLANT_TEMP},
    "throttle": {"name": "Throttle", "unit": "%", "command": obd.commands.THROTTLE_POS},
    "engine_load": {"name": "Engine Load", "unit": "%", "command": obd.commands.ENGINE_LOAD},
    "intake_temp": {"name": "Intake Temp", "unit": "°C", "command": obd.commands.INTAKE_TEMP},
}