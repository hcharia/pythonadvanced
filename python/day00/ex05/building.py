#!/usr/bin/env python3

import sys
import string

def is_punctuation(ch: str) -> bool:
    return ch in string.punctuation

def main():
    text = ""
    up_letters = 0
    lo_letters = 0
    punctuation = 0
    spaces = 0
    digits = 0

    if len(sys.argv) > 2:
        print("too much arguments, stick with one")
        return
    if len(sys.argv) == 1:
        while text == "":
            try:
                print("What is the text to count?")
                text = sys.stdin.readline()
                if text == "":
                    return
            except (EOFError, KeyboardInterrupt):
                return
    else:
        text = sys.argv[1]
    print(f"The text contains {len(text)} characters:")
    for element in text:
        if element.isupper():
            up_letters += 1
        elif element.islower():
            lo_letters += 1
        elif is_punctuation(element):
            punctuation += 1
        elif element.isspace():
            spaces += 1
        elif element.isdigit():
            digits += 1
    print(f"{up_letters} upper letters")
    print(f"{lo_letters} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")

    


if __name__ == "__main__":
    main()