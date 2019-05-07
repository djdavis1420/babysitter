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
