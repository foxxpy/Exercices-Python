#Calculer la valeur factorielle d'un nombre n. n étant un entier positif
def recursion_factorielle(n):
    if n > 2:
        n *= recursion_factorielle(n-1)
    return n

#Factorielle
# 2! = 2
# 3! = 3 * 2
# 4! = 4 * 3 * 2
# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2

#Exemple pour n = 5
#recursion_factorielle(5)
#   recursion_factorielle(4)
#       recursion_factorielle(3)
#           recursion_factorielle(2)
#           return 2
#       n = 3 * 2 = 6 => return 6
#   n = 4 * 6 = 24 => return 24
#n = 5 * 24 = 120 => return 120

