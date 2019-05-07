class Family:

    def __init__(self, name, standard_rate, overtime_rate=None, alternate_rate=None):
        self.name = name
        self.standard_rate = standard_rate
        self.overtime_rate = overtime_rate
        self.alternate_rate = alternate_rate
        self.hour_schedule = {}

    def set_hour_schedule(self, end_standard_rate, start_overtime_rate):
        self.hour_schedule['standard_rate_limit'] = end_standard_rate
        self.hour_schedule['overtime_rate_limit'] = start_overtime_rate
