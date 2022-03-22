# Formatação de strings de uma forma mais complexa
# Nesse exemplo, usamos algo chamado função para transformar a variável
# formatter  em outras strings. Quando aparecer formatter.format(...),
# é como se estivesse dizendo ao Python para fazer o seguinte:
# 1) Pegar a string formatter definida na linha 14.
# 2) Chamar sua função format, que é como pedir para executar um comando da
# linha de comando denominado format.
# 3) Passar quatro argumentos para format, que correspondem às quatro {}s na
# variável formatter. É como passar argumentos para o comando format da linha
# de comando.
# 4) O resultado de chamar format em formatter é uma nova string com as {}
# substituídas por quatro variáveis. Isso é o que o print imprime.

formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
