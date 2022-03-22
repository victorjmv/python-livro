# Na linha 19 temos o que é chamado de import. É como você adiciona
# módulos ao script a partir do conjunto de recursos do Python.

# Segundo a documentação do Python o módulo sys "fornece acesso a algumas
# variáveis usadas ou mantidas pelo interpretador e a funções que interagem
# fortemente com o interpretador."

# argv é a lista de argumentos de linha de comando passadas para o
# script Python.

# A linha 21 descompacta argv, ao invés de conter todos os argumentos.
# Ele é atribuído às quatro variáveis com as quais você pode trabalhar:
# script, first, second e third. Pode parecer estranho, mas "descompactar"
# provavelmente é a melhor palavras para descrever o que ele faz. Significa:
# "Pegue qualquer coisa em argv, descompacte e atribua a todas essas variáveis
# à esquerda em ordem."


from sys import argv

script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
