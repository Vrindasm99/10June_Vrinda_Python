import pandas 
import requests

url="https://fakestoreapi.com/products"

req=requests.get(url)
data=req.json()
print(data)

#print(x)
x=pandas.DataFrame(data)
#print(x)

for i in data:
    print(i)
    print(f"{"id":i.["id"]}")






