def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


@coroutine
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
    while True:
        try:
            print("Delegator. Before yield")
            data = yield
            print(f"Delegator. After yield: {data}")
            g.send(data)
        except BlaBlaException as e:
            print(f"Delegator. BlaBlaException: {e}")
            g.throw(e)


if __name__ == '__main__':
    sg = subgen()
    g = delegator(sg)
    g.send('Hello')
    g.send('World')
    # g.throw(BlaBlaException)
