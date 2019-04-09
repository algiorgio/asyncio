def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


def subgen():
    while True:
        try:
            print("Subgen. Before yield")
            message = yield
            print(f"Subgen. After yield: {message}")
        except BlaBlaException:
            print('Subgen. BlaBlaException')
        else:
            print(f'Subgen. --- Else block: {message}')


@coroutine
def delegator(g):
    yield from g


if __name__ == '__main__':
    sg = subgen()
    g = delegator(sg)
    g.send('Hello')
    g.send('World')
    g.throw(BlaBlaException)
    g.send('!!!')