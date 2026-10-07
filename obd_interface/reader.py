# obd/reader.py

import random

import obd


class OBDReader:
    """Reads vehicle data from an OBD-II connection."""

    def __init__(self, connection):
        self.connection = connection

    def read(self, command):
        """Read a single OBD-II parameter."""

        if self.connection.simulation:
            return self._simulate(command)

        response = self.connection.connection.query(command)

        if response.is_null():
            return None

        return response.value

    def _simulate(self, command):
        """Generate simulated vehicle data for development."""

        simulated_values = {
            obd.commands.RPM: random.randint(700, 3000),
            obd.commands.SPEED: random.randint(0, 100),
            obd.commands.COOLANT_TEMP: random.randint(75, 95),
            obd.commands.THROTTLE_POS: random.uniform(5, 40),
            obd.commands.ENGINE_LOAD: random.uniform(10, 60),
            obd.commands.INTAKE_TEMP: random.randint(20, 45),
        }

        return simulated_values.get(command)