# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
name = "Jonathan"         
age = 30               
languages = ["Python", "JavaScript", "HTML", "CSS", "SQL"] 
is_studying = True  

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
letters_string = name[0:3]

# Exercise 3: Use an index to grab the first element from your list. 
first_element = languages[0]

# Exercise 4: Create a new number variable that adds 10 to your original number. 
new_age = age + 10

# Exercise 5: Use an index to get the last element in your list. 
last_element = languages[-1]


# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
list_of_names = names.split(',')

#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

my_string = "hello world"
first_space_index = my_string.find(" ")
new_string = my_string[:first_space_index].upper() + my_string[first_space_index:]

#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
sentence = f"Yo tengo {age} años."

# Exercise 9: Print “hello world”
print("hello world")


#Extra: Cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".

my_string = "Hola mundo"
new_string = my_string.replace("Hola", "adiós")