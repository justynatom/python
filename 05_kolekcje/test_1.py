phrase= "hello" #z.globalna

def greet(name):
    name.capitalize() #name z.lokalna
    print(phrase,name)

girl='elen'
greet(girl)
print("zmienna: ", phrase, girl, name)