def ft_filter(func, itera):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if (func):
        return (truc for truc in itera if func(truc))
    return (truc for truc in itera if truc)
