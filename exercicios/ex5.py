# Nesse exercício é demonstrado como criar strings que tem variáveis
# incorporadas.

# Para isso, usamos o caracter {} e também a letra "f". Ex:
# print(f"Exemplo de variávei incorporada {variável}")
# nesse caso precisados colcoar a letra "f" antes das aspas duplas
# para formatar a strings colocando o conteudo de determinada
# variável dentro das chaves.

my_name = 'Zed A. Shaw'
my_age = 35 # não é mentira
my_height = 74 # polegadas
my_weight = 180 # libras
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
# essa linha é capciosa, tente escrever exatamente como está
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
