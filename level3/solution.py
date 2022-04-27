import json

# function to calculate the commission of user depending on 
# - amount: the amount of the deal
# - amount_sold : the total amounts of his previous deals
# - objective: the objective of the user
def calculate_commision(amount,amount_sold,objective):
    commission=0
    if(amount_sold < 0.5 * objective and amount>0):
        if(amount + amount_sold > 0.5 * objective):
            commission = commission + (objective *0.5 - amount_sold)*0.05
            amount = amount - objective * 0.5
            amount_sold =amount_sold + objective *0.5 
        else:
            amount_sold = amount_sold + amount
            commission = commission +0.05*amount  
            amount = 0
    if(amount_sold >= 0.5 * objective and amount_sold<objective and amount>0):
        if(amount + amount_sold > objective):
            commission = commission + (objective - amount_sold)*0.1
            amount = amount - (objective - amount_sold)
            amount_sold = objective
        else: 
            commission = commission +0.1*amount
            amount_sold = amount_sold + amount
            amount = 0
    if(amount_sold >= objective and amount>0):
        commission = commission +0.15*amount
    return commission

#open the file input.json
f = open('./data/input.json')
 
#load data from input.json in data 
data = json.load(f)

#inputs
users= data["users"]
deals = data["deals"]

#output
output = {"commission":[],"deals":[]}

for user in users:
    commissions={}
    user_id = user["id"]
    objective = user["objective"]
    amount_sold = 0
    for deal in deals:
        amount= deal["amount"]
        if(deal["user"]==user_id):
            date = deal["payment_date"][0:7]
            commission = calculate_commision(amount,amount_sold,objective)
            if(date in commissions):
                commissions[date]= commissions[date]+commission
            else:
                commissions[date]=commission
            amount_sold = amount_sold + amount
            output["deals"].append({"id":deal['id'],"commission":commission})
    output["commission"].append({"user_id":user_id,"commission":commissions})


