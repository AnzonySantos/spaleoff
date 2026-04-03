"""
Anzony Santos
April 3, 2026
"""
import json
import random
from enum import Enum

debug_flag: bool = False
# Chose tense from "present, preterite'
global_tense: str = "present"


class Forms(Enum):
    YO = 1
    TU = 2
    EL_ELLA_USTED = 3
    NOSOTROS = 4
    VOSOTROS = 5
    ELLOS_ELLAS_USTEDES = 6


def main():
    init()
    data: list = get_verbs()
    verb: dict = get_random_verb(data)

    number_correct: int = 0
    number_total: int = 0

    if (debug_flag):
        random_number = random.random()
        print(data[1]["infinitive"])
        print(random_number)
        print(verb["conjugations"]["present"])
        print(verb)

    while (True):
        loop_verb: dict = get_random_verb(data)
        temp_tuple: tuple = get_random_form(loop_verb, global_tense)
        current_form, correct_answer = temp_tuple  # Figure out how to add types

        user_input = input(f'{current_form}:{loop_verb["infinitive"]} ')
        state = validate_answer(user_input, correct_answer)

        while (state is False):
            number_total += 1

            print(correct_answer)
            print(f'{number_correct}/{number_total}')

            user_input = input(f'{current_form}:{loop_verb["infinitive"]} ')
            state = validate_answer(user_input, correct_answer)

        if (state is True):
            number_correct += 1
            number_total += 1

            print(correct_answer)
            print(f'{number_correct}/{number_total}')

def init():
    random.seed(1)


def get_verbs() -> str:
    with open("verbs.json") as file:
        data = json.load(file)
    return data


def get_random_verb(verbs: list) -> dict:
    verb_index = random.randint(0, len(verbs))
    return (verbs[verb_index])


def get_random_form(verb: dict, tense: str) -> str:
    random_number = random.randint(1, 6)
    form = enum_to_string(random_number)
    return (form, verb["conjugations"][tense][form])


def enum_to_string(form: int) -> str:
    ret: str = ""  # May change default initalization

    if form == Forms.YO.value:
        ret = "yo"
    elif form == Forms.TU.value:
        ret = "tu"
    elif form == Forms.EL_ELLA_USTED.value:
        ret = "usted/el/ella"
    elif form == Forms.NOSOTROS.value:
        ret = "nosotros"
    elif form == Forms.VOSOTROS.value:
        ret = "vosotros"
    elif form == Forms.ELLOS_ELLAS_USTEDES.value:
        ret = "ustedes/ellos/ellas"
    else:
        print("ERROR")
        exit(-1)

    return ret


def validate_answer(input: str, answer: str) -> bool:  # Find a better way to validate answer later like standerdizing comparison to all caps and ignore spaces or somethin
    return input == answer


if __name__ == "__main__":
    main()
