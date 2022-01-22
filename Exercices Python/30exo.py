# 1) saisire le nom avec bienvenue 
# 2) ab et la somme de ab 
# 3) saisir ab affichier le max 


# print("entrer votre nom")
# nom=input()

# print(f"Bienvenue! {nom}")
# print("Bienvenue!",nom)



# print("entrer a")
# a=input()
# print("entrer b")
# b=input()
# somme=int(a)+int(b)
# print("la somme de a et b est ",somme)


# print("entrer un nbr")
# nbr=int(input())
# for i in range(nbr):
#     print("hello")


# print("entrer une phrase")
# str=input()
# if 'a' or 'u' or 'o' or 'i' or 'e' or 'y' in str:
#     print("le mot contient au moins une voyelle")
# else:
#     print("y a pas de voyelle")

#EX 1:

#print ('saisir votre nom: '),
#n = input()
#print ('Bienvenue', n)


#EX 2 :

#nb1 = input('Entrez un nombre: ')
#nb2 = input('Entrez un nombre: ')

#s = int(nb1) + int(nb2)

#print('La somme de {0} et  {1} est {2}'.format(nb1, nb2, s))


#EX 3 :

#a = int(input("Tapez la valeur du nombre a : "))
#b = int(input("Tapez la valeur du nombre b : "))

#if (a > b):
#    print("Le maximum  de a et de b est : a = ", a)
#else:
#    print("Le maximum  de a et de b est : b = ", b)


#EX 4 :

#for i in range(0,101):
#    print(i)


#EX 5:

#n = int(input("saisir un nombre  n : "))



#if(n%2 == 0):
#    print("Le nombre '", n, "'  est pair ")
#else:
#    print("Le nombre '", n, "'  est impair ")


#EX 6:

#age = int(input("saisir votre age : "))
#if(age > 18):print("tu es un majeur ")else:print("tu es un mineur ")


#EX 7:

#x = int(input("saisir un nombre x "))
#y = int(input("saisir un nombre y "))
#z = int(input("saisir un nombre z "))

#max = 0

#if(x > y):
#    max = x
#else:
#    max = y
#if(max < z):
#    max = z
#else:
#    max = max
#print("Le maximum :  ", max)


# EX8:
# somme=0
# nbr = int(input("entrer un nbr"))
# for i in range(nbr+1):
#     somme=somme+i

# print(somme)


#EX 9:

#n = int(input(" n :"))

#j = 1
#for i in range(1, n+1):
#    j = ji
#print("Factorielle de n est : ", n," = : ", j)



#EX 10:
#import math

#r = int(input("entrer le rayon"))
#S=math.piint(r)**2
#P=2math.pir
#print(f"la surface est : {S} \n le perimetre est {P}")


#EX 11:

#n = int(input(" n : "))

#for i in range(1, n+1):

#    if(n%i==0):
#        print(" ",i," est diviseur de ",n)



#EX 12:

# nbr = int(input("entrer un nbr"))
# multiple=0
# for i in range(10):
#     multiple=nbr*i
#     print(multiple)



#EX 13:

#a = int(input("a:"))
#b = int(input("b:"))
#q = a/b
#r = a%b
#print("Le quotient : q = ", q)
#print("Le reste : r = ", r)



#EX 14:

#n = int(input("n :  "))

#j = 0
#for i in range(0,n):
#    if(i**2 == n):
#        j = j +1
#if(j > 0):
#    print("", n, " est un carré parfait")
#else:
#    print("", n, " n'est pas est un carré parfait")



#EX 15:

#n = int(input("n :  "))
#j = 0
#for i in range(1, n+1):
#    if(n%i == 0):
#        j = j + 1

#if( j == 2):
#    print("", n , " est premier")
#else:
#    print("", n , " n'est pas premier")

# #EX12 16% 39min
# nbr = int(input("entrer un nbr"))
# multiple=0
# for i in range(10):
#     multiple=nbr*i
#     print(multiple)



# #EX16
# str = str(input("entrer une phrase"))
# for i in str:
#     print(i)

#EX17
# str = str(input("entrer une phrase : \n"))
# freq=0
# for i in str:
#     print(f"le caractere {i} figure {str.count(i)} dans la chaine S")
    
#EX18
# str = str(input("entrer une phrase : \n"))
# print(f"le lettre a se trouve dans la position:{str.find('a')}")    

#EX19

# l=["laptop","iphone","tablet"]

# for i in l:
#     print(f"la chaine {i} has a lenght of {len(i)}")

#EX20
# s=str(input("entrer une chaine"))
# n = len(s)
# p = s[0]
# d = s[n-1]
# ss = s[1:n-1]
# sss = d + s1 + p
# print(sss)


#EX20
# s=str(input("entrer une chiane"))
# n = len(s)
# p = s[0]
# d = s[n-1]
# ss = s[1:n-1]
# sss = d + s1 + p
# print(sss)


#EX 21:

#voyelles= {'a','e','y','u','i','o'}

#s = "anticonstitutionellement"

#n = len(s)

#nb_voyelles = 0
#for i in range(0,n):
#    if(s[i] in voyelles):
#        nb_voyelles = nb_voyelles + 1
#print("Le nombre de voyelles de 's' est : ", nb_voyelles)


#EX 22:

#s = "Sohaib weld l97ba"

#prmot = ""
#i = 0

#while (s[i] != " "):
#    prmot = prmot + s[i]
#    i = i + 1
#print("Le premier mot de ", s," est  : ", s[:i])



#EX 23:

#fichier = input("fichier : ")
#L = fichier.split(".")
#extensionFichier = "."+ L[-1]
#print("L'extension du fichier est : ", extensionFichier)



#EX 24:

#mot = input("Saisir un mot : ")
#inverse = mot[::-1]
#if(mot == inverse):
#    print("Le mot :", mot," est un palindrome")
#else:
#    print("Le mot : ", mot, " n'est pas un palindrome")

#EX 25
# c = input("Tapez une chaine c : ")
# c1 = c[::-1]
# print("L'inverse de ",c," est : ", c1)

#EX26
# s = input("Entrer un text : ")
# s = s.split()
# for x in s:
#     if(x[0] == 'a'):
#         print("Le mot : ", x, " commence par la lettre 'a'")

#EX27
# l=[1,5,6]
# multi=0
# somme=0
# for i in l:
#     print(i)
#     multi=i*i
#     somme=i+i
# print(f"la multiplkication est {multi} \n la somme et {somme}")


#EX 28:

#l = list()
#if l== [3, 5]:
#    print ("La liste est vide")
#else:
#    print ("La liste n'est pas vide")

#s = "er"

#if s == "":
#    print ("La chaîne est vide")
#else:
#    print ("La chaine n'est pas vide")

#EX29
# l=[1,5,6,5]
# print("la liste avant la suppression",l)
# l = list(dict.fromkeys(l))
# print("la liste apres la suppression",l)

#EX 30:

#def EC(l1,l2):.
#    compteur = 0
#    for x in l1:
#        if x in l2:
#            compteur =compteur + 1
#    if compteur != 0:
#        return True
#    else:
#        return False

#l1 = [1,3,52,8,21]
#l2 = [2,4,5,9,17]
#print(EC(l1,l2))


# def function(l):
#     max=0
#     for i in l:
#         if(i>i+1):
#             max=i
# print(max)            

# print(function([1,2,5,6]))


# L1=[5,6,4,3]
# L2=['A','B','C','N','V']

# for index, char in zip (L1,L2):
#     print(index,char)



