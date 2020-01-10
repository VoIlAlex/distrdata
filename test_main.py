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

    def test_function_as_func_arg(self):
        data = distrdata.generate_dataset(
            100,
            lambda x: x
        )
        assert data.shape == (100, 2)

    def test_radius_int_window(self):
        data = distrdata.generate_window_dataset(
            100,
            norm,
            10
        )
        assert data.shape == (91, 10, 2)

    def test_radius_tuple_window(self):
        data = distrdata.generate_window_dataset(
            (-5, 5, 0.1),
            norm,
            10
        )
        assert data.shape == (91, 10, 2)

    def test_upper_border_window(self):
        data = distrdata.generate_window_dataset(
            100,
            norm,
            10,
            upper_border=10.0
        )
        assert data[:, :, 1].max() == 10.0


class TestGeneratorNorm:
    def test_generation(self):
        data = distrdata.generate_dataset_normal(100)
        assert data.shape == (100, 2)
