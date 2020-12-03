#Inverser une chaîne de caractères grâce à la récursion : reproduction de l'écriture string[::-1]

def recursion_inversion_string(s):
    """Inversion d'une chaîne de caractères par la récursion"""
    new_s = s[-1]
    if len(s) > 1:
        new_s += recursion_inversion_string(s[0:-1])
    return new_s

#Exemple en inversant la chaîne de caractères : "Foxxpy"
#recursion_inversion_string("Foxxpy")
#   recursion_inversion_string("Foxxp")
#       recursion_inversion_string("Foxx")
#           recursion_inversion_string("Fox")
#               recursion_inversion_string("Fo")
#                   recursion_inversion_string("F")
#                   new_s = "F"
#               new_s = "o"+"F" = "oF"
#           new_s = "x" + "oF" = "xoF"
#       new_s = "x" + "xoF" = "xxoF"
#   new_s = "p" + "xxoF" = "poxxF"
#new_s = "y" + "pxxoF" = "ypxxoF"

