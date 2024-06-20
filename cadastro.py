print("Cadastro do seu Gato!! ")
nome = input("Qual é o nome do seu gato? ")
idade = input("Qual é a idade do seu gato? ")
cor = input("Qual é a cor do seu gato? ")
raca = input("Qual é a raça do seu gato? ")

def salvar_dados(nome, idade, cor, raca):
    with open('clinica_de_gatos/dados_gatos.txt', 'w') as file:
       
        file.write(f'nome: {nome}\n')
        
        file.write(f'idade: {idade}\n')

        file.write(f'cor: {cor}\n')

        file.write(f'raça: {raca}\n')
salvar_dados(nome,idade,cor,raca)