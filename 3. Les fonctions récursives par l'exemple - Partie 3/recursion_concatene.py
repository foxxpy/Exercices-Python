#Concaténer deux chaînes de caractères

def recursion_concatene(string1, string2, i=0, j=0):
    new_string = ""
    if i < len(string1):
        new_string += string1[i]
        new_string += recursion_concatene(string1, string2, i+1, j)
    
    elif j < len(string2):
        new_string += string2[j]
        new_string += recursion_concatene(string1, string2, i, j+1)

    return new_string

#Concaténation de "Foxx" et "py"
#recursion_concatene("Foxx", "py", i=0, j=0)
#   recursion_concatene("Foxx", "py", i=1, j=0)
#       recursion_concatene("Foxx", "py", i=2, j=0)
#           recursion_concatene("Foxx", "py", i=3, j=0)
#               recursion_concatene("Foxx", "py", i=4, j=0)
#                   recursion_concatene("Foxx", "py", i=4, j=1)
#                       recursion_concatene("Foxx", "py", i=4, j=2)
#                       return ""
#                   return "y"
#               return "p"+"y"
#           return "x"+"py"
#       return "x"+"xpy"
#   return "o" + "xxpy"
#return "F"+"oxxpy"
