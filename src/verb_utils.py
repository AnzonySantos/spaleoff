"""
Anzony Santos
April 3, 2026
Contains the helper function to load verbs
"""

import json
import random
from enum import Enum

class Forms(Enum):
    YO = 1
    TU = 2
    EL_ELLA_USTED = 3
    NOSOTROS = 4
    VOSOTROS = 5
    ELLOS_ELLAS_USTEDES = 6


def get_verbs() -> str:
    with open("verbs.json") as file:
        data = json.load(file)
    return data


def get_random_verb(verbs: list) -> dict:
    verb_index = random.randint(0, len(verbs) - 1)
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


def update_verb_attributes(verbs: list, tense: str):
    updated_verb = get_random_verb(verbs)
    temp_tuple = get_random_form(updated_verb, tense)

    return (updated_verb, temp_tuple)


def validate_answer(input: str, answer: str) -> bool:  # Find a better way to validate answer later like standerdizing comparison to all caps and ignore spaces or somethin
    return input == answer
