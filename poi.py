#coding:utf-8
x=int(input("Entrer un nombre entier"))
if x%2==1 and x < 0:
    print("Il s'agit d/'/ impair negatif")
elif x%2==1 and x > 0:
    print("Ce nombre est impair et positif")
if x%2==0 and x<0:
    print("Ce nombre est pair et negatif")
elif x%2==0 and x > 0:
    print("nombre pair et postif")
    
