# 5. Python

![Python][python_image]

## Final aim of this lesson
Write your own Python code to achieve something basic a business would want.

## Calculate your age in Python
1. In your host terminal, enter `touch mycode.py` to create :new: the file *mycode.py*
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
    average = float(sum) / numbers_list.length
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

We also have the prices of each of these items:
- Christmas tree is priced at $30
- Christmas garden gnome is priced at $7.50
- Christmas chocolates are priced at $12
- Christmas balls is priced at $1.75

Luckily, some software engineer who now left us already integrated that data in Python:
```python
class Transaction(object): #don't be scared
    def __init__(self, time, client, trees=0, gnomes=0, chocolates=0, balls=0):
        self.time = time
        self.client = client
        self.trees = trees
        self.gnomes = gnomes
        self.chocolates = chocolates
        self.balls = balls
        
    def __repr__(self):
        #This is used to print the Transaction 'object'
        return "At "+str(time)+" minutes, "+client+" bought "+ \
                str(trees)+" trees, "+str(gnomes)+" gnomes, "+ \
                str(chocolates)+" chocolates and "+str(balls)+" balls"

transactions = [] #'list' structure
t = Transaction(8*60 + 35, "John", trees=2, chocolates=1)
transactions.append(t)
t = Transaction(10*60 + 45, "Mike", trees=1, gnomes=12)
transactions.append(t)
t = Transaction(14*60 + 45, "Mike", gnomes=2)
transactions.append(t)
t = Transaction(15*60 + 10, "Audrey", gnomes=2, balls=3)
transactions.append(t)
t = Transaction(18*60 + 0, "John", balls=1)

prices = dict() #'dictionary' structure
prices["tree"] = 30
prices["gnome"] = 7.5
prices["chocolate"] = 12
prices["ball"] = 1.75

print "Prices: ", prices
print "First transaction: ", transactions[0]
print "Second transaction: ", transactions[1]
print "Last transaction: ", transactions[len(transactions)]
```

- Now we need to find how much we have sold for last Sunday.
- Test the code above, understand how it works with `print`.
- Then write a function following this format:
```python
def find_total_sales(transactions, prices):
    total_sales = 0
    # Fill this in. Use for loops !
    # Advice: Accumulate the total number of trees and so on and then multiply by the price.
    # Multiply like c = 2*5
```



  
[python_image]: /internals/icons/python.png