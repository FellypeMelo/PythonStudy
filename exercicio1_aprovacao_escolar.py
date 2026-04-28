# Exercício 1: Sistema de Aprovação Escolar
# Objetivo: Praticar estruturas condicionais simples

def sistema_aprovacao_escolar():
    """
    Recebe quatro notas de um aluno, calcula a média aritmética 
    e informa se ele foi aprovado, está em recuperação ou reprovado.
    """
    # Recebendo as quatro notas
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    
    # Calculando a média aritmética
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    # Determinando a situação do aluno
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    # Exibindo o resultado
    print(f"Média: {media:.1f} - {situacao}")


if __name__ == "__main__":
    sistema_aprovacao_escolar()
