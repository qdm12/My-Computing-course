class Transaction(object): #don't be scared
    def __init__(self, time, client, trees=0, gnomes=0, chocolates=0, balls=0):
        # 0 by default for trees, gnomes, chocolates and balls
        self.time = time
        self.client = client
        self.trees = trees
        self.gnomes = gnomes
        self.chocolates = chocolates
        self.balls = balls
        
    def __repr__(self): #used when you do `print t1` (see below)
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

def find_total_sales(transactions, prices):
    """ Returns the total sales from the transactions provided

        Args:
            transactions (list): List of Transaction objects
            prices (dict): Dictionary of prices
            
        Returns:
            total_sales (float): Total sales in money
    """
    total_sales = 0
    total_trees_sold = 0
    total_gnomes_sold = 0
    total_chocolates_sold = 0
    total_balls_sold = 0
    for t in transactions:
        total_trees_sold += t.trees
        total_gnomes_sold += t.gnomes
        total_chocolates_sold += t.chocolates
        total_balls_sold += t.balls
    total_sales = total_trees_sold * prices["tree"] + \
                  total_gnomes_sold * prices["gnome"] + \
                  total_chocolates_sold * prices["chocolate"] + \
                  total_balls_sold * prices["ball"]
    return total_sales
    
def find_participation(product_name, transactions, prices):
    """ Returns the percentage participation of a product in the total sales

        Args:
            product_name (string): Name of the product
            transactions (list): List of Transaction objects
            prices (dict): Dictionary of prices
            
        Returns:
            participation (float): Percentage of participation of product in total sales
    """
    total_sales = find_total_sales(transactions, prices)
    total_sales_product = 0
    for t in transactions:
        if product_name == "tree":
            total_sales_product += t.trees * prices["tree"]
        elif product_name == "gnome":
            total_sales_product += t.gnomes * prices["gnome"]
        elif product_name == "chocolate":
            total_sales_product += t.chocolates * prices["chocolate"]
        elif product_name == "ball":
            total_sales_product += t.balls * prices["ball"]
        else:
            raise Exception("This product does not exist !") #stops the program entirely
    participation = 100 * (float(total_sales_product) / total_sales) # float() just to make sure division is floating :)
    return participation
    
print "Tree % participation in total sales: ", find_participation("tree", transactions, prices)
print "Gnome % participation in total sales: ", find_participation("gnome", transactions, prices)
print "Chocolate % participation in total sales: ", find_participation("chocolate", transactions, prices)
print "Ball % participation in total sales: ", find_participation("ball", transactions, prices)