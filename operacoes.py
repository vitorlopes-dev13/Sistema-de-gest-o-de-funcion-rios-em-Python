from funcionario import Funcionario
def ler_salario():
    while True:
        try:
            salario = float(input("Digite o salário: "))
            if salario > 0:
                return salario
            print("O salário deve ser maior que zero.")
        except ValueError:
            print("Digite um valor válido.")
def cadastrar_funcionario(funcionarios):
    nome = input("Digite o nome: ")
    salario = ler_salario()
    funcionario = Funcionario(nome, salario)
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

def listar_funcionarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    for f in funcionarios:
        print(f"ID: {f.id} | {f.nome} | R$ {f.salario:.2f} | {f.situacao()}")
def remover_funcionario(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário para remover.")
        return
    listar_funcionarios(funcionarios)
    try:
        id_remover = int(input("Digite o ID do funcionário para remover: "))
        for f in funcionarios:
            if f.id == id_remover:
                funcionarios.remove(f)
                print("Funcionário removido com sucesso!")
                return
        print("ID não encontrado.")
    except ValueError:
        print("Digite um ID válido.")
def atualizar_salario(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    listar_funcionarios(funcionarios)
    try:
        id_func = int(input("Digite o ID do funcionário: "))
        for f in funcionarios:
            if f.id == id_func:
                novo_salario = ler_salario()
                f.salario = novo_salario
                print("Salário atualizado com sucesso!")
                return
        print("ID não encontrado.")
    except ValueError:
        print("Digite um valor válido.")
def calcular_media(funcionarios):
    if not funcionarios:
        return None
    return sum(f.salario for f in funcionarios) / len(funcionarios)
def relatorio_resumo(funcionarios):
    if not funcionarios:
        return "Nenhum funcionário cadastrado."
    media = calcular_media(funcionarios)
    acima = sum(1 for f in funcionarios if f.salario >= 3000)
    abaixo = len(funcionarios) - acima
    return (
        f"Total de funcionários: {len(funcionarios)}\n"
        f"Salários acima da média: {acima}\n"
        f"Salários abaixo da média: {abaixo}\n"
        f"Média salarial: R$ {media:.2f}"
    )
