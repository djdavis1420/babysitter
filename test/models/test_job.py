from mock import Mock

from src.models.job import Job


class TestJob:

    def setup_method(self):
        self.job = Job(1800, 200)

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
