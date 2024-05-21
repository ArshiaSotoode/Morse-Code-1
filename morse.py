from morse_codes import *
from time import sleep


def main():
    typy("hello there 😍", wait=1)
    while True:
        typy("Do you want to encode or decode ? ", next=False)
        process = input("").lower().strip()
        morse_code_engine = MorseCode()
        if process == "encode":
            typy("what is the text you want to encode ? ", next=False)
            text = input()
            encoded_morse_code = morse_code_engine.encode(text)
            typy("please wait we are processing your text", speed=0.07)
            typy("here is your morse code: ", next=False)
            typy(encoded_morse_code, speed=0.1, wait=1)
            typy("do you want to explore more ?(yes,no)", next=False)
            answer = input("").lower().strip()
            if answer == "yes":
                continue
            else:
                typy("it was my pleaser talking to you. Bye🤗", wait=0.8)
                break

        elif process == "decode":
            typy("what is the morse code you want to decode ? ", next=False)
            morse_code = input()
            decoded_morse_code = morse_code_engine.decode(morse_code)
            typy("please wait we are processing your text", speed=0.07)
            typy("here is your decoded morse code: ", next=False)
            typy(decoded_morse_code, speed=0.1)
            typy("do you want to explore more ?(yes,no)", next=False)
            answer = input("").lower().strip()
            if answer == "yes":
                continue
            else:
                typy("it was my pleaser talking to you. Bye🤗", wait=0.8)
                break
        else:
            typy(f'"{process}" is not an operation!!!', wait=0.8)
            typy(
                "do you want to try one more time or leave the program ?(yes,no) ",
                next=False,
            )
            answer = input("").lower().strip()
            if answer == "yes":
                continue
            else:
                typy("it was my pleaser talking to you. Bye🤗", wait=0.8)
                break


def typy(txt, speed=0.05, next=True, wait=0):
    for char in txt:
        sleep(speed)
        print(char, end="", flush=True)
    sleep(wait)
    if next:
        print()


class MorseCode:
    def __init__(self):
        pass

    def encode(self, string: str) -> str:
        self.encoded_string = ""
        # going through each character and inserting the equal morse code into the encoded string
        for char in string:
            if char.upper() in MORSE_CODE_DICT:
                self.encoded_string += MORSE_CODE_DICT[char.upper()]
            else:
                print(f"Invalid character!!!\ncannot encode: {char}")

        return self.encoded_string

    def decode(self, string: str) -> str:
        self.decoded_string = ""
        # splitting the morse code into its core characters
        splitted_morse_code = string.split(" ")
        for morse_code in splitted_morse_code:
            if morse_code in MORSE_CODE_DICT_REVERSE:
                self.decoded_string += MORSE_CODE_DICT_REVERSE[morse_code]
            else:
                print(f"Unknown Morse code: {morse_code}")
        return self.decoded_string


if __name__ == "__main__":
    main()
