"""
Anzony Santos
April 3, 2026
"""
import json
import random

import verb_utils

debug_flag: bool = False
# Chose tense from "present, preterite'
global_tense: str = "present"


def main():
    init()
    data: list = verb_utils.get_verbs()
    verb: dict = verb_utils.get_random_verb(data)

    number_correct: int = 0
    number_total: int = 0

    if (debug_flag):
        random_number = random.random()
        print(data[1]["infinitive"])
        print(random_number)
        print(verb["conjugations"]["present"])
        print(verb)

    while (True):
        loop_verb: dict = verb_utils.get_random_verb(data)
        temp_tuple: tuple = verb_utils.get_random_form(loop_verb, global_tense)
        current_form, correct_answer = temp_tuple  # Figure out how to add types

        user_input = input(f'{current_form}:{loop_verb["infinitive"]} ')
        state = verb_utils.validate_answer(user_input, correct_answer)

        while (state is False):
            number_total += 1

            print(correct_answer)
            print(f'{number_correct}/{number_total}')

            user_input = input(f'{current_form}:{loop_verb["infinitive"]} ')
            state = verb_utils.validate_answer(user_input, correct_answer)

        if (state is True):
            number_correct += 1
            number_total += 1

            print(correct_answer)
            print(f'{number_correct}/{number_total}')

def init():
    random.seed(1)

if __name__ == "__main__":
    main()
