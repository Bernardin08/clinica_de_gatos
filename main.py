#     Clinica de Gatos
from usuario import Usuario
from gato import Gato

def ler_dados():
    usuarios = []
    gatos = []

    try:
        with open('C:/Users/182400219/Documents/Projetos python/clinica_de_gatos/dados_usuarios.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('usuario:'):
                    user_data = line.split('usuario: ')[1]
                    usuarios.append(Usuario.from_string(user_data))
                elif line.startswith('gato:'):
                    cats_data = line.split('gato: ')[1]
                    gatos.append(Gato.from_string(cats_data))
    except FileNotFoundError:
        pass
    return usuarios, gatos

def gato_velho(list_gato_p):

    gato_mais_velho = list_gato_p[0]
    for gato in list_gato_p:
        if int(gato.idade) >= int(gato_mais_velho.idade):
            gato_mais_velho = gato
    print(gato_mais_velho)


def carregar_lista_gatos():
    list_g =[]
    with open('C:/Users/182400219/Documents/Projetos python/clinica_de_gatos/dados_usuarios.txt', 'r') as file:
        for line in file:
                line = line.strip()
                if line.startswith('Gato:'):
                    cats_data = line.split('Gato: ')[1]
                    nome = cats_data.split(",")[0]
                    idade = cats_data.split(",")[1]
                    cor = cats_data.split(",")[2]
                    raca = cats_data.split(",")[3]
                    gato_obj = Gato(nome,idade,cor,raca)
                    list_g.append(gato_obj)
    return list_g

def salvar_dados(usuarios,gatos):
    with open('C:/Users/182400219/Documents/Projetos python/clinica_de_gatos/dados_usuarios.txt', 'w') as file:
        for user in usuarios:
            file.write(f'usuario: {user}\n')
        for cats in gatos:
            file.write(f'Gato: {cats}\n')
            
def login(usuarios):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    for user in usuarios:
        if user.nome == nome and user.senha == senha:
            return True
    return False

def cadastrar_gatos(gatos):
    nome = input("Qual é o nome do seu gato? ")
    idade = input("Qual é a idade do seu gato? ")
    cor = input("Qual é a cor do seu gato? ")
    raca = input("Qual é a raça do seu gato? ")
    gatos.append(Gato(nome, idade, cor, raca))

def main():

    usuarios, gatos = ler_dados()
    
    if not login(usuarios):
        print("Usuário ou senha incorretos.")
        return
    
    print("Login realizado com sucesso!")

    while True:
        print("\n1. Ver Gatos Cadastrados\n2. Cadastrar Gato\n3. Ver Gato Mais Velho\n4. Sair")
        opcao = input("Escolha uma opção: ")
             
        if opcao == '1':
            for gato in gatos:
                print("Gatos:  ",gato)
        elif opcao == '2':
            cadastrar_gatos(gatos)
            salvar_dados(usuarios, gatos)
        elif opcao == '3':
            print("Este é o gato mais velho")
            list_gato = carregar_lista_gatos()
            gato_velho(list_gato)

        elif opcao == '4':
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida.")
main()


#list_gato = carregar_lista_gatos()



