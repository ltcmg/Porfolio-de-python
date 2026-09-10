alunos = {
    "Ana": 8.5,
    "Carlos": 6.0,
    "João": 9.0,
    "Maria": 5.5
}
for nome, nota in alunos.items():
    if nota >=8:
          print (f"{nome}-Aprovado")

    else: 
          print(f"{nome}- Reprovados")