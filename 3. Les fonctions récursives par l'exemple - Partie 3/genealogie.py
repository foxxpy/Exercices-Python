#Afficher l'arbre généalogique d'une famille

class Person:
    def __init__(self, name, child, parent):
        self.name = name
        self.child = child
        self.parent = parent
        self.generation = 0

    def about_me(self):
        print("--- Génération "+str(self.generation)+" ---")
        print("Je suis "+self.name+".")

        if not self.child is None:
            print("J'ai "+str(len(self.child))+" enfants : ", end="")
            for c in self.child:
                print(c+" - ", end="")
            print(".")
        else:
            print("Je n'ai pas d'enfant.")

        if not self.parent is None:
            print("Mon parent est : "+str(self.parent))
        else:
            print("Mon parent est inconnu")

tree = {
    "Elizabeth" : Person("Elizabeth", ["Arthur", "Charles"], None),
    "Arthur" : Person("Arthur", ["Edouard", "Georges"], "Elizabeth"),
    "Charles" : Person("Charles", ["Lucie"], "Elizabeth"),
    "Edouard" : Person("Edouard", ["Henry", "Carl"], "Arthur"),
    "Georges" : Person("Georges", ["Antoine"], "Arthur"),
    "Lucie" : Person("Lucie", ["Catherine", "Emma"], "Charles"),
    "Henry" : Person("Henry", ["Georges II"], "Edouard"),
    "Carl" : Person("Carl", None, "Edouard"),
    "Antoine" : Person("Antoine", None, "Georges"),
    "Catherine" : Person("Catherine", None, "Lucie"),
    "Emma" : Person("Emma", ["Carl II"], "Lucie"),
    "Georges II" : Person("Georges II", None, "Henry"),
    "Carl II" : Person("Carl II", ["Carl III", "Karl"], "Emma"),
    "Carl III" : Person("Carl III", None, "Carl II"),
    "Karl" : Person("Carl III", None, "Carl III")
}

def recursion_genealogie(tree, person_name, generation=1):
    tree[person_name].generation = generation
    tree[person_name].about_me()
    if not tree[person_name].child is None:
        for child in tree[person_name].child:
            recursion_genealogie(tree, child, generation+1)
    return

start_tree = "Elizabeth"
recursion_genealogie(tree, start_tree)