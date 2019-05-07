class Job:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.hours_at_standard_rate = 0
        self.hours_at_overtime_rate = 0
        self.hours_at_alternate_rate = 0
