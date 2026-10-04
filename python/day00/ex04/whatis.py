#!/usr/bin/env python3

import sys


def is_integer(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():
    if len(sys.argv) == 1:
        return
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    if is_integer(sys.argv[1]) and int(sys.argv[1]) % 2 == 1:
        print("I'm Odd")
    elif is_integer(sys.argv[1]) and int(sys.argv[1]) % 2 == 0:
        print("I'm Even")
    else:
        print("AssertionError: argument is not an integer")
    return


if __name__ == "__main__":
    main()
