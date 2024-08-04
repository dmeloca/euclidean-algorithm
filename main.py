def linear_combination(process: list) -> str:
    pass


def correct_values(a: int, b: int) -> tuple:
    if a < 0:
        a = -1 * a
    elif b < 0:
        b = -1 * b
    return (a, b)


def get_quotient(dividend: int, divisor: int, remainder: int) -> int:
    quotient: int = (dividend-remainder)/divisor
    return int(quotient)

def division(dividend: int, divisor: int) -> tuple:
    dividend, divisor = correct_values(dividend, divisor)
    remainder: int = dividend%divisor
    quotient: int = get_quotient(dividend, divisor, remainder)
    return (dividend, divisor, quotient, remainder)


def mcd(a: int, b: int) -> list:
    operations: list = []
    result: tuple = division(a, b)
    operations.append(result)
    while result[3] != 0: 
        result: tuple = division(result[1], result[3])
        operations.append(result)
    return operations[-2][3]


def main() -> None:
    print(mcd(687, -234))  ## (a, b) where a is divided by b

if __name__ == "__main__": 
    main() 
