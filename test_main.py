import distrdata
from scipy.stats import norm


class TestGeneratorBase:
    def test_radius_int(self):
        data = distrdata.generate_dataset(
            100,
            norm
        )

    def test_radius_tuple(self):
        data = distrdata.generate_dataset(
            (-10, 10, 0.1),
            norm
        )

    def test_upper_border(self):
        data = distrdata.generate_dataset(
            100,
            norm,
            upper_border=10.0
        )
        assert data[:, 1].max() == 10.0
