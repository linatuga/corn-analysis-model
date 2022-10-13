#an API request contains the base URL and the parameters which are after the question mark.
#paramaters are specific
import requests #module
import json #help convert jason documents into dictionaries, making api repsonse python friendly
baseUrl = "https://api.upcitemdb.com/prod/trial/lookup"
#create a python dictionary
parameters = {'upc':'073366118238'} #contructs the parameters of the API calls, ucp is key and barcoede the value
#in the documentation for the api sometimes they want you to add an extra key
response = requests.get(baseUrl, params = parameters) #params a dictionary, list of tuples or bytes send as a query string
print(response.url)
#constructed first request for an api
#now we will contruct the response
content = response.content
info = json.loads(content)
print(type(info))
print(info)
#we are gonna try isolating specific data such as name and the brand. 
item = info['items']
itemInfo = item[0]
#grab the dictionaries values for the key title and brand
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)
#functionality of 14 line script
#converts barcodes into their corresponding item name and brand
#
