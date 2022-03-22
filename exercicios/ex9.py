# Aqui temos uma coisa nova estranha, lembre-se de digitá-la exatamente

# Nesse exemplo é usado dois modos para se estender strings para várias
# linhas. No primeiro modo, foi usado os caracteres \n entre os nomes
# dos meses. Esses caracteres insereem um caracter de nova linha na string,
# nesse ponto.

# O caracter \ codifica os caracteres difíceis de digitar em uma string.
# Usado como escape.

# O segundo modo é usando aspas triplas, que são apenas """ e funcionam
# como uma string, mas você também pode colocar quantas linhas de texto
# desejar até digitar """ de novo.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days:", days)
print("Here are the months:", months)
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
