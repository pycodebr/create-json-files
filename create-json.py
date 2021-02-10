import json

# Dados que irão virar json #
# Podem ser listas, dicionários ou tuplas #
dados = {
    'nome': 'Pycodebr',
    'instagram': '@pycodebr',
    'linguagem': 'python',
    'conteudos': [
        {'conteudo': 'Codigos'},
        {'conteudo': 'Curiosidades'}
    ]
}

# Cria o arquivo json no caminho especificado abaixo #
with open(r'.\dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)