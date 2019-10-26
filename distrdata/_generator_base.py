"""
    scipy.stats-compatible datasets generator.
"""

import numpy as np
from collections.abc import Iterable


__all__ = [
    "generate_dataset"
]


def generate_dataset(
        range_of_values: [Iterable, int],
        func: callable,
        *args,
        shuffle=False,
        noise_radius: float = 0,
        upper_border: float = None,
        **kwargs) -> np.ndarray:
    """
    Generates a dataset from the given distribution function.

    Arguments:
        range_of_values {[Iterable, int]} -- range of input values for the function
        func {callable} -- distribution function of the dataset

    Keyword Arguments:
        shuffle {bull} -- indicates whether the generated dataset must be shuffled (default: {False})
        noise_radius {int} -- radius of the noise added to the dataset (default: {0})
        upper_border {int} -- the maximum of the generated values (default: {None})

    Returns:
        np.ndarray -- dataset with format [[x1, y1], [x2, y2], ... [xn, yn]]
    """

    # convert range of values
    # to tuple if it isn't
    if not isinstance(range_of_values, Iterable):
        range_of_values = (range_of_values,)

    # generate the dataset
    X = np.arange(*range_of_values)
    y = np.array([func(*args, **kwargs).pdf(x) for x in X])

    # move to the
    # upper border
    if upper_border is not None:
        coefficient = upper_border / np.max(y)
        y *= coefficient

    # add the noise
    y += np.array([
        (np.random.rand() - 0.5) * 2.0 * noise_radius for _ in X
    ])

    # prepare for concatenation
    X = X.reshape(-1, 1)
    y = y.reshape(-1, 1)

    # convert to format [[x1, y1], [x2, y2], ... [xn, yn]]
    dataset = np.concatenate((X, y), axis=1)

    if shuffle:
        np.random.shuffle(dataset)

    return dataset


if __name__ == "__main__":
    from scipy.stats import norm
    import pandas as pd
    import matplotlib.pyplot as plt
    dataset = generate_dataset(
        (-30, 30, 0.2),
        norm,
        noise_radius=2,
        shuffle=False,
        upper_border=10,
        loc=0,
        scale=10
    )
    print(dataset.shape)
    print(pd.DataFrame(dataset).head())
    plt.scatter(dataset[:, 0], dataset[:, 1])
    plt.show()
