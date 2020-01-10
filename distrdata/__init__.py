from ._generator_base import generate_dataset


import scipy.stats as stats
from functools import partial


def generate_dataset_normal(range_of_values, *args, **kwargs):
    return generate_dataset(
        range_of_values,
        stats.norm,
        *args,
        **kwargs
    )


class _ScipyGenerator:
    """Binder for not implemented generators from scipy.stats."""

    def __getattr__(self, attr_name):
        return partial(generate_dataset, func=getattr(stats, attr_name))


scipy = _ScipyGenerator()
