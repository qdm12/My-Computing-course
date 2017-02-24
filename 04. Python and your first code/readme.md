# 4. Python and your first code

## Final aim of this lesson
Write something that could be useful for some real business

## The "*scenario*"
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
    def __init__(self, date, time, client, trees=0, gnomes=0, chocolates=0, balls=0):
		# 0 by default for trees, gnomes, chocolates and balls
        self.date = date
        self.time = time
        self.client = client
        self.trees = trees
        self.gnomes = gnomes
        self.chocolates = chocolates
        self.balls = balls
        
    def __repr__(self): #used when you do `print t1` (see below)
        return "On "+self.date+" at "+self.time+" "+self.client+" bought "+\
                str(self.trees)+" trees, "+str(self.gnomes)+" gnomes, "+\
                str(self.chocolates)+" chocolates and "+str(self.balls)+" balls."

t1 = Transaction("30/01/2017", "8:35", "John", trees=2, chocolates=1)
t2 = Transaction("30/01/2017", "10:45", "Mike", trees=1, gnomes=12)
t3 = Transaction("30/01/2017", "14:45", "Mike", gnomes=2)
t4 = Transaction("30/01/2017", "15:10", "Audrey", gnomes=2, balls=3)
t5 = Transaction("30/01/2017", "18:00", "John", balls=1)
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

## What is wanted
### PART 1 of 3: Find how much we have sold overall that last Sunday
- Test the code above, understand how it works with `print`.
    - For example you can add `print prices` or `print transactions[2].client` at the end of the code
- Then write a function following this format:
```python
def find_total_sales(transactions, prices):
    total_sales = 0
    # Fill this in
    # Use for loops like this:
	# for element in elements_list:
	#     element = element + 5
    # Advice:
    # 1. Accumulate the total number of trees bought Sunday
    # 2. Accumulate the total number of gnomes bought Sunday
    # 3. Accumulate the total number of chocolates bought Sunday
    # 4. Accumulate the total number of balls bought Sunday
    # 5. Multiply each number of X by its associated price (Multiply with this syntax c = 2*5)
    # 6. Sum all the 4 total sales to get the total sale of Sunday
    return total_sales
```
- If you can't make it, you can have a look at the file `mycode1.py` online.

### PART 2 of 3: Find percentages of each product as its total sale participation
- For example, if we sold 3 christmas trees @ $30 and have sold $150 overall, the Chritmas
  tree total sale participation is 100 * (3*$30)/$150 = 60%.
- We want this information for the same Sunday as before
- Write (append) a function following this format:
```python
def find_participation(product_name, transactions, prices):
    total_sales = find_total_sales(transactions, prices)
	total_sales_product = 0
	for t in transactions:
		if product_name == "tree":
			# Accumulate each transaction tree's sales in total_sales_product
		elif product_name == "ball":
			#...
    # ...
	# You may have troubles here but it's good you'll learn that way !
	return participation
```
- Then just test it out with `print find_participation("tree", transactions, prices)` for example
- If you can't make it, you can have a look at the file `mycode2.py` online.

### PART 3 of 3: Find the sorted list of the clients spending with their name and spendings in a descending order
- Accumulate the total amount of money spent for each client (use a `dict()`)
- Then sort your dictionary in a descending order according the accumulated money spent
- Follow this format and finish up that new function
```python
def sort_clients_by_spending(transactions, prices):
	money_spent = dict() #Dictionary so you can have 3 clients or 300 it will still work
	for t in transactions:
		if t.client not in money_spent:
			money_spent[t.client] = 0 #initializes to 0 for a client not encountered before
		money_spent[t.client] += t.trees * prices["tree"] + t.gnomes * prices["gnome"] + \
								 t.chocolates * prices["chocolate"] + t.balls * prices["ball"]
	# You can't sort a dictionary unfortunately because its unordered
    # But you can sort a list which has indices and is ordered
    # Anyway, just google it it should only take one line to sort money_spent !
    # Here http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    return sorted_money_spent # That's a list of 'tuples' like [('mike',256), ('John', 23), ...]
```
- If you can't make it, you can have a look at the file `mycode3.py` online.
- If you think you're done, be sure it is in **DESCENDING** order (have a quick look [here](https://docs.python.org/2/howto/sorting.html#ascending-and-descending))

***

## What did you learn?
- **if**, **elif**, **else** conditions and **for** loops
- Python functions
- Python built-in types: *list*, *dict*, *tuple*
- First programming headaches
- Use of **GitKraken** or **Git**
- Use of **Liclipse**
- **Sort** data with `sorted`

WELL DONE ! You have wrote your first pieces of headaches in a Python program !

Time to take a break from Python and learn about [**Github**][lesson_05]

[lesson_05]: /05.%20Github