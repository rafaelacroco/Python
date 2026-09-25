h = int(input("Digite a hora inicial: "))
m = int(input("Digite o minuto inicial: "))
hf = int(input("Digite a hora final: "))
mf = int(input("Digite o minuto final: "))

x = h * 60
y = hf * 60

# Transforma tudo em minutos
mini = m + x
minf = mf + y

# Se a hora final for menor ou igual à inicial, soma 24h (1440 minutos)
if minf <= mini:
    minf += 1440

mt = minf - mini

# Agora o limite máximo é 1440 minutos (24 horas)
if mt >= 1 and mt <= 1440:
    ht = mt // 60  # Duas barras pegam a hora inteira (ex: 2)
    mr = mt % 60   # O sinal de % pega o resto da divisão (os minutos que sobraram)
    print (f"O jogo durou {ht} hora(s) e {mr} minuto(s)")