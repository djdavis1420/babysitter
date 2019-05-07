from src.models.family import Family


class TestFamily:

    def setup_method(self):
        self.family = Family('Smith', 12, 8, 16)

    def test__should_create_new_instance_of_family_with_rates(self):
        assert self.family.name == 'Smith'
        assert self.family.standard_rate == 12
        assert self.family.overtime_rate == 8
        assert self.family.alternate_rate == 16

    def test_set_hour_schedule__should_update_hour_schedule_dictionary(self):
        end_standard_rate = 2200
        start_overtime_rate = 0

        self.family.set_hour_schedule(end_standard_rate, start_overtime_rate)

        assert self.family.hour_schedule == {'standard_rate_limit': 2200, 'overtime_rate_limit': 0}
