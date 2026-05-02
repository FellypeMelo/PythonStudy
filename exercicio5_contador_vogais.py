# Exercício 5: Contador de Vogais
# Objetivo: Combinar repetição (for) e condicionais

def contador_vogais():
    """
    Pede ao usuário uma frase qualquer e conta quantas vogais 
    (a, e, i, o, u) existem nela.
    """
    # Recebendo a frase do usuário
    frase = input("Digite uma frase: ")
    
    # Definindo as vogais (maiúsculas e minúsculas)
    vogais = "aeiouAEIOU"
    
    # Contando as vogais
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    
    # Exibindo o resultado
    print(f"A frase possui {contador} vogal{'is' if contador != 1 else ''}.")


if __name__ == "__main__":
    contador_vogais()
