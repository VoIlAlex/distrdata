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
        *args -- used by func if it's a functor

    Keyword Arguments:
        shuffle {bull} -- indicates whether the generated dataset must be shuffled (default: {False})
        noise_radius {int} -- radius of the noise added to the dataset (default: {0})
        upper_border {int} -- the maximum of the generated values (default: {None})
        **kwargs -- used by func if it's a functor

    Returns:
        np.ndarray -- dataset with format [[x1, y1], [x2, y2], ... [xn, yn]]

    """

    # convert range of values
    # to tuple if it isn't
    if not isinstance(range_of_values, Iterable):
        range_of_values = (range_of_values,)

    # get actual function-generator
    try:
        generator = func(*args, **kwargs)
        if hasattr(generator, 'pdf'):
            generator = generator.pdf
        else:
            generator = func
    except TypeError:
        generator = func

    # generate the dataset
    X = np.arange(*range_of_values, dtype=np.float)
    y = np.array([generator(x) for x in X], dtype=np.float)

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


def generate_window_dataset(
        range_of_values: [Iterable, int],
        func: callable,
        window_size: int,
        *args,
        shuffle=False,
        noise_radius: float = 0,
        upper_border: float = None,
        stride: int = 1,
        **kwargs) -> np.ndarray:
    """
    Generates a dataset from the given distribution function.

    Arguments:
        range_of_values {[Iterable, int]} -- range of input values for the function
        func {callable} -- distribution function of the dataset
        window_size -- size of the window 
        *args -- used by func if it's a functor

    Keyword Arguments:
        shuffle {bull} -- indicates whether the generated dataset must be shuffled (default: {False})
        noise_radius {int} -- radius of the noise added to the dataset (default: {0})
        upper_border {int} -- the maximum of the generated values (default: {None})
        stride {int} -- distance between start of window n and start of window n + 1 (default: {1})
        **kwargs -- used by func if it's a functor

    Returns:
        np.ndarray -- dataset with shape (S, W, 2), where S - number of samples, W - width of the window, 2 - coordinates
    """
    # convert range of values
    # to tuple if it isn't
    if isinstance(range_of_values, int):
        range_of_values = (0, range_of_values, 1)

    # get actual function-generator
    try:
        generator = func(*args, **kwargs)
        if hasattr(generator, 'pdf'):
            generator = generator.pdf
        else:
            generator = func
    except TypeError:
        generator = func

    # generate the dataset
    dataset = []
    for i in np.arange(range_of_values[0], range_of_values[1] - (window_size - 1) * range_of_values[2], stride * range_of_values[2]):
        X = np.arange(i, i + window_size *
                      range_of_values[2], range_of_values[2], dtype=np.float)
        y = np.array([generator(x) for x in X], dtype=np.float)

        # add the noise
        y += np.array([
            (np.random.rand() - 0.5) * 2.0 * noise_radius for _ in X
        ])

        # prepare for concatenation
        X = X.reshape(-1, 1)
        y = y.reshape(-1, 1)

        # convert to format [[x1, y1], [x2, y2], ... [xn, yn]]
        sample = np.concatenate((X, y), axis=1)
        dataset.append(sample)

    dataset = np.array(dataset)

    # move to the
    # upper border
    if upper_border is not None:
        coefficient = upper_border / dataset[:, :, 1].max()
        dataset[:, :, 1] *= coefficient

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
