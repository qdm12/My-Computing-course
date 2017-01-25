def find_average(numbers_list):
	""" Returns the average of a list of numbers
	
		Sums all the numbers of the list and then divides 
		the sum by the length of the list to obtain the average.
		
	Args:
		numbers_list (list): A list of numbers.
	
	Returns:
		average (int): The resulting average of the list of numbers
	"""
	# Checks the input is a list
	if type(numbers_list) is not list:
		raise Exception("numbers_list has to be a list")
	
	# Checks the first element of the list is an integer or floating 
	# point number
	first_number = numbers_list[0]
	if type(first_number) is not int and type(first_number) is not float:
		raise Exception("numbers_list has to contain numbers (integer or floating point)")
	
	# Sums all the numbers
	sum = 0
	for number in numbers_list:
		sum = sum + number # can also be sum += number
	print sum # to check the code is working ;)
	
	# Divides the sum by the number of numbers
	average = float(sum) / numbers_list.length
	# WE USE float() otherwise the division does not result 
	# in a floating number
	
	# When the function is called, it "returns" the average
	# Example: x = find_average([2,4,7])
	return average
    
if __name__ == "__main__":
    numbers = [1,3,5,7,10]
    average = find_average(numbers)
    print "Average of "+str(numbers)+" is "+str(average)