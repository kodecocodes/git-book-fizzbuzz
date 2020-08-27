#!/usr/bin/env python


def fizzbuzz_for_num(
    n,
    fizz_divisor=3,
    fizz_word="Fizz",
    buzz_divisor=5,
    buzz_word="Buzz",
):
    should_fizz = n % fizz_divisor == 0
    should_buzz = n % buzz_divisor == 0
    if should_fizz and should_buzz:
        return fizz_word + buzz_word
    elif should_fizz:
        return fizz_word
    elif should_buzz:
        return buzz_word
    else:
        return str(n)


def fizzbuzz(start=1, end=100):
    for n in range(start, end + 1):
        value = fizzbuzz_for_num(n)
        print(value)


def main():
    fizzbuzz()


if __name__ == "__main__":
    main()
