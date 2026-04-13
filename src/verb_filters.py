"""
Anzony Santos
April 13, 2026
Test for filtering verbs
"""
import verb_utils
import random

def basic_verbs(verbs: list) -> list:
    new_verb_list: list = []

    for entry in verbs:
        if entry["infinitive"] == "decir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "estar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "haber":
            new_verb_list.append(entry)
        if entry["infinitive"] == "hacer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "ir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "poner":
            new_verb_list.append(entry)
        if entry["infinitive"] == "ser":
            new_verb_list.append(entry)
        if entry["infinitive"] == "tener":
            new_verb_list.append(entry)
        if entry["infinitive"] == "venir":
            new_verb_list.append(entry)
    return new_verb_list


def regular_verbs(verbs: list) -> list:
    new_verb_list: list = []

    for entry in verbs:
        if entry["infinitive"] == "bailar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "cantar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "comer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "correr":
            new_verb_list.append(entry)
        if entry["infinitive"] == "escribir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "hablar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "subir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "terminar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "vender":
            new_verb_list.append(entry)
        if entry["infinitive"] == "vivir":
            new_verb_list.append(entry)

    return new_verb_list


def present_irregular_verbs(verbs: list) -> list:
    new_verb_list: list = []
    for entry in verbs:
        if entry["infinitive"] == "cerrar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "comenzar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "dar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "encontrar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "perder":
            new_verb_list.append(entry)
        if entry["infinitive"] == "querer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "saber":
            new_verb_list.append(entry)
        if entry["infinitive"] == "salir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "traer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "ver":
            new_verb_list.append(entry)

    return new_verb_list


def learning_verbs(verbs: list) -> list:
    new_verb_list: list = []
    for entry in verbs:
        if entry["infinitive"] == "aprender":
            new_verb_list.append(entry)
        if entry["infinitive"] == "entender":
            new_verb_list.append(entry)
        if entry["infinitive"] == "estudiar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "explicar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "olvidar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "pensar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "preguntar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "saber":
            new_verb_list.append(entry)
        if entry["infinitive"] == "traducir":
            new_verb_list.append(entry)

    return new_verb_list


def traveling_verbs(verbs: list) -> list:
    new_verb_list: list = []
    for entry in verbs:
        if entry["infinitive"] == "buscar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "comer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "comprar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "dormir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "encontrar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "llevar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "necesitar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "pagar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "tomar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "viajar":
            new_verb_list.append(entry)

    return new_verb_list


def preterite_irregular_verbs(verbs: list) -> list:
    new_verb_list: list = []
    for entry in verbs:
        if entry["infinitive"] == "creer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "dar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "dormir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "leer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "pagar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "querer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "saber":
            new_verb_list.append(entry)
        if entry["infinitive"] == "traducir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "traer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "ver":
            new_verb_list.append(entry)

    return new_verb_list


def imperfect_irregular_verbs(verbs: list) -> list:
    new_verb_list: list = []
    for entry in verbs:
        if entry["infinitive"] == "ir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "ser":
            new_verb_list.append(entry)
        if entry["infinitive"] == "ver":
            new_verb_list.append(entry)

    return new_verb_list


def future_irregular_verbs(verbs: list) -> list:
    new_verb_list: list = []
    for entry in verbs:
        if entry["infinitive"] == "querer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "saber":
            new_verb_list.append(entry)
        if entry["infinitive"] == "salir":
            new_verb_list.append(entry)

    return new_verb_list


def subjunctive_present_irregular_verbs(verbs: list) -> list:
    new_verb_list: list = []
    for entry in verbs:
        if entry["infinitive"] == "cerrar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "comenzar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "dar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "encontrar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "perder":
            new_verb_list.append(entry)
        if entry["infinitive"] == "querer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "saber":
            new_verb_list.append(entry)
        if entry["infinitive"] == "salir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "traer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "ver":
            new_verb_list.append(entry)

    return new_verb_list


def subjunctive_imperfect_irregular_verbs(verbs: list) -> list:
    new_verb_list: list = []
    for entry in verbs:
        if entry["infinitive"] == "creer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "dar":
            new_verb_list.append(entry)
        if entry["infinitive"] == "dormir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "leer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "querer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "saber":
            new_verb_list.append(entry)
        if entry["infinitive"] == "traducir":
            new_verb_list.append(entry)
        if entry["infinitive"] == "traer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "ver":
            new_verb_list.append(entry)

    return new_verb_list


def conditional_irregular_verbs(verbs: list) -> list:
    new_verb_list: list = []
    for entry in verbs:
        if entry["infinitive"] == "querer":
            new_verb_list.append(entry)
        if entry["infinitive"] == "saber":
            new_verb_list.append(entry)
        if entry["infinitive"] == "salir":
            new_verb_list.append(entry)

    return new_verb_list


def random_verbs(verbs: list) -> list:
    new_verb_list: list = []
    for i in range(10):
        new_verb_list.append(verbs[random.randint(0, len(verbs) - 1)])
    return new_verb_list


if __name__ == "__main__":
    all_verbs: list = verb_utils.get_verbs()
    basic_verb_list = basic_verbs(all_verbs)
    regular_verb_list = regular_verbs(all_verbs)
    learning_verb_list = learning_verbs(all_verbs)
    traveling_verb_list = traveling_verbs(all_verbs)
    random_verb_list = random_verbs(all_verbs)

    print("---------------------")
    for entry in basic_verb_list:
        print(entry["infinitive"])
    print("---------------------")
    for entry in regular_verb_list:
        print(entry["infinitive"])
    print("---------------------")
    for entry in learning_verb_list:
        print(entry["infinitive"])
        print(entry["conjugations"]["conditional"])
    print("---------------------")
    for entry in traveling_verb_list:
        print(entry["infinitive"])
    print("---------------------")

    print("---------------------")
    for entry in random_verb_list:
        print(entry["infinitive"])
    print("---------------------")
