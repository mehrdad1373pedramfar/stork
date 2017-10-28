
class Person:

    def __init__(self, name):
        self._name = name

    # def get_name(self):
    #     return self._name
    #
    # def set_name(self, v):
    #     self._name = v
    #
    # name = property(get_name, set_name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v
