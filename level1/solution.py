import json

#open the file input.json
f = open('./data/input.json')

#load data from input.json in data 
data = json.load(f)

#inputs
users=data["users"]
deals = data["deals"]

#output
output={"commissions":[]}
