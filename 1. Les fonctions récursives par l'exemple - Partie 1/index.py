#Renvoyer le premier index de l'élément que l'on recherche dans une liste : équivalent de la méthode index d'un objet list()
def recursion_index(liste, element, i=0):
    
    if i < len(liste):
        if liste[i] == element:
            return i
        else:
            i = recursion_index(liste, element, i=i+1)
        return i
    else:
        return None

#Exemple en recherchant "x" dans la chaîne "Foxxpy"
#recursion_index(["F", "o", "x", "x", "p", "y"], "x", i=0)
#   recursion_index(["F", "o", "x", "x", "p", "y"], "x", i=1)
#       recursion_index(["F", "o", "x", "x", "p", "y"], "x", i=2)
#       return 2
#   return 2
#return 2

#Exemple en recherchant le "h" dans la chaîne "Foxxpy"
#recursion_index(["F", "o", "x", "x", "p", "y"], "h", i=0)
#   recursion_index(["F", "o", "x", "x", "p", "y"], "h", i=1)
#       recursion_index(["F", "o", "x", "x", "p", "y"], "h", i=2)
#           recursion_index(["F", "o", "x", "x", "p", "y"], "h", i=3)
#               recursion_index(["F", "o", "x", "x", "p", "y"], "h", i=4)
#                   recursion_index(["F", "o", "x", "x", "p", "y"], "h", i=5)
#                       recursion_index(["F", "o", "x", "x", "p", "y"], "h", i=6)
#                       return None
#                   return None
#               return None
#           return None
#       return None
#   return None
#return None
