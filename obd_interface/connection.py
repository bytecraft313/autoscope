import obd


class OBDConnection:
    """Manages the connection between AutoScope and the OBD-II adapter."""

    def __init__(self, port=None, simulation=False):
        self.simulation = simulation
        self.connection = None

        if not simulation:
            self.connection = obd.OBD(port)

    @property
    def connected(self):
        if self.simulation:
            return True
        return self.connection is not None and self.connection.is_connected()

    def status(self):
        if self.simulation:
            return "Simulation Mode"
        return "Connected" if self.connected else "Disconnected"