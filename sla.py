import json

# Bem vindos a lista de contatos do Luis
print("Bem vindos à lista de contatos de [Luis vinicius correa farias]")

# EXIGÊNCIA DE CÓDIGO 2 de 8
lista_contatos = []
id_global = 1

# Função para carregar os contatos do arquivo
def carregar_contatos():
    global lista_contatos, id_global
    try:
        # Abre o arquivo 'contatos.json' com o encoding especificado
        with open('contatos.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            lista_contatos = dados['contatos']
            id_global = dados['id_global']
    except FileNotFoundError:
        # Se o arquivo não existir, inicializa uma lista vazia e id_global com 1
        lista_contatos = []
        id_global = 1
    except json.JSONDecodeError:
        # Se o arquivo não for um JSON válido, exibe uma mensagem de erro
        print("Erro ao decodificar o arquivo JSON. O arquivo pode estar corrompido ou mal formatado.")
    except Exception as e:
        # Para outros erros genéricos, imprima uma mensagem
        print(f"Ocorreu um erro inesperado: {e}")

# Função para salvar os contatos no arquivo
def salvar_contatos():
    with open('contatos.json', 'w', encoding='utf-8') as f:
        dados = {'contatos': lista_contatos, 'id_global': id_global}
        json.dump(dados, f, ensure_ascii=False, indent=4)

# EXIGÊNCIA DE CÓDIGO 3 de 8
def cadastrar_contato():
    global id_global
    id = int(input("Digite o id: "))
    nome = input("Digite o nome do contato: ")
    atividade = input("Digite a atividade do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contato = {"id": id, "nome": nome, "atividade": atividade, "telefone": telefone}
    lista_contatos.append(contato)
    id_global += 1  # Incrementa id_global para o próximo contato
    salvar_contatos()  # Salva os contatos após o cadastro

# EXIGÊNCIA DE CÓDIGO 4 de 8
def consultar_contatos():
    while True:
        opcao = input("1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Atividade\n4. Retornar ao menu\nEscolha uma opção: ")
        if opcao == '1':
            for contato in lista_contatos:
                print(contato)
        elif opcao == '2':
            try:
                id_consulta = int(input("Digite o id do contato: "))
            except ValueError:
                print("Por favor, insira um número válido")
            else:
                encontrado = False
                for contato in lista_contatos:
                    if contato['id'] == id_consulta:
                        print(contato)
                        encontrado = True
                        break
                if not encontrado:
                    print("Contato não encontrado.")
        elif opcao == '3':
            atividade_consulta = input("Digite a atividade: ")
            for contato in lista_contatos:
                if contato['atividade'] == atividade_consulta:
                    print(contato)
        elif opcao == '4':
            return
        else:
            print("Opção inválida.")

def remover_contato():
    id_remover = int(input("Digite o id do contato a ser removido: "))
    for i, contato in enumerate(lista_contatos):
        if contato['id'] == id_remover:
            del lista_contatos[i]
            print("Contato removido com sucesso.")
            salvar_contatos()  # Salva os contatos após a remoção
            return
    print("Id inválido.")
# EXIGÊNCIA DE CÓDIGO 6 de 8
while True:
  opcao = input("1. Cadastrar Contato\n2. Consultar Contato\n3. Remover Contato\n4. Encerrar Programa\nEscolha uma opção: ")
  if opcao == '1':
        cadastrar_contato()
  elif opcao == '2':
        consultar_contatos()
  elif opcao == '3':
        remover_contato()
  elif opcao == '4':
        break
  else:
        print("Opção inválida.")
