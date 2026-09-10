alunos = {
    "Ana": 8.5,
    "Carlos": 6.0,
    "João": 9.0,
    "Maria": 5.5
}
for nome, nota in alunos.items():
    if nota>= 7:
        print(f"Alunos aprovado {nome}-{nota}")
    else:
        print(f"Alunos reprovados {nome}-{nota}")