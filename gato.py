class Gato:
    def __init__(self, nome, idade, cor, raca):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca
    
    def __repr__(self):
        return f"{self.nome},{self.idade},{self.cor},{self.raca}"
    
    def from_string(gato_str):
        nome, idade, cor, raca = gato_str.split(",")
        return Gato("Nome :",nome,"Idade",idade,"Cor",cor,"Raça",raca)

