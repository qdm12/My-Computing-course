# 9. Python and Yahoo Finance and OOP

## Definitions
- *OOP*: Object oriented programming, just means you some *classes* in your code (to make *"objects"*)

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
    - **Assume** we exchange these currencies at each transaction automatically

## What is wanted from us
1. Find and write the variable profit in *GBP* of each transaction, taking into account:
    - Cost of an item and the GBPCNY exchange rate at the date and time of transaction, UK timezone
    - Price of an item and the past EURGBP exchange rate at the date and time of transaction, UK timezone
    - **DO NOT TAKE INTO ACCOUNT** the *fixed costs*
    - Write the results in an extra column on the right most side in *transactions.xlsx*
2. Write to *transactions.xlsx* the overall profit in GBP since the beginning of the year, assuming today is the last transaction's date.
    - Take the fixed costs into account
    - Use the column previously created in part 1

## PART 1 OF 2: Variable profit of each transaction

## PART 2 OF 2: Overall profit since year's start
	
## What did you learn?
- More use of packages like for *yahoo-finance*
- More currency formatting for Excel
- Some bases for **OOP** which is very useful soon
	
## To add to your resume
- Yahoo Finance (Python)
- OOP or *Object oriented programming*