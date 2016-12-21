# 02. Code writing

![Code writing example](code_writing)

## Code editor
- [![Atom.io][atom_image]][atom_link]
- Python
  - [Liclipse](liclipse.com/download.html)
- Mac OSX
  - [Coda 2](panic.com/coda/)
- Windows
  - [Notepad++](notepad-plus-plus.org/download/v7.2.2.html)

## Test your code ASAP
- Always **test** your code by running it :running:
  - Even with some fake data you make up
  - Find a :bug: (*bug*) early !
- Use the *Python console* for simple stuff, by entering `python` in a terminal
- Run directly your code by entering `python mycode.py` in a terminal (or use Liclipse)

## Code style :computer:
- Your code has to be understandable by **others** (and **you** in the *future*)
- Write explicit code
  - Choose names wisely (for *variables*, *functions*, etc.)
  - Comment your code
  - Check the input which can be trash
- Think as your code as re-usable :recycle:
- Good example :wink: :
```python
def find_average(numbers_list):
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
```
- Bad example :japanese_ogre: :
```python
def getavg(numbers):
  s = 0
  for x in numbers:
      sum = sum + x
  return float(sum) / numbers.length
```
- Best super complete example :relieved: :
```python
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
```
      
## Other tips
- You mostly need to know about **if**, **elif** (*else if*) and **else**.
- And **for loops**, but I'll teach you that

Before going any further, time to [Vagrant up](github.com/qdm12/My-Computing-course/tree/master/03.%20Vagrant)


[code_writing]: internals/gif/code_writing.gif "Code writing example"
[atom_link]: atom.io
[atom_image]: internals/icons/atom.io.png "Atom.io"