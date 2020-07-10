#!/usr/bin/env python


def fizzbuzz_for_num(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def fizzbuzz():
    for n in range(1, 101):
        value = fizzbuzz_for_num(n)
        print(value)


def main():
    fizzbuzz()


if __name__ == "__main__":
    main()
