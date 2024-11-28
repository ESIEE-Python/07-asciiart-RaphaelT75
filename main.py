#### Imports et définition des variables globales


#### Fonctions secondaires
"""
Ce fichier utilise deux algorithmes pour encoder une chaîne de 
caractères, pour cela il fait appel à 2 fonctions artcode_i(itteratif)
et artcode_r(récursif)
"""
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
    en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1

    result.append((current_char, count))
    return result

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    if not s:
        return []

    caracteres = [s[0]]
    occurences = [1]
    n = len(s)

    for k in range(1, n):
        if s[k] == s[k - 1]:
            occurences[-1] += 1
        else:
            caracteres.append(s[k])
            occurences.append(1)

    return list(zip(caracteres, occurences))

#### Fonction principale

def main():
    """
    méthode main teste le programme en faisant des appels des fonctions secondaires
    """
    print(artcode_i(' '))
    print(artcode_i('MMaMM'))
    print(artcode_r('MMaMM'))
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
