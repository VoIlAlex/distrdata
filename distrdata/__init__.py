from ._generator_base import generate_dataset


import scipy.stats as stats


def generate_dataset_normal(range_of_values, *args, **kwargs):
    return generate_dataset(
        range_of_values,
        stats.norm,
        *args,
        **kwargs
    )
