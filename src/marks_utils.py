
import numpy as np


def standardise_loop(data):
    """Standardise each column using Python loops."""
    rows = data.tolist()
    n_rows = len(rows)
    n_cols = len(rows[0])

    means = []
    stds = []

    for j in range(n_cols):
        column = [rows[i][j] for i in range(n_rows)]
        mean = sum(column) / n_rows
        variance = sum((x - mean) ** 2 for x in column) / n_rows
        means.append(mean)
        stds.append(variance ** 0.5)

    result = []
    for i in range(n_rows):
        new_row = []
        for j in range(n_cols):
            if stds[j] == 0:
                new_row.append(0.0)
            else:
                new_row.append((rows[i][j] - means[j]) / stds[j])
        result.append(new_row)

    return np.array(result)


def standardise_np(data):
    """Standardise each column using NumPy broadcasting."""
    means = data.mean(axis=0)
    stds = data.std(axis=0)

    safe_stds = np.where(stds == 0, 1, stds)
    return (data - means) / safe_stds
