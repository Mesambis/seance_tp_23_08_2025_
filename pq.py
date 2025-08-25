#coding:utf-8
score=0
print("Q1: Qui est l'actuel Président du Bénin")
print("a-Patrice TOLON  b-Patrice TALON  c-Paul BIYA")
q1=input("Entrer la lettre correspondante => ")
if q1=="b":
    print("Bravo, +1")
    score=score + 1
else:
    print("Mauvaise réponse + 0")


print("Q2: La statue de l'amazone est dans quelle ville du Bénin?")
print("a-Ouidah  b-Porto-Novo  c-Cotonou")
q2=input("Entrer la lettre correspondante => ")
if q2=="c":
    print("Bravo, +1")
    score=score + 1
else:
    print("Mauvaise réponse + 0")


print("Q3: Le Bénin est sur quel continent?")
print("a-AFRIQUE  b-AMERIQUE  c-ASIE")
q3=input("Entrer la lettre correspondante => ")
if q3=="a":
    print("Bravo, +1")
    score=score + 1
else:
    print("Mauvaise réponse + 0")

print("le score final est:", score)