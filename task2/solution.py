from collections import OrderedDict


def groupby(func, seq):
    result = {func(x): [] for x in seq}
    for x in seq:
        result[func(x)].append(x)
    return result


def compose(outer, inner):
    return lambda x: outer(inner(x))


def iterate(func):
    result = lambda x: x

    while True:
        yield result
        result = compose(func, result)


def zip_with(func, *iterables):
    return [func(*args) for args in zip(*iterables)]


def cache(func, cache_size):
    cached_calls = OrderedDict()

    def func_cached(*args):
        if args in cached_calls:
            return cached_calls[args]
        else:
            value = func(*args)
            if cache_size > 0:
                if len(cached_calls) == cache_size:
                    cached_calls.popitem(last=False)
                cached_calls[args] = value
            return value
    return func_cached
