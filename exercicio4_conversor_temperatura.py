# Exercício 4: Conversor de Temperatura com Função
# Objetivo: Praticar a criação e chamada de funções

def celsius_para_fahrenheit(celsius):
    """
    Converte um valor em Celsius para Fahrenheit.
    Fórmula: F = (C * 9/5) + 32
    """
    return (celsius * 9/5) + 32


def programa_principal():
    """
    Programa principal que pede a temperatura ao usuário 
    e usa a função de conversão.
    """
    # Recebendo a temperatura em Celsius
    celsius = float(input("Digite a temperatura em °C: "))
    
    # Convertendo para Fahrenheit
    fahrenheit = celsius_para_fahrenheit(celsius)
    
    # Exibindo o resultado
    print(f"{fahrenheit:.1f}°F")


if __name__ == "__main__":
    programa_principal()
