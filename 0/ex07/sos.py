import sys


def main():
    NESTED_MORSE = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ' ': '/'}
    if (len(sys.argv) != 2):
        print("AssertionError: the arguments are bad")
        return
    string = sys.argv[1].upper()
    morse: str = ""
    for char in string:
        if morse != "":
            morse += " "
        if (char in NESTED_MORSE):
            morse += NESTED_MORSE[char]
        else:
            print("AssertionError: the arguments are bad")
            return
    print(morse)


if __name__ == "__main__":
    main()
