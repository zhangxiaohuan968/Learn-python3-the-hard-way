types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x) # There are 10 types of people.
print(y) # Those who know binary and those who don't.

print(f"I said: {x}") # I said: There are 10 types of people.
print(f"I also said: '{y}'") # I also said: 'Those who know binary and those who don't.'

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) # Isn't that joke so funny?! False

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e) # This is the left side of ...a string with a right side.
