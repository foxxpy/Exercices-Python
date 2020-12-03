#Retrouver le maximum d'une liste de nombre

def recursion_max(liste, i=0, max_liste=0):

    if i < len(liste):
        if i == 0 or liste[i] > max_liste:
            max_liste = liste[i]
        max_liste = recursion_max(liste, i+1, max_liste)
    return max_liste

#recursion_max([0,2,-1,5,1,1,8,0], i=0, max_liste=0)
#   recursion_max([0,2,-1,5,1,1,8,0], i=1, max_liste=0)
#       recursion_max([0,2,-1,5,1,1,8,0], i=2, max_liste=2)
#           recursion_max([0,2,-1,5,1,1,8,0], i=3, max_liste=2)
#               recursion_max([0,2,-1,5,1,1,8,0], i=4, max_liste=5)
#                   recursion_max([0,2,-1,5,1,1,8,0], i=5, max_liste=5)
#                       recursion_max([0,2,-1,5,1,1,8,0], i=6, max_liste=5)
#                           recursion_max([0,2,-1,5,1,1,8,0], i=7, max_liste=8)
#                               recursion_max([0,2,-1,5,1,1,8,0], i=8, max_liste=8)
#                               return 8
#                           return 8
#                       return 8
#                   return 8
#               return 8
#           return 8
#       return 8
#   return 8
#return 8
