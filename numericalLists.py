def counting():
	for number in range(1,5):
		print(number)

counting()		

def ListOfNumbers():
	numbers = list(range(1,5))
	return numbers

print("a list of numbers: ", ListOfNumbers())	

def evenNumbers():
	even_numbers = list(range(2,11,2)) #start at 2, go up to 10, add 2 each time
	return even_numbers

print("a list of even numbers: ", evenNumbers())	

def squares():
	squares_list = []
	for value in range(1,11):
		squares_list.append(value**2)
	return squares_list

print("a list of squares: ", squares())		

nums = [1,2,3,4,5,6,7,8,9,10,-1]
print(nums)
print("minimum is = ", min(nums))
print("maximum is = ", max(nums))
print("summation is = ", sum(nums))

#using a list comprehension 
adding_three = [v+3 for v in range(1,11)]
print(adding_three)
# general format is: 
# name_of_list = [(expression) (for loop)]