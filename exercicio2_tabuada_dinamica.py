# Exercício 2: Tabuada Dinâmica
# Objetivo: Demonstrar domínio sobre a estrutura de repetição for

def tabuada_dinamica():
    """
    Solicita ao usuário um número inteiro e exibe a tabuada 
    desse número de 10 a 1 (ordem decrescente).
    """
    # Recebendo o número inteiro
    numero = int(input("Digite um número inteiro: "))
    
    # Exibindo a tabuada em ordem decrescente
    for i in range(10, 0, -1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


if __name__ == "__main__":
    tabuada_dinamica()
