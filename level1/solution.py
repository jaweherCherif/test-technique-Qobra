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

for user in users :
    total_amounts=0
    number_of_deals=0
    for deal in deals:
        if(deal["user"]==user['id']):
            total_amounts= total_amounts +deal["amount"]
            number_of_deals = number_of_deals+1
    commission= calculate_commision(total_amounts,number_of_deals)
    output["commissions"].append({"user_id":user["id"],"commission":commission})
    

#create the file output.json and write in it the output
json_output = json.dumps(output, indent = 2)
with open("output.json", "w") as outfile:
    outfile.write(json_output)

f.close()

