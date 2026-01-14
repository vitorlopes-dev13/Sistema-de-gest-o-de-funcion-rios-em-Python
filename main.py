from operacoes import (
    cadastrar_funcionario,
    listar_funcionarios,
    remover_funcionario,
    atualizar_salario,
    calcular_media,
    relatorio_resumo
)
from arquivo import carregar_funcionarios, salvar_funcionarios
def main():
    funcionarios = carregar_funcionarios()
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar funcionário")
        print("2 - Listar funcionários")
        print("3 - Atualizar salário")
        print("4 - Remover funcionário")
        print("5 - Média salarial")
        print("6 - Relatório geral")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_funcionario(funcionarios)
            salvar_funcionarios(funcionarios)
        elif opcao == "2":
            listar_funcionarios(funcionarios)
        elif opcao == "3":
            atualizar_salario(funcionarios)
            salvar_funcionarios(funcionarios)
        elif opcao == "4":
            remover_funcionario(funcionarios)
            salvar_funcionarios(funcionarios)
        elif opcao == "5":
            media = calcular_media(funcionarios)
            if media is None:
                print("Nenhum funcionário cadastrado.")
            else:
                print(f"Média salarial: R$ {media:.2f}")
        elif opcao == "6":
            print(relatorio_resumo(funcionarios))
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()
