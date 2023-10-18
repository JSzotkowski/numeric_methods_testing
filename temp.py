import random


def get_rand(min_, max_):
    return random.random() * (max_ - min_) + min_


if __name__ == '__main__':
    a, b, c = get_rand(-1000, 1000), get_rand(-1000, 1000), get_rand(-1000, 1000)

    i = 0
    while True:
        i += 1
        assert max(a + b, c) < max(a, c) + max(b, c)
        if i % 100000 == 0:
            print(i)
