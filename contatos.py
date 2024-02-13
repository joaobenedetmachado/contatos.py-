contatos = {}

while True:
    escolha = input(''' 
adicionar um contato: pressione 1
listar contatos: pressione 2
excluir um contato: pressione 3
sair: digite 'sair'
        
''')

    if escolha == '1': 
        nome = input('nome: ')
        numeroemail = input('numero/email: ')
        contatos[len(contatos) + 1] = {'nome': nome, 'numero/email': numeroemail}
    
    elif escolha == '2':
        print('lista de contatos:')
        for contato_id, info_contato in contatos.items():
            print(f'ID: {contato_id} | nome: {info_contato["nome"]} | numero/email: {info_contato["numero/email"]}')
        
    elif escolha == '3':
        excluir = int(input("qual o ID do contato que deseja excluir?"))
        if excluir in contatos:
            print(f'usuario ID {excluir}: {contatos[excluir]} sera excluido')
            del contatos[excluir]
        else:
            print(f'ID {excluir} nao encontrado')
    
    elif escolha == 'sair':
        break
