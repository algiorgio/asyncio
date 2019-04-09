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
        except StopIteration:
            print('Subgen. BlaBlaException')
            break
        else:
            print(f'Subgen. --- Else block: {message}')
    return 'Returned from subgen()'


@coroutine
def delegator(g):
    result = yield from g
    print(f'Delegator. Result: {result}')


if __name__ == '__main__':
    g = delegator(subgen())
    g.send('Hello')
    g.send('World')
    g.throw(StopIteration)
