# 5. Python and setup

[![Python][python_image]][python_link]

## Final aim of this lesson
Understand some Python, setup your installation and learn how to use some tools.

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

***

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
	3. In your workplace, you now have a directory *first-project* with only the files *.project* and *.pydevproject* in it; but Python :snake: is ready !

### Add what you've done to *Liclipse*'s project
To add what we've done in the previous [Github lesson 4][lesson_04]:
- Nerdy way, with your terminal :computer: :
	- Modify and enter `cp -fr /home/username/lesson_04/first-project/* /home/username/workplace/first-project/`
- Normal way, with your file explorer:
	1. Go to your *first-project* directory you have cloned in lesson 4 with **git** :open_file_folder:
	2. Select all the files **including** the **.git** sub-directory (which contain all the git & github information)
	3. Copy them and paste them into the *first-project* directory created in the Liclipse workspace directory.

### Ignore the Liclipse's project files for Git
- The problem
    - In your terminal, enter `git status`
    - You will see in red two `modified:` concerning the project files *.project* and *.pydevproject*
    - These are only used by Liclipse to remember your theme and so on.
    - You don't want them to be uploaded to Github
- The solution
    - Create a file *.gitignore*
    - Write the following into it and save it
    ```
    .project
    .pydevproject
    .vagrant
    *.pyc
    ```
    - Enter `git status` again, and these files will disappear from git :wink:
    - *PS*: `.vagrant` is to ignore the VM files when you're gonna `vagrant up`
    - *PS*: `*.pyc` is to ignore any **.pyc** files *compiled* by Liclipse from your Python code
- Why: because later on you might use `git add .` to add all the modifications made in all the files

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
    
Now that you are ready to write some Python well... [lesson 6][lesson_06]

## What did you learn?
- Run Python code with a Vagrant VM
- Setup Python and Liclipse
- Create modules and test them in Liclipse
- Use of `.gitignore` to ignore files in Git
- Syntax and runtime errors in Python and Liclipse

## To add to your resume
- Python 2.7
- Liclipse

[python_image]: /internals/icons/python.png
[python_link]: https://www.python.org/downloads/release/python-2713/
[liclipse_link]: https://www.liclipse.com/download.html
[lesson_04]: /04.%20Github
[lesson_06]: /06.%20Python%20and%20your%20first%20code