def mean(values):
    """
    :param values: a list of floats
    :return: the mean of all numbers in values
    """
    return int(len(values) > 0) and sum(values) / len(values)


def median(values):
    """
    :param values: a list of floats
    :return: the median of all numbers in values
    """
    sorted_values = sorted(values)
    n = len(sorted_values)
    return (sorted_values[n // 2 - (n%2 == 0)] + sorted_values[n // 2]) / 2