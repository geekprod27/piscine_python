import sys
from ft_filter import ft_filter


def main():
    if (len(sys.argv) != 3):
        print("AssertionError: the arguments are bad")
        return
    if ((not isinstance(sys.argv[1], str)) or (not sys.argv[2].isdigit())):
        print("AssertionError: the arguments are bad")
        return
    text = sys.argv[1].split(" ")
    num = int(sys.argv[2])
    filtered = list(ft_filter(lambda x: len(x) > num, text))
    print(filtered)


if __name__ == "__main__":
    main()
