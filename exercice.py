#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


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


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        print('Veuillez ecrire 2 mots.')
        mot1 = input('Veuillez ecrire la premiere ici')
        mot2 = input('Veuillez ecrire la deuxieme ici')
        c = 0
        d = 0
        if len(mot1) == len(mot2):
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
            if c == d and c == len(mot2) and d == len(mot1):
                return True

        pass

    return False


def contains_doubles(items: list) -> bool:
    for i in range(len(items)):
        a = items[i]
        b = items.count(a)
        if b > 1:
            return True
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best = dict()
    for i in student_grades:
        c = 0
        d = 0
        a = student_grades[i]
        for q in range(len(a)):
            c += a[q]
        c = c / len(a)
        if len(best) == 0 or list(best.values())[0] < c:
            best = {i: c}

    return best


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    dictionnaire = dict()

    for lettre in range(len(sentence)):
        count = sentence.count(sentence[lettre])
        dictionnaire[sentence[lettre]] = count
    sorted_dic = sorted(dictionnaire.items(), key=lambda item: item[1], reverse=True) ## le reverce = True nous donne donne un ordre decroissant
    for item in sorted_dic:
        if item[1] > 5:
            print("le caractere ", item[0], " revient ", item[1], " fois.")
    return sorted_dic


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom = ""
    nombre = 0
    indice = "O"
    dictionnaire = {}
    dic_ingredients = {}
    while indice == "O":
        nom = input("Veuillez entre le nom de la recette ")
        nombre = int(input(" La recette est composé de combien d'ingredient ?"))
        for i in range(nombre):
            print(" Veuillez entrer le nom de la ", i + 1, "em ingredient")
            ingredient = input()
            print(" Veuillez entrer la qantité en gramme ")
            quantite = input()
            dic_ingredients[ingredient] = quantite
        dictionnaire[nom] = dic_ingredients
        indice = input(" Voulez vous ajouter une autre recette? O/N ")
        indice = indice.upper()
    return dictionnaire



def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input("Veuillez entrer le nom de la recette ")
    while nom not in ingredients:
        nom = input(" Le nom de la recette n'est pas dans la liste, veuillez entrer un nom valide. ")
    print(ingredients[nom])
    pass


def main() -> None:
    """
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    if anagrams():
        print('oui')
    else:
        print("non")


    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")


    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)"""


    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
