# 5. Python

[![Python][python_image]][python_link]

## Final aim of this lesson
Write your own Python code to achieve something basic a business would want.

## Calculate your age in Python
1. In your host terminal and in your project, enter `touch mycode.py` to create the file *mycode.py* :new:
2. Open *mycode.py* with `atom mycode.py`
3. Copy the following into it:
   ```python
   from datetime import datetime
   
   name = raw_input("Hello ! Please enter your name: ")
   birth_date = raw_input("Enter your birth date in the format dd/mm/yyyy: ")
   
   print
   print "Hello "+name+"! I'm calculating your age, 1 second..."
   today_object = datetime.today()
   today_year = today_object.year
   today_month = today_object.month
   today_day = today_object.day
   
   birth_year = int(birth_date[6:10])
   birth_month = int(birth_date[3:5])
   birth_day = int(birth_date[0:2])
   #int() converts the 'text' (string) to an integer
   
   age_year = today_year - birth_year
   age_month = today_month - birth_month
   age_day = today_day - birth_day
   
   age_float = age_year + float(age_month)/12 + float(age_day)/365
   #float() converts to a floating point number. It is necesary to floating point divisions !
   print "You are "+str(age_float)+" years old"
   #str() converts to 'text' (string)
   ```
3. Launch your VM with `vagrant up` :rocket:
4. Log into your VM with `vagrant ssh` :unlock:
5. Go to the shared directory `cd /vagrant` in the guest terminal (VM) :file_folder:
6. Enter `python mycode.py` :snake: and play with it

## Perform an average on a list of numbers
1. Just switch to *Atom* again, delete all the code
2. Don't shutdown Vagrant :wink:
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
     # WE USE float() otherwise the division does not result in a floating number
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
- *Note*: You can try the **up** arrow :arrow_up: which brings up your last command :wink:

## How to write your code

### Setting up Liclipse and Python

Although you can write code in any code editor *"blindly"* :see_no_evil:, 
it is better to see what syntax errors :x: or what possibilities you have while writing code.

Unfortunately, Vagrant/Pydev/Python/BunchOfOtherThings are stupid on something called *remote debugging*
except if you spend $200 on a program called *Pycharm* but we're **cheap** so we will go a harder way...

1. Install [**Python 2.7**][python_link] on your computer.
2. Install [**Liclipse**][liclipse_link] on your computer.
3. Launch Liclipse, choose **Liclipse dark theme** :black_large_square:,
   then choose a workplace as it prompts for it (and tick :ballot_box_with_check:
   the *always use this workplace* box)
4. In Liclipse, on the top right, click on **File**, **New**, **Pydev project** :new:
	1. For the project name, enter *first-project* then click on **Finish**
	2. It will prompt you to configure a Python *interpreter*, just click on **Quick auto-config**
	3. In your workplace, you now have a directory *first-project* with nothing in it; but Python :snake: is ready !

### Add what you've done to *Liclipse*'s project
To add what we've done in the previous [Github lesson 4][lesson_04]:
- Nerdy way, with your terminal :computer: :
	- Modify and enter `cp -fr /home/username/lesson_04/first-project/* /home/username/workplace/first-project/`
- Normal way, with your file explorer:
	1. Go to your *first-project* directory you have cloned in lesson 4 with **git** :open_file_folder:
	2. Select all the files **including** the **.git** sub-directory (which contain all the git & github information)
	3. Copy them and paste them into the *first-project* directory created in the Liclipse workspace directory.

### Create the Python file (or *module*) mycode.py
- Option 1: In your terminal, `cd` to the Liclipse's *first-project* directory and enter `touch mycode.py`
- Option 2: In Liclipse, click on **File**, **New**, **Pydev Module**, enter *mycode.py* in the name field and click on **Finish** :new:
- Option 3: In your file explorer, create a file named *mycode.py* :page_with_curl:

### Test out the installation Liclipse + Python
1. Open *mycode.py* in Liclipse from the left directory pane (click on *first-project*)
2. Write `print "Hello"` in *mycode.py* :dolphin:
3. Run the code by pressing on the *Play* button :arrow_forward: on the top or by pressing your **F9** key. 
  *Note that you can still run that code with `python mycode.py` in your terminal or in Vagrant as before.*
4. You should see *Hello* in the Liclipse bottom pane console.

### Liclipse and errors
1. Syntax and obvious errors you make :x:
    - Change `"Hello"` to `x` for example and save the code (TIP: use **CMD**+**S** or **CTRL**+**S**)
	- A *red cross* on the line and a red underlining the `x` will appear
	- Hover over the *red cross* or the `x` and it will say **Undefined variable: x**
	- Indeed, the variable `x` does not exist, so just add `x = "Hello"` above that line and save; errors will disappear :heavy_check_mark:
2. Runtime errors :bangbang:
	- These are errors that only occur when the code runs and that are not syntax or simple logical errors.
	- These are usually harder to *debug* but Liclipse & Python make this quite easy :smirk:
	- As an example, let's say you want to read a file called **data.txt** with this code:
    ```python
    f = open("data.txt", "rb") #rb means in read mode
    data = f.read()
    print data
    f.close()
    ```
    Just copy this code, and run it with Liclipse.
    - Because there is no such file **data.txt**, the program fails at the line 1 :disappointed:
    - It tells you why: `IOError: [Errno 2] No such file or directory: 'data.txt'`
    - This `IOError` is called an **Exception** and there are plenty of other variants
    - You can also click on it and it will direct you to the line failing in the code :wink:
    - Note that the code works, but fails because of an external event
    

## Now write code

### The "scenario"
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
		# 0 by default for trees, gnomes, chocolates and balls
        self.time = time
        self.client = client
        self.trees = trees
        self.gnomes = gnomes
        self.chocolates = chocolates
        self.balls = balls
        
    def __repr__(self):
        return "At "+self.time+" "+self.client+" bought "+str(self.trees)+\
                " trees, "+str(self.gnomes)+" gnomes, "+str(self.chocolates)+\
                " chocolates and "+str(self.balls)+" balls."

t1 = Transaction("8:35AM", "John", trees=2, chocolates=1)
t2 = Transaction("10:45AM", "Mike", trees=1, gnomes=12)
t3 = Transaction("2:45PM", "Mike", gnomes=2)
t4 = Transaction("3:10PM", "Audrey", gnomes=2, balls=3)
t5 = Transaction("6:00PM", "John", balls=1)
transactions = [] #'list' structure
transactions.append(t1)
transactions.append(t2)
transactions.append(t3)
transactions.append(t4)
transactions.append(t5)
print "Last transaction t5 was: ", transactions[4] #starts from 0

prices = dict() #'dictionary' structure
prices["tree"] = 30
prices["gnome"] = 7.5
prices["chocolate"] = 12
prices["ball"] = 1.75
```

### What is wanted
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
[python_link]: https://www.python.org/downloads/release/python-2713/
[liclipse_link]: https://www.liclipse.com/download.html
[lesson_04]: /04.%20Github