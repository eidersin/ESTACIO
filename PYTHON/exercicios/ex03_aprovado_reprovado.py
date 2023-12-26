nota = eval(input('Digite a nota: '))
if nota >= 7:
    situacao = 'aprovado'
elif nota >= 5:
    situacao = 'em recuperação'
else:
    situacao = 'reprovado'
print(f'O estudante está: {situacao}')
