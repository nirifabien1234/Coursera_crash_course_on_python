# name = "Fabien"
# number = len(name) * 3
# print("Hello {}, your lucky number is {}".format(name, number))

# def student_grade(name, grade):
#     	return "{name} received {grade}% on the exam".format(name=name, grade=grade)

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))

# DEALING WITH DECIMAL PLACES WITH STINGS
price = 7.5
with_tax = 1.09
print(price, with_tax)

print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))