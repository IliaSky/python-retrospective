from collections import OrderedDict


def groupby(func, seq):
    result = {func(x): [] for x in seq}
    for x in seq:
        result[func(x)].append(x)
    return result


def iterate(func):
    return Iterator(func)


class Iterator():
    def __init__(self, func):
        self.func = func

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current = self.current
            self.current = lambda x: self.func(current(x))
        except AttributeError:
            self.current = lambda x: x
        return self.current


def zip_with(func, *iterables):
    return [func(*args) for args in zip(*iterables)]


def cache(func, cache_size):
    if not hasattr(cache, 'dict'):
        cache.dict = OrderedDict()

    def func_cached(*args):
        if args in cache.dict:
            return cache.dict[args]
        else:
            value = func(*args)
            if cache_size > 0:
                if len(cache.dict) == cache_size:
                    cache.dict.popitem(last=False)
                cache.dict[args] = value
            return value
    return func_cached
