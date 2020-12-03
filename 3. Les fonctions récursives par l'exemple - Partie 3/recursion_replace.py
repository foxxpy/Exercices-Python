#On va recoder la fonction replace() d'une chaîne de caractères

def recursion_replace(string, to_replace, replacement, i =0):
    new_string = ""
    if i < len(string):
        if string[i] == to_replace:
            new_string += replacement
        else:
            new_string += string[i]

        new_string += recursion_replace(string, to_replace, replacement, i+1)

    return new_string


#Remplacer un 1 par rien
#recursion_replace("F1o1x1x1p1y1", "1", "", i=0)
#   recursion_replace("F1o1x1x1p1y1", "1", "", i=1)
#       recursion_replace("F1o1x1x1p1y1", "1", "", i=2)
#           recursion_replace("F1o1x1x1p1y1", "1", "", i=3)
#               recursion_replace("F1o1x1x1p1y1", "1", "", i=4)
#                   recursion_replace("F1o1x1x1p1y1", "1", "", i=5)
#                       recursion_replace("F1o1x1x1p1y1", "1", "", i=6)
#                           recursion_replace("F1o1x1x1p1y1", "1", "", i=7)
#                               recursion_replace("F1o1x1x1p1y1", "1", "", i=8)
#                                   recursion_replace("F1o1x1x1p1y1", "1", "", i=9)
#                                       recursion_replace("F1o1x1x1p1y1", "1", "", i=10)
#                                           recursion_replace("F1o1x1x1p1y1", "1", "", i=11)
#                                               recursion_replace("F1o1x1x1p1y1", "1", "", i=12)
#                                               return ""
#                                           return "" + ""
#                                       return "y"+""
#                                   return ""+"y"
#                               return "p"+"y"
#                           return ""+"py"
#                       return "x"+"py"
#                   return ""+"xpy"
#               return "x"+"xpy"
#           return ""+"xxpy"
#       return "o"+"xxpy"
#   return ""+"oxxpy"
#return "F"+"oxxpy"
