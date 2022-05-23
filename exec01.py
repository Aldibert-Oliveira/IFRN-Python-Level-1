lista_pessoas = []
idade_media = 0

pessoa = input('Digite nome, idade:  ')
nome,idade = pessoa.split(',')
lista_pessoas.append({'nome': nome, 'idade': int(idade)})
idade_media += int(idade)

pessoa = input('Digite nome, idade:  ')
nome,idade = pessoa.split(',')
lista_pessoas.append({'nome': nome, 'idade': int(idade)})
idade_media += int(idade)

pessoa = input('Digite nome, idade:  ')
nome,idade = pessoa.split(',')
lista_pessoas.append({'nome': nome, 'idade': int(idade)})
idade_media += int(idade)

quant_pessoas = len(lista_pessoas)
print(f'{quant_pessoas} cadastradas')
print(f'idade média: {idade_media}')
