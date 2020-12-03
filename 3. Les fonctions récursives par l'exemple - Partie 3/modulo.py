#Fonction récursive qui reproduit le comportement du modulo (%)

def recursion_modulo(nb1, nb2):
    if nb1 >= nb2:
        nb1 = recursion_modulo(nb1-nb2, nb2)
    return nb1

#Exemple : 17 % 3
#recursion_modulo(17, 3)
#   recursion_modulo(14, 3)
#       recursion_modulo(11, 3)
#           recursion_modulo(8, 3)
#               recursion_modulo(5, 3)
#                   recursion_modulo(2, 3)
#                   return 2
#               return 2
#           return 2
#       return 2
#   return 2
#return 2
