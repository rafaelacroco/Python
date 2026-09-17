#variaveis locais (altera dentro da função return)
a = 5
def altera_valor ():
    #global a pega o a fora da função
    a = 7
    print("a dentro da função =", a) 

print("a antes da função =", a)
altera_valor () #variavel local
print ("a depois da função =", a)

