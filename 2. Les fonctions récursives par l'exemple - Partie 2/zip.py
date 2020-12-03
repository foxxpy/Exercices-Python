#Récréer la méthode zip() avec une fonction de récurrence
#Si les deux listes envoyées sont de longueurs différentes, la liste renvoyée aura la même longueur que la liste la plus petite

def recursion_zip(l1, l2, i=0):
    nb_iter = len(l1) if len(l1) <= len(l2) else len(l2)
    new_list = []

    if i < nb_iter:
        new_list = [(l1[i], l2[i])]
        new_list += recursion_zip(l1, l2, i+1)

    return new_list


#recursion_zip([1,3], [2,4,6,8], i=0)
#   recursion_zip([1,3], [2,4,6,8], i=1)
#       recursion_zip([1,3], [2,4,6,8], i=2)
#       return []
#   return [(3,4)] + []
#return [(1,2)]+[(3,4)]
#z = [(1,2), (3,4)]
