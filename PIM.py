import json
import os
from statistics import mean, median, mode

ARQUIVO = "alunos.json"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar_alunos(alunos):
    with open(ARQUIVO, "w") as f:
        json.dump(alunos, f, indent=4)

def carregar_alunos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return {}

def validar_ra(ra):
    return ra.isdigit() and len(ra) == 9

def adicionar_aluno(alunos):
    limpar_tela()
    print("=== Adicionar Aluno ===")
    ra = input("Digite o RA (9 dígitos numéricos): ")
    if not validar_ra(ra):
        print("RA inválido. Deve conter exatamente 9 dígitos numéricos.")
        input("Pressione Enter para continuar...")
        return

    if ra in alunos:
        print("Já existe um aluno com esse RA.")
        input("Pressione Enter para continuar...")
        return

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    genero = input("Gênero: ")
    nota = float(input("Nota (0 a 10): "))

    alunos[ra] = {
        "nome": nome,
        "idade": idade,
        "genero": genero,
        "nota": nota
    }

    salvar_alunos(alunos)
    print("Aluno adicionado com sucesso!")
    input("Pressione Enter para continuar...")

def remover_aluno(alunos):
    limpar_tela()
    print("=== Remover Aluno ===")
    ra = input("Digite o RA do aluno a remover: ")
    if ra in alunos:
        del alunos[ra]
        salvar_alunos(alunos)
        print("Aluno removido com sucesso!")
    else:
        print("RA não encontrado.")
    input("Pressione Enter para continuar...")

def listar_alunos(alunos):
    limpar_tela()
    print("=== Lista de Alunos ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for ra, dados in alunos.items():
            status = "Aprovado ✅" if dados["nota"] >= 5 else "Reprovado ❌"
            print(f"RA: {ra} | Nome: {dados['nome']} | Idade: {dados['idade']} | Gênero: {dados['genero']} | Nota: {dados['nota']} | {status}")
    input("Pressione Enter para continuar...")

def mostrar_estatisticas(alunos):
    limpar_tela()
    print("=== Estatísticas ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        input("Pressione Enter para continuar...")
        return

    idades = [dados["idade"] for dados in alunos.values()]
    notas = [dados["nota"] for dados in alunos.values()]

    try:
        moda_idade = mode(idades)
    except:
        moda_idade = "Sem moda"

    try:
        moda_nota = mode(notas)
    except:
        moda_nota = "Sem moda"

    print(f"Média de idade: {mean(idades):.2f}")
    print(f"Moda de idade: {moda_idade}")
    print(f"Mediana de idade: {median(idades):.2f}")
    print()
    print(f"Média das notas: {mean(notas):.2f}")
    print(f"Moda das notas: {moda_nota}")
    print(f"Mediana das notas: {median(notas):.2f}")

    print("\n=== Situação dos Alunos ===")
    for ra, dados in alunos.items():
        status = "Aprovado ✅" if dados["nota"] >= 5 else "Reprovado ❌"
        print(f"{dados['nome']} - Nota: {dados['nota']} → {status}")
    input("\nPressione Enter para continuar...")

def alterar_aluno(alunos):
    limpar_tela()
    print("=== Alterar Cadastro do Aluno ===")
    ra = input("Digite o RA do aluno que deseja alterar: ")
    
    if ra not in alunos:
        print("RA não encontrado.")
        input("Pressione Enter para continuar...")
        return

    print(f"Dados atuais: {alunos[ra]}")
    nome = input("Novo nome (pressione Enter para manter o atual): ")
    idade = input("Nova idade (pressione Enter para manter o atual): ")
    genero = input("Novo gênero (pressione Enter para manter o atual): ")
    nota = input("Nova nota (pressione Enter para manter a atual): ")

    if nome:
        alunos[ra]["nome"] = nome
    if idade:
        alunos[ra]["idade"] = int(idade)
    if genero:
        alunos[ra]["genero"] = genero
    if nota:
        alunos[ra]["nota"] = float(nota)

    salvar_alunos(alunos)
    print("Cadastro do aluno atualizado com sucesso!")
    input("Pressione Enter para continuar...")

def menu():
    alunos = carregar_alunos()
    while True:
        limpar_tela()
        print("="*40)
        print("📘  SISTEMA DE GESTÃO DE ALUNOS")
        print("="*40)
        print("1️⃣  Adicionar aluno")
        print("2️⃣  Remover aluno")
        print("3️⃣  Listar alunos")
        print("4️⃣  Mostrar estatísticas")
        print("5️⃣  Sair")
        print("6️⃣  Alterar cadastro do aluno")
        print("="*40)

        opcao = input("Escolha uma opção (1-6): ")

        if opcao == "1":
            adicionar_aluno(alunos)
        elif opcao == "2":
            remover_aluno(alunos)
        elif opcao == "3":
            listar_alunos(alunos)
        elif opcao == "4":
            mostrar_estatisticas(alunos)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        elif opcao == "6":
            alterar_aluno(alunos)
        else:
            print("Opção inválida. Pressione Enter para tentar novamente.")
            input()

if __name__ == "__main__":
    menu()
