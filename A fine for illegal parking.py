def calculate_change(paid, price):
    change = paid - price
    return change

ticket_price = 30
print("===== PARKING TICKET PAYMENT HELPER =====")
print(f"This parking ticket costs {ticket_price} untis. ")
print("Accepted coins are 1, 5, 10, 25\n")

totalins = 0
coinsins = 0

while True:
    coin = int(input("Insert a coin (1, 5, 10 or 25)"))
    
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid code, try again.\n")
        continue
    
    totalins += coin
    coinsins += 1
    print(f"Inserted {coin}. Total so far: {totalins}\n")
    
    if totalins >= ticket_price:
        print("Enough money inserted!\n")
        break
    
    changedue = calculate_change(totalins, ticket_price)
    
print("Printing...")

if changedue == 0:
    pass
else:
    print(f"Here is your change: {changedue} units.")
    
print("\n===== Payment summary =====")
print("Ticket price: ", ticket_price)
print("Coins inserted: ", coinsins)
print("Total paid: ", totalins)
print("Change given: ", changedue)
print("=============================")
print("Parking ticket payment complete!")