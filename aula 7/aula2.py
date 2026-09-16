import time
def cronometro (segundos_total, segundos_intervalo):
    for i in range (2, segundos_total+1, segundos_intervalo ):
        time.sleep (segundos_intervalo)
        print (i)

cronometro (10,2)