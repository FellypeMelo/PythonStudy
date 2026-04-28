# Exercício 3: Gerador de E-mails Corporativos
# Objetivo: Praticar manipulação de strings e listas

def gerador_emails_corporativos():
    """
    Percorre uma lista com nomes de funcionários e gera um e-mail 
    para cada um no formato nome.sobrenome@empresa.com (tudo em minúsculas).
    """
    # Lista de funcionários definida no código
    funcionarios = ['Ana Silva', 'Bruno Costa', 'Carla Souza']
    
    # Nova lista para armazenar os e-mails gerados
    emails = []
    
    # Percorrendo a lista de funcionários
    for nome in funcionarios:
        # Convertendo para minúsculas e trocando espaço por ponto
        email = nome.lower().replace(" ", ".") + "@empresa.com"
        emails.append(email)
    
    # Exibindo a lista de e-mails gerados
    print(emails)


if __name__ == "__main__":
    gerador_emails_corporativos()
