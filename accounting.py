def customer_expectation(filename):
    """This function opens files with list of customer name ,amout paid and excepted amount
    and if the amount paid doesnot match amount customer paid then it will print that 
    customer's name with amount paid and excepted amount"""
    file = open(filename)
    for line in file:
        sep_words = line.split('|')
        customer_name = sep_words[1]
        customer_paid = float(sep_words[2])    
        customer_expected = float(sep_words[3])
        if customer_expected != customer_paid:
            print(f"{customer_name} paid ${customer_paid},expected ${customer_expected}")