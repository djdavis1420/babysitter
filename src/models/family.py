class Family:

    def __init__(self, name, standard_rate, overtime_rate=None, alternate_rate=None):
        self.name = name
        self.standard_rate = standard_rate
        self.overtime_rate = overtime_rate
        self.alternate_rate = alternate_rate
