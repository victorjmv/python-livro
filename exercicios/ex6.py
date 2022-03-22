# Nesse exemplo é usado uma outra forma para formatar variáveis dentro
# de strings. No exemplo anterior foi usado : f"um texto qualqer{variável}".
# Nesse exemplo haverá também o uso da sintaxe .format()

types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said:'{y}'")
hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious))
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
