n=int(input("Quantos termos?"))
a, b = 0, 1
k=1
while k <= n:
    print(a, end= "")
    a, b = b, a+b
    k=k+1
    