from src.models.babysitter import Babysitter


class TestBabysitter:

    def setup_method(self):
        self.babysitter = Babysitter('Dylan', 1700, 400)

    def test__should_create_new_instance_of_babysitter(self):
        assert self.babysitter.name == 'Dylan'
        assert self.babysitter.start_time == 1700
        assert self.babysitter.end_time == 400
