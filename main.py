import requests
def get_crypto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code == 200 :
        return response.json()
    

    
crypto_response = get_crypto_data()
user_input = input("Enter your crypto currency: ")

count = 0

for crypto in crypto_response:
    count +=1
    print(count)
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break



