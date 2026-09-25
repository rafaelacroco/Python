f = str(input("Digite sua faixa etária: "))

if f in ("Bebê", "bebê"):
    print("menor que 2 anos")
elif f in ('Criança' , 'criança'):
    print("de 3 a 10 anos")
elif f in ("Adulto", "adulto"):
    print("maior de 18 a 64 anos")
elif f in ('Idoso', 'idoso'):
    print("maior que 65 anos")

