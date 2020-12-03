#On va recoder la notion de "puissance" en mathématiques avec une fonction récursive

def recursion_puissance(nb, puissance, i=0):
    if i < puissance - 1:
        nb = recursion_puissance(nb, puissance, i+1) * nb
    return nb

#Exemple : calcul de 2**5
#recursion_puissance(2, 5, i=0)
#   recursion_puissance(2, 5, i=1)
#       recursion_puissance(2, 5, i=2)
#           recursion_puissance(2, 5, i=3)
#               recursion_puissance(2, 5, i=4)
#               return 2
#           return 2 * 2
#       return 2 * 4
#   return 2 * 8
#return 2 * 16
