def f(a: int, b: int) -> int:

    def g(b: int) -> int:
        return b + 1

    return a + g(b)

if __name__ == '__main__':
    print("Hi from a folder")
    print(f(1, 2))