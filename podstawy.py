def dodawanie():
    a = 2
    b = 3
    print(f'a+b = {a + b}')
    a = 3
    print(f'a+b = {a + b}')
    print(f'a+b = a+b')


def petla():
    for x in range(10):
        print(x)


def hello_world():
    print('Hello world!')


def warunek():
    for x in range(10):
        print(x)
        if x == 1:
            print('warunek spelniony')


if __name__ == "__main__":
    hello_world()
    # dodawanie()
    # petla()
    # warunek()