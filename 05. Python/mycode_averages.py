#The following defines a 'function' to perform an average on multiple numbers
#A 'function' is great because we can re-use as shown at the bottom of the code
#The function is not ran except if it is "called" (below)
def find_average(numbers_list):
    # Sums all the numbers
    sum = 0
    for number in numbers_list:
        sum += number
    # Divides the sum by the number of numbers
    average = float(sum) / len(numbers_list)
    # WE USE float() otherwise the division does not result in a floating number
    return average

#Main code being run
average1 = find_average([2,4,6]) #we call the find_average function !
print "average1 = " + str(average1) #average1 is (2+4+6)/3 = 12/3 = 4

average2 = find_average([1,3,5])
print "average2 = " + str(average2) #average2 is (1+3+5)/3 = 9/3 = 3

average3 = find_average([average1, average2])
print "average3 = " + str(average3) #average3 is (3+4)/2 = 7/2 = 3.5