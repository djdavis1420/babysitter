from mock import Mock

from src.models.job import Job


class TestJob:

    def setup_method(self):
        self.job = Job(1800, 200)
        self.family = Mock()

    def test__should_create_new_instance_of_job_with_hours(self):
        assert self.job.start_time == 1800
        assert self.job.end_time == 200
        assert self.job.hours_at_standard_rate == 0
        assert self.job.hours_at_overtime_rate == 0
        assert self.job.hours_at_alternate_rate == 0

    def test_is_valid_job__should_return_true_for_job_with_valid_hours(self):
        babysitter = Mock()
        babysitter.start_time = 1700
        babysitter.end_time = 400

        actual = self.job.is_valid_job(babysitter)

        assert actual is True

    def test_parse_hours__should_update_standard_hours_on_job_to_four(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200}

        self.job.parse_hours(self.family)

        assert self.job.hours_at_standard_rate == 4

    def test_parse_hours__should_update_standard_hours_on_job_to_six(self):
        self.family.hour_schedule = {'standard_rate_limit': 0}

        self.job.parse_hours(self.family)

        assert self.job.hours_at_standard_rate == 6

    def test_parse_hours__should_update_standard_hours_on_job_to_eight(self):
        self.family.hour_schedule = {'standard_rate_limit': 200}

        self.job.parse_hours(self.family)

        assert self.job.hours_at_standard_rate == 8

    def test_parse_hours__should_update_overtime_hours_on_job_to_one(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 2300}

        self.job.parse_hours(self.family)

        assert self.job.hours_at_overtime_rate == 1

    def test_parse_hours__should_update_overtime_hours_on_job_to_two(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 0}

        self.job.parse_hours(self.family)

        assert self.job.hours_at_overtime_rate == 2

    def test_parse_hours__should_update_overtime_hours_on_job_to_three(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 100}

        self.job.parse_hours(self.family)

        assert self.job.hours_at_overtime_rate == 3

    def test_parse_hours__should_update_alternate_hours_on_job_to_one(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 100}

        self.job.parse_hours(self.family)

        assert self.job.hours_at_alternate_rate == 1

    def test_parse_hours__should_update_alternate_hours_on_job_to_two(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 0}

        self.job.parse_hours(self.family)

        assert self.job.hours_at_alternate_rate == 2

    def test_parse_hours__should_update_alternate_hours_on_job_to_three(self):
        self.family.hour_schedule = {'standard_rate_limit': 2200, 'overtime_rate_limit': 2300}

        self.job.parse_hours(self.family)

        assert self.job.hours_at_alternate_rate == 3
