# 9. Python, currencies and OOP

## Definitions
- *OOP*: Object oriented programming, just means you use *classes* in your code (to make *"objects"*)

## Excel spreadsheets, just to remind you...
- **transactions.xlsx** is a record of all the client quantity purchases since the beginning of the year
- **costs_and_prices.xlsx** indicates the following information:
    - The cost of an item
        - It is the cost to manufacture and ship the item
        - It is in *CNY* :yen: because our products are all made in China :blush:
    - The price of an item is the price at which it is sold to the client (with 15% tax :weary:)
        - So we need to deduce these 15% we have to pay to the state from our gains
        - These are in *EUR* :euro: because we ship to European countries
    - The fixed costs
        - This indicates the costs of the warehouse, the web server etc. per week
        - This one is in *GBP* :pound: because the company is actually based in UK :gb:
    - Note that our final revenues or profits are in *GBP*
    - **Assume** we exchange all revenues and costs in GBP on the day of the transaction automatically

## What is wanted from us
1. Find and write the variable profit in *GBP* of each transaction, only taking into account:
    - The cost of an item and the GBPCNY exchange rate at the date of transaction, UK timezone
    - Price of an item and the past EURGBP exchange rate at the date of transaction, UK timezone
    - Write the results in an extra column "Variable Profit" on the right most side in *transactions.xlsx*
    - **DO NOT TAKE INTO ACCOUNT** the *fixed costs*
2. Write to *transactions.xlsx* the overall profit in GBP since the beginning of the year, assuming today is the last transaction's date.
    - Take the fixed costs into account
    - Use the column previously created in part 1

## PART 1 OF 2: Variable profit of each transaction

### Historical exchange rates of GBPCNY and EURGBP

First, just create the file **online.py**

#### Skeleton
We want to write a function following this skeleton (add it to *online.py*):
```python
def get_historical_exchange_rate(currency_pair, date):
    """ Fetches the exchange rate of a currency pair at a certain date.

        Args:
            currency_pair (string): Currency pair in the form USDEUR
            date (string): European date format dd/mm/yyyy

        Returns:
            rate (float): Exchange rate of the currency pair
    """
    currency1 = currency_pair[0:3]
    currency2 = currency_pair[3:]
    if currency1 == currency2: #if it is CNYCNY, EUREUR... just return 1.00
        return 1.00
    # get the historical exchange rate somehow here...
    return rate
```
- The *arguments* (inputs) are the currency pair (*such as GBPCNY*) and the date (*such as 05/01/2017*)
- The *return value* (output) should be the actual exchange rate we are searching for

#### Historical exchange rates and fixer.io
- Just so you know: I tried hard on Yahoo Finance but their *YQL* database is quite bugged so let's forget it.
- Instead, we'll use [**fixer.io**](fixerio_link) which takes data from the European Central Bank.
    - The data is from the European Central Bank
    - The rates are updated daily at around 4PM (*which suits our problem here*)
    - It is way easier to use than Yahoo Finance oddly...
- In your browser, try entering this URL: [https://api.fixer.io/latest?base=GBP&symbols=EUR&date=2017-01-05][fixerio_query_link]
- And TADAA you get an ugly "*JSON*" response where the rate is the last number on the line

#### Plug *fixer.io* into *Python*
There is a built-in Python package called urllib which is great for web stuff
1. At the top of *online.py*, add:
```python
from urllib import urlopen
```
2. Add the main thingy at the bottom of *online.py*:
```python
if __name__ == "__main__":
   url = 'https://api.fixer.io/latest?base=GBP&symbols=EUR&date=2017-01-05'
   response = urlopen(url)
   print response.read()
```
3. Now run **online.py** and TADAA you got the same ugly JSON response...
4. You may remove that print line you just added if you feel like it

#### Parse this ugly JSON
We are only interested into the last number (exchange rate) of the response.
1. To parse json, well, you just add that to the top of *online.py*:
```python
from json import load
```
2. Then append the following to your *main* code:
```python
   data = load(response)
   rate_string = data["rates"]["EUR"]
   print rate_string  
```
3. Now run **online.py** and TADAA the last printed line is the rate (a string though, so convert it later with **float()**)

#### Plug this into the skeleton
- Let's make it work universally for any currencies and any date !
- Think about what are the parameters: **date**, **currency1**, **currency2**
- What should be the output? A **floating** number representing the rate.
- You should be able to do that function easily. Just in case, here is the solution:
```python
def get_historical_exchange_rate(currency_pair, date):
  """ Fetches the exchange rate of a currency pair at a certain date.
  
      The rates are fetched from fixer.io (European central bank), which are 
      updated daily at 4PM EST.

      Args:
          currency_pair (string): Currency pair in the form USDEUR
          date (string): European date format dd/mm/yyyy

      Returns:
          rate (float): Exchange rate of the currency pair
  """
  currency1 = currency_pair[0:3]
  currency2 = currency_pair[3:]
  if currency1 == currency2: #if we want the rate USDUSD or EUREUR etc.
      return 1.00
  date = date.split('/')
  date = date[2] + "-" + date[1] + "-" + date[0] #format for fixer.io
  response = urlopen("https://api.fixer.io/latest?base="+currency1+"&symbols="+currency2+"&date="+date)
  data = load(response)
  rate_string = data["rates"][currency2]
  rate = float(rate_string) #converts to floating point number
  return rate
```
- Finally, replace your code in the main block with:
```python
if __name__ == "__main__":
  print get_historical_exchange_rate("GBPEUR", "05/01/2017")
```
- You can run *online.py* to test out everything works as planned.
  
### TO BE CONTINUED ===


## PART 2 OF 2: Overall profit since year's start

	
## What did you learn?
- Use of Python built-in packages urllib and json
- Some simple Web parsing (you can urlopen any page and dig in the webpage)
- fixer.io
- More currency formatting for Excel
- Some bases for **OOP** which is very useful soon
	
## To add to your resume
- web parsing
- fixer.io
- OOP or *Object oriented programming*


[fixerio_link]: http://fixer.io/
[fixerio_query_link]: https://api.fixer.io/latest?base=GBP&symbols=EUR&date=2017-01-05