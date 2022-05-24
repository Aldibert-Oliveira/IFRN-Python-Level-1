lista_pessoas = []
idade_media = 0

for _ in range(0,3):
    pessoa = input('Digite nome, idade:  ')
    nome,idade = pessoa.split(',')
    lista_pessoas.append({'nome': nome, 'idade': int(idade)})
    idade_media += int(idade)
quant_pessoas = len(lista_pessoas)
idade_media = idade_media /quant_pessoas
print(f'{quant_pessoas} cadastradas')
print(f'idade média: {idade_media}')

