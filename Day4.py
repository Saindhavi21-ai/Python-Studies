flights = {
    "AI101": {"source": "Delhi", "dest": "Mumbai", "seats": 5, "price": 5500},
    "AI102": {"source": "Mumbai", "dest": "Delhi", "seats": 8, "price": 5200},
    "6E201": {"source": "Bangalore", "dest": "Chennai", "seats": 3, "price": 3200},
    "6E202": {"source": "Chennai", "dest": "Bangalore", "seats": 4, "price": 3100},
    "UK301": {"source": "Delhi", "dest": "Kolkata", "seats": 2, "price": 6000},
    "UK302": {"source": "Kolkata", "dest": "Delhi", "seats": 6, "price": 6200},
    "SG401": {"source": "Hyderabad", "dest": "Pune", "seats": 10, "price": 4000},
    "SG402": {"source": "Pune", "dest": "Hyderabad", "seats": 7, "price": 4100},
    "QP501": {"source": "Ahmedabad", "dest": "Delhi", "seats": 5, "price": 3500},
    "QP502": {"source": "Delhi", "dest": "Ahmedabad", "seats": 9, "price": 3600}
}


s=input("Enter the source : ")
d=input("Enter the Destination : ")

found=False

for i,j in flights.items():
    if s.lower()  == j["source"].lower() :
        if d.lower() == j["dest"].lower():
            print("Flight available!")
            print("Flight No : ",i)
            print("Seats available : ",j["seats"])
            print("Price : ",j["price"])
            found=True

            sit=int(input("Enter the no of seats : "))

            if sit<=j["seats"]:
                print(f"{sit} seat(s) confirmed.")
                j["seats"]-=sit
            
            else:
                print("Required seats not available!")
            
            break
                

if found==False :
    print("Flight between the give source and destination is not available!")

print("\n\n")
print(flights)

#Output
Enter the source : Chennai
Enter the Destination : BANGALORE
Flight available!
Flight No :  6E202
Seats available :  4
Price :  3100
Enter the no of seats : 4
4 seat(s) confirmed.


{'AI101': {'source': 'Delhi', 'dest': 'Mumbai', 'seats': 5, 'price': 5500}, 
 'AI102': {'source': 'Mumbai', 'dest': 'Delhi', 'seats': 8, 'price': 5200}, 
 '6E201': {'source': 'Bangalore', 'dest': 'Chennai', 'seats': 3, 'price': 3200}, 
 '6E202': {'source': 'Chennai', 'dest': 'Bangalore', 'seats': 0, 'price': 3100}, 
 'UK301': {'source': 'Delhi', 'dest': 'Kolkata', 'seats': 2, 'price': 6000}, 
 'UK302': {'source': 'Kolkata', 'dest': 'Delhi', 'seats': 6, 'price': 6200}, 
 'SG401': {'source': 'Hyderabad', 'dest': 'Pune', 'seats': 10, 'price': 4000}, 
 'SG402': {'source': 'Pune', 'dest': 'Hyderabad', 'seats': 7, 'price': 4100}, 
 'QP501': {'source': 'Ahmedabad', 'dest': 'Delhi', 'seats': 5, 'price': 3500}, 
 'QP502': {'source': 'Delhi', 'dest': 'Ahmedabad', 'seats': 9, 'price': 3600}}


# Output 2
Enter the source : CHENNAI
Enter the Destination : COIMBATORE
Flight between the give source and destination is not available!


{'AI101': {'source': 'Delhi', 'dest': 'Mumbai', 'seats': 5, 'price': 5500}, 
 'AI102': {'source': 'Mumbai', 'dest': 'Delhi', 'seats': 8, 'price': 5200}, 
 '6E201': {'source': 'Bangalore', 'dest': 'Chennai', 'seats': 3, 'price': 3200}, 
 '6E202': {'source': 'Chennai', 'dest': 'Bangalore', 'seats': 0, 'price': 3100}, 
 'UK301': {'source': 'Delhi', 'dest': 'Kolkata', 'seats': 2, 'price': 6000}, 
 'UK302': {'source': 'Kolkata', 'dest': 'Delhi', 'seats': 6, 'price': 6200}, 
 'SG401': {'source': 'Hyderabad', 'dest': 'Pune', 'seats': 10, 'price': 4000}, 
 'SG402': {'source': 'Pune', 'dest': 'Hyderabad', 'seats': 7, 'price': 4100}, 
 'QP501': {'source': 'Ahmedabad', 'dest': 'Delhi', 'seats': 5, 'price': 3500}, 
 'QP502': {'source': 'Delhi', 'dest': 'Ahmedabad', 'seats': 9, 'price': 3600}}
