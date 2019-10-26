import distrdata
from scipy.stats import norm


class TestGeneratorBase:
    def test_radius_int(self):
        data = distrdata.generate_dataset(
            100,
            norm
        )
        assert data.shape == (100, 2)

    def test_radius_tuple(self):
        data = distrdata.generate_dataset(
            (-10, 10, 0.1),
            norm
        )
        assert data.shape == (200, 2)

    def test_upper_border(self):
        data = distrdata.generate_dataset(
            100,
            norm,
            upper_border=10.0
        )
        assert data[:, 1].max() == 10.0


class TestGeneratorNorm:
    def test_generation(self):
        data = distrdata.generate_dataset_normal(100)
        assert data.shape == (100, 2)
