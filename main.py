from feature1 import feature1

from feature2 import feature2, nome

from feature3 import feature3


def base():
    print('base')
    feature1()
    feature2()
    feature3()
    print(nome)


if __name__ == '__main__':
    base()
