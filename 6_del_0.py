def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


def subgen():
    for i in 'egor':
        yield i


def delegator(g):
    for i in g:
        yield i


if __name__ == '__main__':
    sg = subgen()
    g = delegator(sg)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
