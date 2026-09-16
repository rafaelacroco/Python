def soma (x,y):
    return x + y


def par (x):
    if x % 2 == 0:
        print(f"{x} é par")
        return True
    else:
        print (f"{x} não é par")
        return False

x = int (input("digite um valor:"))
par (x)
y = int (input("digite um segundo  valor:"))
par (y)
