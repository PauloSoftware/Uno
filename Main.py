#liste des flag pour pas en avoir 2 les memes : flag1 flag2 flag3 flag4 flag5 flag6
from random import *
liste_cartes = []
pioche = []
couleur = 0
periode = "pioche"
flag2=0
n=0
liste_totale = []
tas = []
liste_joueurs=[]
flag5= 0
playtimes=0
def lancer ():
    n_joueurs=int(input("combien de joueurs"))
    flag5= 0
    while n_joueurs>flag5 :
        nompartiel=input("nom")
        liste_totale.append([[nompartiel],[]])
        flag5+=1
def placement_possible (ID_joueur,ID_carte):
    if (tas[0][0]==liste_totale[ID_joueur][1][ID_carte][0]) or (tas[0][1]==liste_totale[ID_joueur][1][ID_carte][1]) or (liste_totale[ID_joueur][1][ID_carte][1]=="noir"):
        return True
    else :
        return False
def clean (b):
    a = 0
    while a<b :
        print (" ")
        a+=1
def piocher (ID , n):
    flag3 = 0
    while flag3 < n :
        liste_totale[ID][1].append(pioche[0])
        del pioche[0]
        flag3+=1

def voir_main (ID):
    useless = input ("appuyez pour voir vos cartes")
    flag4 = 0
    while flag4<len(liste_totale[ID][1]) :
        print (flag4 ,"-->", liste_totale[ID][1][flag4][0], liste_totale[ID][1][flag4][1])
        flag4 +=1
def jouer (ID , index) :
    if placement_possible(ID_joueur,ID_carte) :
        del tas[0]
        tas.append (liste_totale[ID_joueur][1][ID_carte])
        del liste_totale[ID_joueur][1][ID_carte]
    else :
        print ("placement impossible")
        return False
def periscope ():
    flag6 = 0
    while flag6<len(liste_totale) :
        print (str(liste_totale[flag6][0][0])+"-->"+ str(len(liste_totale[flag6][1])))
        flag6+=1
liste_couleurs = ["bleu","rouge","vert","jaune"]
while couleur!=4 :
    #le 0 n'est présent qu'une fois par couleur, on va l'insérer
    liste_cartes.append ([0,liste_couleurs[(couleur)]])
    rounde = 0
    #beaucoup de cartes sont présentes en 2 exemplaires, je vais donc doubler ma methode de rajout
    while rounde <2 :
        numero = 1
        while numero <10 :
            liste_cartes.append ([(numero) , liste_couleurs[(couleur)]])
            numero=numero+1
        #on va rajouter les cartes semi spéciales (1 par round donc 2)
        #d'abord les cartes +2 nomées p2
        liste_cartes.append (["plus 2" , liste_couleurs[(couleur)]])
        #puis les passe tour nomées "pt"
        liste_cartes.append (["passe ton tour" , liste_couleurs[(couleur)]])
        #enfin les change de sens nomées "cs"
        liste_cartes.append (["change de sens" , liste_couleurs[(couleur)]])
        rounde+=1
    #les cartes +4 et couleurs sont présente à raison de 4 chaqu'une, soit un par couleur
    #on va rajouter 4 cartes +4 nomées "p4"
    liste_cartes.append (["plus 4" , "noir"])
    #puis les jokers només "jk"
    liste_cartes.append (["jk" , "noir"])
    couleur+=1
while len(liste_cartes)>1 :
    flag=randint(1 , (len(liste_cartes)-1))
    pioche.append(liste_cartes[flag])
    del liste_cartes[flag]

#while not (main1==0)and (main2==0):
    
