def calcular_fibonacci(n):
    if n <= 0:
        return "O termo deve ser um número inteiro maior que zero."
    elif n == 1 or n == 2:
        return 1
    
    # Começamos com os dois primeiros termos da sequência
    a, b = 1, 1
    
    # Calculamos os próximos termos até chegar ao 'n' desejado
    for _ in range(3, n + 1):
        a, b = b, a + b
        
    return b

# Loop para o usuário poder interagir e fazer várias consultas
while True:
    entrada = input("Digite o número do termo que deseja descobrir (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break
        
    try:
        termo = int(entrada)
        resultado = calcular_fibonacci(termo)
        print(f"-> O {termo}º termo de Fibonacci é: {resultado}\n")
    except ValueError:
        print("-> Por favor, digite apenas números inteiros válidos.\n")