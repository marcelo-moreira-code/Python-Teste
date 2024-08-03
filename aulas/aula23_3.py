while True:
    user_action = input("Escreva um comando após a seta : \n"
                        "add - adicionar\n"
                        "mos - mostrar\n"
                        "edi - editar\n"
                        "apa - apagar\n"
                        "sai - sair\n-> ").strip()

    if user_action == "add":
        tarefa = input("Escreva a tarefa: ") + "\n"

        arquivo = open("tarefas.txt", "r")
        tarefas = arquivo.readlines()
        arquivo.close()

        tarefas.append(tarefa)

        arquivo = open("tarefas.txt", "w")
        arquivo.writelines(tarefas)
        arquivo.close()

    elif user_action == "mos":
        for index, tarefa in enumerate(tarefas):
            linha = f"{index + 1}-{tarefa}"
            print(linha)

    elif user_action == "edi":
        numero = int(input("Número da tarefa que queres editar: "))
        numero = numero - 1
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas[numero] = nova_tarefa

    elif user_action == "apa":
        numero = int(input("Número da tarefa a ser apagada: "))
        tarefas.pop(numero - 1)

    elif user_action == "sai":
        break

print("Até Logo!")
