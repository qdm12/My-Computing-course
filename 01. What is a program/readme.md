# 01. The program :floppy_disk:

## First, how are computers so clever?
- Computers are **stupid**
  - Just do  ![0s and 1s](/internals/gifs/01.gif)  very quickly and a lot
  - Does not know anything about what we expect it to do
  - Similar to 6 billion :chicken: running around
- Programs are **clever**
  - Similar to one clever :tiger2: managing those 6 billion :chicken: idiots
  - Together, they can build great thing like pyramids
  - But it's hard to write programs to make use of this superfast stupidness
![Building pyramids](dropbox.com/s/mjvsv4njvf6e28s/pyramids.gif?dl=1)
  
## What does a program do?
- Takes **input(s)**
  - Website form
  - File / Database
  - Network or other programs
- Does **stuff** on inputs
- Produces **output**
  - Website page
  - File / Database change
  - Network or other programs

## Programming to stupid *binary*
- Any code in any programming language is *compiled* into ![0s and 1s](/internals/gifs/01.gif)  code
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
  - Generally, to perform the same action, Python code is half of C++ code which is a hundredth of Assembly.