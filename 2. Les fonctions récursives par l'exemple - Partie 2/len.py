#On va recréer la fonction len() avec une méthode récursive

def recursion_len(string, i=0):
    if string != "":
        i = recursion_len(string[1:], i+1)
    return i

#On veut la longueur de la chaîne de caractères "Foxxpy"
#recursion_len("Foxxpy", i=0)
#   recursion_len("oxxpy", i=1)
#       recursion_len("xxpy", i=2)
#           recursion_len("xpy", i=3)
#               recursion_len("py", i=4)
#                   recursion_len("y", i=5)
#                       recursion_len("", i=6)
#                       return 6
#                   return 6
#               return 6
#           return 6
#       return 6
#   return 6
#return 6
