# 5. Excel file and data

![Excel][excel_image] XXXXX

## Aim
Process an excel file with Python code and write back results to it

## Excel spreadsheet
- I have generated an Excel spreadsheet, saved in the default **.xlsx** format
- It contains 4 columns and 10 000 *entries* (rows), structured as shown here:
XXXXX

## Python and **xlsx** format
1. Python does not *understand* **.xlsx** files yet, we need to add something
2. Have a look at the *Vagrantfile* of your *christmas-project*
   - You can use your code editor as usual or try entering `cat Vagrantfile` :wink:
   ```shell   
   cd /vagrant
   sudo pip install -r requirements.txt  
   ```
   - First line changes your directory (`cd`) to the shared directory
   - Second line tells **pip** to install what is asked for in the *requirements.txt* file
   - *Note: **pip** is a recursive acryonym: pip installs packages*
3. Now open the *requirements.txt* file with your code editor
  - Nothing ? Yes. Because we did not need any packages yet.
  - We need to read and write on excel **.xlsx** files, so we need a package for that
  - Just [Google python xlsx][google_xlsx] and the first thing you see is **openpyxl**
  - So add **openpyxl** to the first line of *requirements.txt*
4. Install the package in the VM: on your host machine's terminal
  - If you started the VM, enter `vagrant up`
  - Otherwise, enter `vagrant provision`

## The Python simplest code ever
1. In your host terminal, enter `touch mycode.py`
2. Open *mycode.py* with your code editor
3. Copy the following into it:
  ```python
  message = "Hello "
  name = "Denisa"  
  print message + name
  ```
4. Now in your VM (`vagrant up` if not done already):
  1. Go to the shared directory `cd /vagrant`
  2. Enter `python mycode.py` :wink:
  
## The Python code
- Copy the following in your Python code:
  ```python
  import openpyxl #to read and write excel files
  
  
  ```

  
[excel_image]: /internals/icons/excel.png
[google_xlsx]: https://www.google.com/search?q=python%20xlsx