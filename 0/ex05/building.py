import sys


def main():
    arg = ""
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided")
    elif (len(sys.argv) == 1):
        print("What is the text to count?")
        arg = sys.stdin.readline()
    else:
        arg = sys.argv[1]
    tot = 0
    up = 0
    lo = 0
    pon = 0
    space = 0
    digi = 0
    for c in arg:
        if c.isupper():
            up += 1
        elif c.islower():
            lo += 1
        elif c.isdigit():
            digi += 1
        elif c == ' ' or c == '\n':
            space += 1
        elif c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            pon += 1
        tot += 1
    print(f"The text contains {tot} characters:")
    print(f"{up} upper letters")
    print(f"{lo} lower letters")
    print(f"{pon} punctuation marks")
    print(f"{space} spaces")
    print(f"{digi} digits")


if __name__ == "__main__":
    main()
