class Funcionario:
    contador_id = 1
    def __init__(self, nome, salario):
        self.id = Funcionario.contador_id
        Funcionario.contador_id += 1
        self.nome = nome
        self.salario = salario
    def situacao(self, limite=3000):
        return "Acima da média" if self.salario >= limite else "Abaixo da média"
