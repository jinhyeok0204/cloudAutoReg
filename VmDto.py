class VmDto:
    def __init__(self, name_id, system_id):
        self._name_id = name_id
        self._system_id = system_id

    @property
    def get_name_id(self):
        return self._name_id

    @property
    def get_system_id(self):
        return self._system_id

    def __str__(self):
        return f"{self.get_name_id} // {self.get_system_id}"
