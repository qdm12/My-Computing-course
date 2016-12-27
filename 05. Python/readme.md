# 5. Python

![Python][python_image]

## Final aim of this lesson
Write your own Python code to achieve something basic a business would want.

## Calculate your age in Python
1. In your host terminal and in your project, enter `touch mycode.py` to create the file *mycode.py* :new:
2. Open *mycode.py* with your code editor
3. Copy the following into it:
  ```python
  import time
  
  message = "Hello "
  name = "Denisa"
  print message + name
  
  #Your birthday date
  birthday_day = 2
  birthday_month = 12
  birthday_year = 1993
  
  #Gets the current date
  present_day = int(time.strftime("%d"))
  present_month = int(time.strftime("%m"))
  present_year = int(time.strftime("%Y"))
  #int() converts the 'text' (string) to an integer
  
  age = present_year - birthday_year
  age = age + float(present_month - birthday_month)/12
  #we use float otherwise 5/2 = 2 and not 2.5
  age += float(present_day - birthday_day)/365
  # += is a shortcut for age = age + ..
  print "You are " + str(age) + " years old :P"        
  ```
3. Launch your VM with `vagrant up`
4. Log into your VM with `vagrant ssh`
5. Go to the shared directory `cd /vagrant` in the guest terminal (VM)
6. Enter `python mycode.py` :wink:

## Perform an average on a list of numbers
1. Just switch to your code editor again, delete all the code
2. Don't close Vagrant :wink:
3. Now just copy and try to understand that code (we saw that in lesson 2):
  ```python
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
    # WE USE float() otherwise the division does not result 
    # in a floating number
    return average
    
  #Main code being run
  average1 = find_average([2,4,6]) #we call the find_average function !
  print "average1 = " + str(average1) #average1 is (2+4+6)/3 = 12/3 = 4
  average2 = find_average([1,3,5])
  print "average2 = " + str(average2) #average2 is (1+3+5)/3 = 9/3 = 3
  average3 = find_average([average1, average2])
  print "average3 = " + str(average3) #average3 is (3+4)/2 = 7/2 = 3.5
  ```
4. As before, go on your guest terminal (VM) and enter `python mycode.py`
- *Note*: You can try the **up** arrow which brings up your last command :wink:

## Write your code now
We now have a Christmas online shop, selling Chritmas trees, 
Christmas garden gnomes, Chritmas chocolates and Chritmas balls.
And we are quite popular, with thousands of sales just before Chritmas.
However, it's a mess in our numbers, we just keep a record of all 
transactions chronogically.

We therefore want to bring in some program to generate us to some useful 
information from that mess !

We will only focus on last Sunday, which has the following record of transactions:
- At 8:35AM, John bought 2 Chritmas trees and 1 Chritmas chocolates
- At 10:45AM, Mike bought 1 Chritmas trees and 12 Chritmas garden gnomes
- At 2:45PM, Mike bought 2 Chritmas gnomes
- At 3:10PM, Audrey bought 2 Chritmas garden gnomes and 3 Christmas balls
- At 6:00PM, John bought 1 Christmas balls

We also have the prices we have set for each of these items:
- Christmas tree is priced at $30
- Christmas garden gnome is priced at $7.50
- Christmas chocolates are priced at $12
- Christmas balls is priced at $1.75

Luckily, some software engineer who now left us already integrated that data in some Python code:
```python
class Transaction(object): #don't be scared
    def __init__(self, time, client, trees=0, gnomes=0, chocolates=0, balls=0):
		#0 by default for trees, gnomes, chocolates and balls
        self.time = time
        self.client = client
        self.trees = trees
        self.gnomes = gnomes
        self.chocolates = chocolates
        self.balls = balls

transactions = [] #'list' structure
t = Transaction("8:35AM", "John", trees=2, chocolates=1)
transactions.append(t)
t = Transaction("10:45AM", "Mike", trees=1, gnomes=12)
transactions.append(t)
t = Transaction("2:45PM", "Mike", gnomes=2)
transactions.append(t)
t = Transaction("3:10PM", "Audrey", gnomes=2, balls=3)
transactions.append(t)
t = Transaction("6:00PM", "John", balls=1)

prices = dict() #'dictionary' structure
prices["tree"] = 30
prices["gnome"] = 7.5
prices["chocolate"] = 12
prices["ball"] = 1.75
```

1. First, we want to find how much we have sold overall that last Sunday
  - Test the code above, understand how it works with `print`.
    - For example you can add `print prices` or `print transactions[2].client` at the end of the code
  - Then write a function following this format:
```python
def find_total_sales(transactions, prices):
    total_sales = 0
    # Fill this in
	# Use for loops (for element in elements_list: ...)
	# Advice:
	# 1. Accumulate the total number of trees bought Sunday
	# 2. Accumulate the total number of gnomes bought Sunday
	# 3. Accumulate the total number of chocolates bought Sunday
	# 4. Accumulate the total number of balls bought Sunday
	# 5. Multiply each number of X by its associated price
	# 6. Sum all the 4 multiplication results to get the total sale of Sunday
    #    PS: Multiply with this syntax c = 2*5
	return total_sales
```
  - If you can't make it, you can have a look at the file `mycode1.py` online.
2. The second task is to find percentages of each product as its total sale participation.
  - For example, if we sold 3 christmas trees @ $30 and have sold $150 overall, the Chritmas
    tree total sale participation is 100 * (3*$30)/$150 = 60%.
  - We want this information for the same Sunday as before.
```python
def find_participation(product_name, transactions, prices):
	total_sales = find_total_sales(transactions, prices)
	if product_name == "tree":
		# find total quantity sold, then multiply by price of a tree
		# Then do 100 * what you've found / total_sales
		# return that !
	elif product_name == "ball":
		#...
	# ...
```


  
[python_image]: /internals/icons/python.png