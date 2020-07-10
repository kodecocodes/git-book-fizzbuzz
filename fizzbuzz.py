#!/usr/bin/env python


def fizzbuzz_for_num(n):
    should_fizz = n % 3 == 0
    should_buzz = n % 5 == 0
    fizz_word = "Fizz"
    buzz_word = "Buzz"
    if should_fizz and should_buzz:
        return fizz_word + buzz_word
    elif should_fizz:
        return fizz_word
    elif should_buzz:
        return buzz_word
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
