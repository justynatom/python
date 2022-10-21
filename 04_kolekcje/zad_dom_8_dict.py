austria=["Anna","Marie","Sophie","Emilia","Elena","Lena","Emma","Lea","Mia","Sarah"]
belgia=["Olivia","Emma","Mila","Louise","Lina","Alice","Sofia","Mia","Anna","Julia"]
wielka_Brytania=["Olivia","Amelia",	"Isla","Ava","Ivy","Florence","Lily","Freya","Mia",	"Willow"]
estonia=["Mia","Sofia","Emily","Hanna","Nora","Emma","Eva","Alice","Marta",	"Lena"]
francja=["Louise","Alma","Emma","Adele", "Chloe","Anna","Olivia","Eva", "Gabrielle","Alice"]
malta=["Julia",	"Elena","Emma",	"Elizabeth","Mia","Emily","Catherine","Lea","Valentina","Sophia"]
szkocja=["Olivia","Emily","Isla","Freya","Ella","Amelia","Ava","Sophia","Grace","Millie"]
polska=["Susanna","Sophia","Hannah","Julia","Maja","Laura","Olivia","Alice","Lena","Pola"]
serbia=["Mia","Emma","Mila","Lara","Lina", "Sophia","Hannah","Anna","Lea","Natalie"]
hiszpania=["Lucía","Martina","Sophía","María","Valeria","Julia","Paula","Emma",	"Daniela","Carla"]

lista=austria+belgia+wielka_Brytania+estonia+francja+malta+szkocja+polska+serbia+hiszpania
print(lista)
imiona_3_kraje=[]
for i in lista:
    if lista.count(i)>=3:
        imiona_3_kraje.append(i)

set(imiona_3_kraje)
print(set(imiona_3_kraje))
