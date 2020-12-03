#Recréer une multiplication grâce à la récursion

def recursion_multiplication(n1, n2, i=1):
    """Multiplie le nombre n1 par n2 en utilisant la récursion"""

    if i < n2:
        n1 = recursion_multiplication(n1, n2, i=i+1) + n1
    return n1

#Exemple avec la multiplication de : 3 * 5
#recursion_multiplication(3, 5, 1):
#   recursion_multiplication(3, 5, 2)
#       recursion_multiplication(3, 5, 3)
#           recursion_multiplication(3, 5, 4)
#               recursion multiplication(3, 5, 5)
#               n1 = 3
#           n1 = 3 + 3 = 6
#       n1 = 6 + 3 = 9
#   n1 = 9 + 3 = 12
#n1 = 12 + 3 = 15
