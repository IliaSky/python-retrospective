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
    if not hasattr(cache, 'arguments'):
        cache.arguments = []
        cache.values = []

    def func_cached(*args):
        if args in cache.arguments:
            index = cache.arguments.index(args)
            cache.arguments.insert(0, cache.arguments.pop(index))
            cache.values.insert(0, cache.values.pop(index))
            return cache.values[0]
        else:
            value = func(*args)
            cache.arguments.append(args)
            cache.values.append(value)
            return value
    return func_cached
