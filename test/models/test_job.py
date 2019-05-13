from mock import Mock

from src.models.job import Job


class TestJob:

    def setup_method(self):
        self.job = Job(1800, 200)
        self.family = Mock()
        self.babysitter = Mock()
        self.babysitter.start_time = 1700
        self.babysitter.end_time = 400

    def test__should_create_new_instance_of_job_with_hours(self):
        assert self.job.start_time == 1800
        assert self.job.end_time == 200
        assert self.job.hours_at_standard_rate == 0
        assert self.job.hours_at_overtime_rate == 0
        assert self.job.hours_at_alternate_rate == 0

    def test_is_valid_job__should_return_true_for_job_with_valid_hours(self):
        actual = self.job.is_valid_job(self.babysitter)

        assert actual is True

    def test_is_valid_job__should_return_false_for_job_with_invalid_start_time(self):
        self.babysitter.start_time = 2000
        actual = self.job.is_valid_job(self.babysitter)

        assert actual is False

    def test_is_valid_job__should_return_false_for_job_with_invalid_end_time(self):
        self.babysitter.end_time = 0
        actual = self.job.is_valid_job(self.babysitter)

        assert actual is False

    def test_parse_hours__should_update_standard_hours_on_job_to_four(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_standard_rate == 4

    def test_parse_hours__should_update_standard_hours_on_job_to_six(self):
        self.family.hour_schedule = {'standard_rate_limit': 0}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_standard_rate == 6

    def test_parse_hours__should_update_standard_hours_on_job_to_eight(self):
        self.family.hour_schedule = {'standard_rate_limit': 200}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_standard_rate == 8

    def test_parse_hours__should_update_overtime_hours_on_job_to_one(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 2300}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_overtime_rate == 1

    def test_parse_hours__should_update_overtime_hours_on_job_to_two(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 0}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_overtime_rate == 2

    def test_parse_hours__should_update_overtime_hours_on_job_to_three(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 100}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_overtime_rate == 3

    def test_parse_hours__should_update_alternate_hours_on_job_to_one(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 100}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_alternate_rate == 1

    def test_parse_hours__should_update_alternate_hours_on_job_to_two(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 0}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_alternate_rate == 2

    def test_parse_hours__should_update_alternate_hours_on_job_to_three(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 2300}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_alternate_rate == 3

    def test_parse_hours__should_update_standard_hours_to_five_and_overtime_hours_to_three(self):
        self.family.hour_schedule = {'standard_rate_limit': 2300}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_standard_rate == 5
        assert self.job.hours_at_overtime_rate == 3
        assert self.job.hours_at_alternate_rate == 0

    def test_parse_hours__should_update_standard_hours_to_four_and_overtime_hours_to_two_and_alternate_hours_to_two(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 0}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_standard_rate == 4
        assert self.job.hours_at_overtime_rate == 2
        assert self.job.hours_at_alternate_rate == 2

    def test_parse_hours__should_update_standard_hours_to_three_and_overtime_hours_to_five(self):
        self.family.hour_schedule = {'standard_rate_limit': 2100}

        self.job.parse_hours(self.babysitter, self.family)

        assert self.job.hours_at_standard_rate == 3
        assert self.job.hours_at_overtime_rate == 5
        assert self.job.hours_at_alternate_rate == 0

    def test_calculate_pay__should_update_total_pay_on_job_to_fifty_dollars(self):
        self.job.hours_at_standard_rate = 5
        self.family.standard_rate = 10.00

        self.job.calculate_total_pay(self.family)

        assert self.job.total_pay == 50.00
