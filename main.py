from logging.config import listen


def tailleList(liste,n):
    ret = []
    for mot in liste:
        if len(mot) == n+1:
            ret.append(mot)
    return ret

def motWith(liste, index, letter):
    ret = []
    index -=1
    for mot in liste:
        if mot[index] == letter:
            ret.append(mot)
    return ret

def motWithOut(liste, letter):
    ret = []
    for mot in liste:
        if letter not in mot:
            ret.append(mot)
    return ret

def motWithTwo(liste, letter):
    ret = []
    for mot in liste:
        if letter in mot:
            ret.append(mot)
    return ret

if __name__=="__main__":
    liste = []
    with open('./liste_francais.txt','r') as f:
        for line in f:
            liste.append(line)
    
    taille = int(input("Taille du mot : "))
    ret = tailleList(liste,taille)
    print(len(ret))

    while(True):

        nbtours = int(input("Nombre de lettres connues + position : "))
        for i in range(nbtours):
            char = str(input("Lettre connue : "))
            pos = int(input("Position de la lettre : "))
            ret = motWith(ret, pos, char)
            print(len(ret))
            print("_________________")


        nbtours = int(input("Nombre de lettres connues mais sans position :"))
        for i in range(nbtours):
            char = str(input("Lettre connue :"))
            ret = motWithTwo(ret, char)
            print(len(ret))
            print("___________________")
        
        nbtours = int(input("Nombre de lettres connues qui ne sont pas dans le mot :"))
        for i in range(nbtours):
            char = str(input("Lettre connue qui n'est pas dans le mot :"))
            ret = motWithOut(ret, char)
            print(len(ret))
            print("___________________")

        print("Proposition possibles : ")
        for mot in ret:
            print(mot)
     
   
    