import json

# define function to calculate commission of user depending on the number of deals he made and the total amounts of these deals
def calculate_commision(total_amounts,number_of_deals):
    commission=0
    if(number_of_deals<=2):
        commission = total_amounts*0.1
    else:
        if(number_of_deals>=3):
            commission = total_amounts*0.2
    if(total_amounts>2000):
        commission = commission+500
    return commission
       

#open the file input.json
f = open('./data/input.json')

#load data from input.json in data 
data = json.load(f)

#inputs
users=data["users"]
deals = data["deals"]

#output
output={"commissions":[]}
