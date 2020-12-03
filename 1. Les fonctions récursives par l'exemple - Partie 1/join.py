#Recréer la fonction join() des chaînes de caractères avec un algorithme récursif

def recursion_join(c, liste, i=0):
    final_string = str(liste[i])+c if i < len(liste)-1 else str(liste[i])
    if i < len(liste)-1:
        final_string += recursion_join(c, liste, i+1)
    return final_string

#recursion_join("-", ["1", "2", "3", "4", "5", "6"], i=0)
#   recursion_join("-", ["1", "2", "3", "4", "5", "6"], i=1)
#       recursion_join("-", ["1", "2", "3", "4", "5", "6"], i=2)
#           recursion_join("-", ["1", "2", "3", "4", "5", "6"], i=3)
#               recursion_join("-", ["1", "2", "3", "4", "5", "6"], i=4)
#                   recursion_join("-", ["1", "2", "3", "4", "5", "6"], i=5)
#                   return "6"
#               return "5-"+"6"
#           return "4-"+"5-6"
#       return "3-"+"4-5-6"
#   return "2-"+"3-4-5-6"
#return "1-"+"2-3-4-5-6"
