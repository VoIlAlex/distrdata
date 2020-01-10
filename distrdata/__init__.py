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


# To be used as module with `scipy` functions
#
# For example:
# scipy.norm - points to generator, bound with norm function from scipy
#
# It binds the distrdata module to scipy module,
# so it will work for new functionality if it appears
# in scipy.
scipy = _ScipyGenerator()
