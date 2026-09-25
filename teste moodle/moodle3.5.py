h = int(input("Digite a hora inicial: "))
m = int(input("Digite o minuto inicial: "))
hf = int(input("Digite a hora final: "))
mf = int(input("Digite o minuto final: "))

x = h * 60
y = hf * 60

mini = m + x
minf = mf + y

if minf <= mini:
    minf += 1440
mt = minf - mini
if mt >= 1 and mt <= 1440:
    ht = mt // 60  # Duas barras pegam a hora inteira 
    mr = mt % 60   # O sinal de % pega o resto da divisão
    print (f"O jogo durou {ht} hora(s) e {mr} minuto(s)")
