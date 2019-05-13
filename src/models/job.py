class Job:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.hours_at_standard_rate = 0
        self.hours_at_overtime_rate = 0
        self.hours_at_alternate_rate = 0
        self.total_pay = 0

    def is_valid_job(self, babysitter):
        if self.__is_valid_start_time(babysitter) and self.__is_valid_end_time(babysitter):
            return True
        return False

    def parse_hours(self, babysitter, family):
        if self.is_valid_job(babysitter):
            self.hours_at_standard_rate = self.__calculate_hours_at_standard_rate(family)
            self.hours_at_overtime_rate = self.__calculate_hours_at_overtime_rate(family)
            self.hours_at_alternate_rate = self.__calculate_hours_at_alternate_rate(family)
        else:
            raise ValueError

    def calculate_total_pay(self, family):
        standard_pay = self.hours_at_standard_rate * family.standard_rate if self.hours_at_standard_rate > 0 else 0
        self.total_pay = round(standard_pay, 2)

    def __is_valid_start_time(self, babysitter):
        if 1200 <= self.start_time <= 2400 and self.start_time >= babysitter.start_time:
            return True
        return False

    def __is_valid_end_time(self, babysitter):
        if 0 < self.end_time < 1200 and self.end_time <= babysitter.end_time:
            return True
        return False

    def __calculate_hours_at_standard_rate(self, family):
        standard_rate_limit = family.hour_schedule.get('standard_rate_limit')
        standard_rate_limit = 2400 if standard_rate_limit == 0 else standard_rate_limit
        hours = (standard_rate_limit - self.start_time) / 100
        return int(hours) if hours > 0 else (24 - abs(int(hours)))

    def __calculate_hours_at_overtime_rate(self, family):
        standard_rate_limit = family.hour_schedule.get('standard_rate_limit')
        if family.hour_schedule.get('overtime_rate_limit') is None:
            hours = (self.end_time - standard_rate_limit) / 100
        else:
            overtime_rate_limit = family.hour_schedule.get('overtime_rate_limit')
            overtime_rate_limit = 2400 if overtime_rate_limit == 0 else overtime_rate_limit
            hours = (overtime_rate_limit - standard_rate_limit) / 100
        return int(hours) if hours > 0 else (24 - abs(int(hours)))

    def __calculate_hours_at_alternate_rate(self, family):
        if family.hour_schedule.get('overtime_rate_limit') is None:
            return 0
        else:
            overtime_rate_limit = family.hour_schedule.get('overtime_rate_limit')
            hours = (self.end_time - overtime_rate_limit) / 100
            return int(hours) if hours > 0 else (24 - abs(int(hours)))
