print("Welcome to the Disneyland trip" )
print("I'm going to ask your experience about your disneyland trip")
print("calcualte how much your trip will cost")
#("Iinformation all group going to disney land trip")
name=(input("what is your name"))
number_of_people = int(input("How many people are going to disneyland"))
number_of_disneyland_park_days=int(input("How many days will you spend at disneyland")) 
hotel_nights=int(input("How many nights will you stay at hotel"))
number_of_park_hopper_ticket=int(input("How many park hopper days ticket do you have"))
#("these are expenses of disneyland trip")
ticket_price= float(input("How much is a ticket"))
total=number_of_people*ticket_price
park_hopper_price=float(input("what is the park hooper price per person "))
totalticketcost=park_hopper_price*number_of_people
food_cost_per_person=float(input("How much will per person spend on food each day"))
total_food_cost=food_cost_per_person*number_of_disneyland_park_days*number_of_people
souvenir_cost=float(input("How much will one person spend on souvenir"))
total_souvenir_cost=souvenir_cost*number_of_people
hotel_cost=float(input("How much does on hotel room cost per person"))
hotel_rooms=int(input("How many hotels rooms will your group need"))
hotel_cost_per_room=hotel_cost*hotel_nights
total_hotel_cost=hotel_cost_per_room*hotel_rooms
one_way_distance=float(input("How many miles away from disneyland do you live"))
vichel_mpg=float(input("How many miles per gallon does your vechile get"))
round_trip_Distance= one_way_distance*2
gas_price=float(input("what is today's price of regular gas per galon"))
gallons_needed=round_trip_Distance*vichel_mpg
total_gas_cost =gallons_needed*gas_price
parking_cost_per_day=float(input("How much does disneyland parking cost per day"))
total_parking_cost=parking_cost_per_day*number_of_disneyland_park_days
final_trip_cost=park_hopper_price*food_cost_per_person*souvenir_cost*total_hotel_cost*gas_price*parking_cost_per_day
cost_per_person=final_trip_cost* number_of_people
trip_budget=float(input("How much money does your group budget for the disneyland trip"))
cost_per_day=trip_budget* number_of_disneyland_park_days
buget_differnce=trip_budget-final_trip_cost
print("Your name is " + name)
print("you are going with" + str(number_of_people ))
print("How many disneyland park days"+ str(number_of_disneyland_park_days))
print("How many hotel nights"+str(hotel_nights))
print("How many park ticket do we have"+ str(number_of_park_hopper_ticket))
print("what is the total ticket cost"+str(totalticketcost))
print("How much is the food cost per person each day"+str(food_cost_per_person))
print("How much is the total food cost"+str(total_food_cost))
print("How much will one person spend on each day"+str(souvenir_cost))
print("what is the total souvenir cost"+str(total_souvenir_cost))
print("How much is  is the  hotel_cost"+str(hotel_cost))
print("How many hotel rooms do we need"+str(hotel_rooms))
print("What is one hotel room oer night"+str(hotel_cost_per_room))
print("WHat is the total hotel cost"+str(total_hotel_cost))
print("How many miles away is disneyland"+str(one_way_distance))
print("What is your vehicle's MPG"+str(vichel_mpg))
print("What is your round trip distance"+str(round_trip_Distance))
print("What is today gas price"+str(gas_price ))
print("How many gallons do we need"+str(gallons_needed))
print("What is total gas cost"+str(total_gas_cost))
print("How much is Disneyland parking per day"+str(parking_cost_per_day))
print("what is total parking cost"+str(total_parking_cost))
print("How much is the final trip cost"+str(final_trip_cost))
print("How is the cost per person for disneyland trip"+str(cost_per_person))
print("What is the trip budget"+str(trip_budget))
print("What is the cost per day "+str(cost_per_day))
print("What is your total trip budget"+str(buget_differnce))
#("Have a nice trip")