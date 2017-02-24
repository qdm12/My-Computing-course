# 3. Python and setup

[![Python][python_image]][python_link]

## Final aim of this lesson
Setup your installation, learn how to use some tools and understand some codes.

## How to write your code

### Setting up Liclipse and Python

Although you can write code in any text editor *"blindly"* :see_no_evil:, 
it is better to see what syntax errors :x: or what possibilities you have while writing code.

1. Install [**Python 2.7**][python_link]
    - You should **already** have Python on Mac OS and some Linux OS*, just check it by entering `python` in your terminal.
2. Install [**Liclipse**][liclipse_link]
3. Launch Liclipse
4. Choose a workplace as it prompts you for it and tick :ballot_box_with_check:
   the *always use this workplace* box)
5. Finally, choose the **Liclipse dark theme** :black_large_square:
6. In Liclipse, on the top left, click on **File**, **New**, **Pydev project** :new:
    1. Click on **Configure the Python interpreter** and then **Quick auto-config**
    2. For the project name, enter *myproject* then click on **Finish**
7. In your workplace, you now have a directory *myproject* with only the files *.project* and *.pydevproject* in it; but Python :snake: is ready !

### Create a Python *.py* file (or *module*) mycode.py
- Option 1: In your terminal, `cd` to the Liclipse's *myproject* directory and enter `touch mycode.py`
- Option 2: In Liclipse, click on **File**, **New**, **Pydev Module**, enter *mycode.py* in the name field and click on **Finish** :new:
- Option 3: In your file explorer, create a file named *mycode.py* :page_with_curl:

### Test out the installation Liclipse + Python
1. In Liclipse, double-click on *myproject* on the left directory pane to expand it.
2. Double-click on *mycode.py* to open it.
3. Write `print "Hello"` in *mycode.py*.
4. To run your code the **first** time:
    - Right click on *mycode.py* on the left pane
    - Hover over **Run as**
    - Click on **1 Python Run**
5. After that, run it by pressing on the *Play* button :arrow_forward: at the top or by pressing your **F9** key.
    - *Note that you can still run that code with `python mycode.py` in your terminal.*
6. You should see *Hello* in the Liclipse bottom pane console.

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


## Example 1: Calculate your age in Python
1. Overwrite/Copy the following into *mycode.py*:
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
   #float() converts to a floating point number. It is necessary to floating point divisions !
   print "You are "+str(age_float)+" years old"
   #str() converts to 'text' (string)
   ```
2. Run the code ! (with the **Play** button at the top)
3. Understand it, especially the comments (with `#`)

## Example 2: Perform an average on a list of numbers
1. Delete the content and copy the following into *mycode.py*:
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
2. Run the code ! (with the **Play** button at the top)
3. Understand it

***
    
Now that you are ready to write some Python well... [lesson 4][lesson_04]

## What did you learn?
- Setup Python and Liclipse
- Create modules and test them in Liclipse
- Syntax and runtime errors in Python and Liclipse

## To add to your resume
- Python 2.7
- Liclipse

[python_image]: /internals/icons/python.png
[python_link]: https://www.python.org/downloads/release/python-2713/
[liclipse_link]: https://www.liclipse.com/download.html
[lesson_04]: /04.%20Python%20and%20your%20first%20code