from funcionario import Funcionario
def salvar_funcionarios(funcionarios, nome_arquivo="funcionarios.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for f in funcionarios:
            arquivo.write(f"{f.id},{f.nome},{f.salario}\n")
def carregar_funcionarios(nome_arquivo="funcionarios.txt"):
    funcionarios = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                id_f, nome, salario = linha.strip().split(",")
                funcionario = Funcionario(nome, float(salario))
                funcionario.id = int(id_f)
                funcionarios.append(funcionario)
        if funcionarios:
            Funcionario.contador_id = max(f.id for f in funcionarios) + 1
    except FileNotFoundError:
        pass
    return funcionarios
