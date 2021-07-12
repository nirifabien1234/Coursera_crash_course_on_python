# name = "Fabien"
# number = len(name) * 3
# print("Hello {}, your lucky number is {}".format(name, number))

# def student_grade(name, grade):
#     	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))

# DEALING WITH DECIMAL PLACES WITH STINGS
# price = 7.5
# with_tax = 1.09
# print(price, with_tax)

# print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

# message = "Fabien is the Fabien best programmer in the world"
# message = message.replace(message.split()[0], "Fab")
# print(message)

def get_word(sentence, n):
    	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n - 1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing