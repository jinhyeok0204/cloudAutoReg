class ConnConfigDto:
    def __init__(self, configName):
        self._configName = configName

    @property
    def configName(self):
        return self._configName

    def __str__(self):
        return f"Config Name: {self.configName}"

