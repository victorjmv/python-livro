tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# Sequência de escape que o Python suporta:


#   ESCAPE      O QUE FAZ
#   \\          Barra invertida (\))
#   \'          Aspas simples(')
#   \"          Aspas duplas (")
#   \a          Campainha ASCII (BEL)
#   \b          Retorno ASCII (BS)
#   \f          Avanço de página ASCII (FF)
#   \n          Nova linha ASCII (LF)
#   \N{name}    Caractere name no banco de dados Unicode (Unicode apenas)
#   \r          Retorno de carro (CR)
#   \t          Tabulação horizontal (TAB)
#   \uxxxx      Caractere com valor hex de 16 bits xxxx
#   \Uxxxxxxxx  Caractere com valor hex de 32 bits xxxxxxxx
#   \v          Tabulação vertical ASCII (VT)
#   \ooo        Caractere com valor octal ooo
#   \xhh        Caractere com valor hex
#
#
#
#
#
#
#
