from src.models.job import Job


class TestJob:

    def setup_method(self):
        self.job = Job()

    def test__should_create_new_instance_of_job_with_hours(self):
        assert self.job.at_standard_rate == 0
        assert self.job.at_overtime_rate == 0
        assert self.job.at_alternate_rate == 0
