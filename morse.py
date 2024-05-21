from morse_codes import *
from time import sleep


def main():
    morse_code_engine = MorseCode()
    typy("hello there 😍", wait=1)
    while True:
        # asking the user for what to do
        asked_process = get_user_input(
            "Do you want to encode or decode?(encode,decode)",
            expected_values=("encode", "decode"),
        )
        if asked_process == "encode":
            text = typy(
                "what is the text you want to encode ? ", next=False, get_input=True
            )
            encoded_morse_code = morse_code_engine.encode(text)
            typy("here is your morse code: ", next=False, speed=0.1)
            typy(encoded_morse_code, speed=0.01, wait=1)
            continue_process = get_user_input(
                "Do you want to continue exploring?(Yes,No)",
                expected_values=("yes", "no"),
            )
            if continue_process == "no":
                typy("it was my pleaser talking to you. Bye🤗", wait=0.8)
                exit()

        elif asked_process == "decode":
            morse_code = typy(
                "what is the morse code you want to decode ? ",
                next=False,
                get_input=True,
            )
            decoded_morse_code = morse_code_engine.decode(morse_code)
            typy("here is your decoded morse code: ", next=False)
            typy(decoded_morse_code, speed=0.1)
            continue_process = get_user_input(
                "Do you want to continue exploring?(Yes,No)",
                expected_values=("yes", "no"),
            )
            if continue_process == "no":
                typy("it was my pleaser talking to you. Bye🤗", wait=0.8)
                exit()


def get_user_input(prompt: str, expected_values: tuple) -> str:
    while True:
        # asking the user with the given prompt
        user_input = typy(prompt, next=False, get_input=True).lower().strip()
        # check if the input is expected and if it is returning the values
        if user_input in expected_values:
            return user_input
        # if the user input is not valid ask him to do it again
        else:
            typy(f'"{user_input}" is not a valid operation!!!', wait=0.5)
            while True:
                continue_prompt = (
                    typy(
                        "do you want to continue or not?(yes,no) ",
                        next=False,
                        get_input=True,
                    )
                    .lower()
                    .strip()
                )
                if continue_prompt == "yes":
                    break
                elif continue_prompt == "no":
                    typy("it was my pleaser talking to you. Bye🤗", wait=0.8)
                    exit()
                else:
                    typy(f'"{continue_prompt}" is not a valid key word!!!', wait=0.5)


# a simple func to type a string character by character
def typy(txt, speed=0.05, next=True, wait=0, get_input=False) -> str | None:
    for char in txt:
        sleep(speed)
        print(char, end="", flush=True)
    sleep(wait)
    if next:
        print()
    if get_input:
        return input()


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
