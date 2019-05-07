from src.models.family import Family


class TestFamily:

    def setup_method(self):
        self.family = Family('Smith', 12, 8, 16)

    def test__should_create_new_instance_of_family_with_rates(self):
        assert self.family.name == 'Smith'
        assert self.family.standard_rate == 12
        assert self.family.overtime_rate == 8
        assert self.family.alternate_rate == 16
