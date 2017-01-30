# 1. The program :floppy_disk:

## First, how are computers so clever?
- Computers are **stupid**
  - Just do  ![0s and 1s][01s]  very quickly and a lot
  - Does not know anything about what we expect it to do
  - Similar to 6 billion :chicken: running around
- Programs are **clever**
  - Similar to one clever :tiger2: managing those 6 billion :chicken: idiots
  - Together, they can build great thing like pyramids
  - But it's hard to write programs to make use of this superfast stupidness
![Building pyramids][pyramid]

## What does a program do?
1. Takes **input(s)**
  - Website form
  - File / Database
  - Network or other programs
2. Does **stuff** on inputs
3. Produces **output**
  - Website page
  - File / Database change
  - Network or other programs

## From programming *code* to stupid *binary*
- Any code in any programming language is *compiled* into  ![0s and 1s][01s]  code
- With time, we gained more **abstraction** and it is much simpler to write code (easier *syntax*)
- The following will show you that
  - Back in the old days, we only had *assembly language*
  ```Assembly
  MOV R0, Dh
  MOV R1, 5h
  ADD R0, R1
  ```
  - Then we had *C++* (still use it)
  ```c++
  int a, b;
  a = 13;
  b = a + 5;
  ```
  - And now we have nice & simple *Python*
  ```python
  a = 13
  b = a + 5
  ```
  - Generally, to perform the same action, Python code is half the size of 
    C++ code which is a hundredth the size of Assembly code.
    
Now, time to dive into [good coding habits][lesson_02] :computer:

[01s]: /internals/gifs/01.gif
[pyramid]: https://www.dropbox.com/s/mjvsv4njvf6e28s/pyramids.gif?dl=1
[lesson_02]: /02.%20Code%20writing