#lab 4 ex1
a = str(input("Primeira palavra: "))
b = str(input("Segunda palavra: "))
c = str(input("Terceira palavra: "))

if a == "vertebrado" or b == "vertebrado" or c == "vertebrado":
    if a == "mamifero" or b == "mamifero" or c == "mamifero":
        if a == "herbivoro" or b == "herbivoro" or c == "herbivoro":
                print ("Vaca") #SAÍDA
        if a == "onivoro" or b == "onivoro" or c == "onivoro":
                print ("Homem") #SAÍDA
    if a == "ave" or b == "ave" or c == "ave":
            if a == "carnivoro" or b == "carnivoro" or c == "carnivoro":
                    print ("águia")
            if a == "onivoro" or b == "onivoro" or c == "onivoro":
                    print ("Pomba") #SAÍDA
elif a == "invertebrado" or b == "invertebrado" or c == "invertebrado":
    if a == "inseto" or b == "inseto" or c == "inseto":
        if a == "hematofago" or b == "hematofago" or c == "hematofago":
                print ("Pulga") #SAÍDA
        if a == "herbivoro" or b == "herbivoro" or c == "herbivoro":
                print ("Largata") #SAÍDA
    if a == "anelideo" or b == "anelideo" or c == "anelideo":
            if a == "hematofago" or b == "hematofago" or c == "hematofago":
                    print ("Sanguessuga") #SAÍDA
            if a == "onivoro" or b == "onivoro" or c == "onivoro":
                    print ("Minhoca") #SAÍDA  
else:
    print ("Informações insuficientes para identificar um animal")