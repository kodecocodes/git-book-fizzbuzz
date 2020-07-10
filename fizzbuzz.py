#!/usr/bin/env python


def fizzbuzz_for_num(n):
    should_fizz = n % 3 == 0
    should_buzz = n % 5 == 0
    if should_fizz and should_buzz:
        return "FizzBuzz"
    elif should_fizz:
        return "Fizz"
    elif should_buzz:
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
