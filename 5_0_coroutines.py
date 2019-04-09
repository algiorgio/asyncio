def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received: ', message)


class BlaBlaException(Exception):
    pass


def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        except BlaBlaException:
            print('.....................')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)


if __name__  == '__main__':
    g = average()
    print(g.send(None))
    print(g.send(4))
    print(g.send(5))
    print(g.send(10))
