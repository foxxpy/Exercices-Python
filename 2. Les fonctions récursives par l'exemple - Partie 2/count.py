#Recréer la méthode count d'une liste avec une fonction récursive
def recursion_count(liste, search, i=0):
    count = 0
    if i < len(liste):
        if liste[i] == search:
            count += 1
        count += recursion_count(liste, search, i+1)
    return count

#Exemple : on veut compter le nombre de fois que 1 est dans la liste ci-dessous
#recursion_count([1, 4, 1, 1, 3, 1, 7, 4, 9, 6, 7, 0], 1, i=0)
#   recursion_count([1, 4, 1, 1, 3, 1, 7, 4, 9, 6, 7, 0], 1, i=1)
#       recursion_count([1, 4, 1, 1, 3, 1, 7, 4, 9, 6, 7, 0], 1, i=2)
#           recursion_count([1, 4, 1, 1, 3, 1, 7, 4, 9, 6, 7, 0], 1, i=3)
#               recursion_count([1, 4, 1, 1, 3, 1, 7, 4, 9, 6, 7, 0], 1, i=4)
#                   recursion_count([1, 4, 1, 1, 3, 1, 7, 4, 9, 6, 7, 0], 1, i=5)
#                       recursion_count([1, 4, 1, 1, 3, 1, 7, 4, 9, 6, 7, 0], 1, i=6)
#                           recursion_count([1, 4, 1, 1, 3, 1, 7, 4, 9, 6, 7, 0], 1, i=7)
#                               recursion_count([1, 4, 1, 1, 3, 1, 7, 4, 9, 6, 7, 0], 1, i=8)
#                                   recursion_count([1, 4, 1, 1, 3, 1, 7, 4, 9, 6, 7, 0], 1, i=9)
#                                   return 0
#                               return 0 + 0
#                           return 0 + 0
#                       return 0 + 0
#                   return 0 + 0
#               return 1 + 0
#           return 0 + 1
#       return 1 + 1
#   return 0 + 2
#return 1 + 2
