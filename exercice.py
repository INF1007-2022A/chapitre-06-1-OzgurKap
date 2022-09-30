#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        print('Veuillez entrer 10 valeurs svp. ')
        liste1 = []
        for i in range(10):
            liste1.append(input())
        liste1.sort()
        print(liste1)
        pass

    return [liste1]
"""


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        print('Veuillez ecrire 2 mots.')
        mot1 = input('Veuillez ecrire la premiere ici')
        mot2 = input('Veuillez ecrire la deuxieme ici')
        c = 0
        d = 0
        for i in range(len(mot1)):
            if mot1[i] in mot2:
                c += 1
            else:
                return False
        for a in range(len(mot2)):
            if mot2[a] in mot1:
                d += 1
            else:
                return False

        if d == len(mot1) - 1 and c == len(mot2) - 1:
            return True

        pass

    return False


def contains_doubles(items: list) -> bool:
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    """""
    print(f"On essaie d'ordonner les valeurs...")
    order()
    """""
    print(f"On vérifie les anagrammes...")
    if anagrams():
        print('oui')
    else:
        print("non")

"""
    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)"""


if __name__ == '__main__':
    main()
