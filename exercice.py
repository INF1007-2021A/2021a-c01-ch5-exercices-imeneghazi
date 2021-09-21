#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number = -number
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    List = []
    for i in range(len(prefixes)):
        List.append(prefixes[i] + suffixe)
    return List


def prime_integer_summation() -> int:
    c = 0
    n = 1
    s = 0
    while c != 100:
        n += 1
        for i in range(n-1, 0, -1):
            if n % i == 0:
                break
        if i == 1:
            c += 1
            s += n
    return s
    # Version du prof
    #prime = [2, 3, 5]
    #number = 6
    #while len(prime) < 100:
        #is_prime = True
        #for diviseur in range(2, number//2):
            #if number % diviseur == 0:
                #is_prime = False
                #break
        #if is_prime:
            #prime.append(number)
    #number += 1
    #return sum(prime)



def factorial(number: int) -> int:
    f = 1
    for i in range(2, number + 1):
        f *= i
    return f


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    #liste_a_supprimer = []
    liste_booleenne = [n*0 for n in groups]
    for i in range(len(groups)):
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 18
        if len(groups[i]) > 10 or len(groups[i]) <= 3:
            #liste_a_supprimer.append(groups[i])
            liste_booleenne[i] = False
        for j in range(len(groups[i])):
            if groups[i][j] == 25:
                temp3 = 25
                break
            elif groups[i][j] < 18:
                temp4 = groups[i][j]
            elif groups[i][j] > 70:
                temp1 = groups[i][j]
            elif groups[i][j] == 50:
                temp2 = 50
        if temp2 == 50 and temp1 > 70 and temp3 != 25:
            #liste_a_supprimer.append(groups[i])
            liste_booleenne[i] = False
        elif temp4 < 18 and temp3 != 25:
            liste_booleenne[i] = False
    #for element in liste_a_supprimer:
    #    groups.remove(element)
    for k in range(len(liste_booleenne)):
        if liste_booleenne[k] != False:
            liste_booleenne[k] = True
    #si on veut retourner la liste sans les groupes qui ont été refusé on return groups
    return liste_booleenne

    # Version du prof
    acceptance = []
    for group in groups:
        if len(group) > 10 or len(group) <= 3:
            acceptance.append(False)
            continue
        if 25 in group:
            acceptance.append(True)
            continue
        if (min(group) < 18) or (50 in group and max(group) > 70):
            acceptance.append(False)
            continue
        acceptance.append(True)
    return acceptance

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
