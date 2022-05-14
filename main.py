import cryptocode

nome_cliente = input("Escreva seu nome: ")
cpf_cliente = input("Escreva seu CPF: ")

opcao1 = input("Você deseja anonimar seus dados?\n [Y] Yes [N] No: ")

if opcao1.upper() == 'S':
    print ('\nSeus dados anonimados: ')

    nome_cliente_cript = cryptocode.encrypt(nome_cliente,"wow")
    cpf_cliente_cript = cryptocode.encrypt(cpf_cliente,"wow")

    print ("Nome:", nome_cliente_cript)
    print ("CPF:", cpf_cliente_cript)
    
    opcao2 = input("\nVocê deseja voltar seus dados?\n [Y] Yes [N] No: ")

    if opcao2.upper() == 'S':
        nome_cliente_decript = cryptocode.decrypt(nome_cliente_cript, "wow")
        cpf_cliente_decript = cryptocode.decrypt(cpf_cliente_cript, "wow")

        print ("\nNome:", nome_cliente_decript)
        print ("CPF:", cpf_cliente_decript)

    elif opcao1.upper() == 'N':
        print ('Não quis rever')

elif opcao1.upper() == 'N':
    print ('Não quis anonimizar')

