melon_cost = 1.00 #cost of one melon
def customer_expectation(filename):
    """This function opens files with list of customer name ,amout paid and excepted amount
    and if the amount paid doesnot match amount customer paid then it will print that 
    customer's name with amount paid and excepted amount"""
    file = open(filename) #open file
    for line in file: #loop to check each line in the file
        sep_words = line.split('|') #spliting each words in line by |
        customer_fullname = sep_words[1] #first split is the full name
        customer_firstname = customer_fullname.split(" ")[0] # spliting first and last name getting first name
        melon_qty = sep_words[2]    #gets number of melon purched
        expected_amt = float(melon_qty * melon_cost) #calculates expected amount
        customer_paid = float(sep_words[3]) #get amont customer paid from file
        print(f"{customer_fullname} paid ${customer_paid},expected ${expected_amt}") #print genral file
        #check and prints if customer underpaid or overpaid
        if customer_paid > expected_amt:
            print(f"{customer_firstname} overpaid for purchase")
        elif customer_paid < expected_amt:
            print(f"{customer_firstname} underpaid for their purchase")    
        
    filename.close()