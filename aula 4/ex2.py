x = int(input("Digite um número:"))
y = int(input("Digite outro número:"))
z = int(input("Digite mais um número:"))

if (x!= y) and (x!= z) and (y!=z):
    if x > y and y > z:
        print(x, y, z)
        print ("teste1")
    elif x > z and z > y:
        print(x,z,y)
        print("teste 2")
    elif y > x and x > z:
        print (y,x,z)
        print("teste 3")
    elif y > z and z > x:
        print(y,z,x)
        print("teste 4")
    elif z > y and y > x:
        print (z,y,x)
        print("teste 5")
    elif z > x and x > y:
        print(z,x,y)
        print("teste 6")
else:
    print ("inválido, os números PRECISAM ser diferentes entre si!")