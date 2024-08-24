
def ext_euc(a: int, b: int) -> tuple[int, int]:
    if b == 0:
        return 1, 0
    x, y = ext_euc(b, a % b)
    return y, x - (a // b) * y


def ext_euc_act(a: int, b: int) -> None:
    a, b = 25, 15
    x, y = ext_euc(a, b)
    print(f'{x = }, {y = }')
    print(f'{x * a + y * b = }')


def main() -> None:
    ...


if __name__ == '__main__':
    main()
