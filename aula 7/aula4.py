a = 5
def altera_valor ( x = 0):
    global a 
    a = x
   

print( a)
altera_valor (10) #variavel local
print (a)
altera_valor()
print (a)