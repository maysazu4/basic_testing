# def pick_winner(names):
#     pass

# class Person:
#     def __init__(self,tickets) -> None:
#         self.tickets = tickets
#     def add_ticket(self):
#         self.tickets += 1

# class Raffle:
#     def check_init_params_types_and_values(self,max_people_num, max_tickets_num,earnings,ticket_price,people):
#         if type(max_tickets_num)!=int or type(max_people_num) != int \
#             or type(earnings) != int or type(ticket_price) != int or not isinstance(people,list):
#             raise TypeError('Invalid Type!')
#         elif earnings != 0 or people != [] or max_people_num <= 0 or max_tickets_num <= 0 or ticket_price <= 0 :
#             raise ValueError('Invalid Value!')

#     def __init__(self,max_people_num, max_tickets_num,earnings,ticket_price,people) -> None:
#         try:
#             self.check_init_params_types_and_values(max_people_num, max_tickets_num,earnings,ticket_price,people)
#             self.max_people_num = max_people_num,
#             self.max_tickets_num = max_tickets_num,
#             self.earnings = earnings,
#             self.ticket_price = ticket_price,
#             self.people = people
        
#         except TypeError as te:
#             print("Error:", te)
#         except ValueError as ve:
#             print("Error:", ve)  
#         except Exception as e:
#             print("Error:", e)
            
#     def get_ticket_price(self):
#         return self.ticket_price     
    
#     def get_max_tickets_num(self):
#         return self.max_tickets_num 
    
#     def get_people(self):
#         return self.people

#     def get_max_people_num(self): 





#     def buy_ticket(self,person):
#         try:
#             #check if the argument is person object
#             if not isinstance(person, Person):
#                 raise TypeError("Type must be Person")
#             #check if there are enough tickets
#             if self.max_tickets_num == 0:
#                 print('Sorry, all tickets have been sold.')
#                 return False
#             #there are enough tickets, check if the person is particpant, if not check if we can add more people to the raffle
#             elif person not in self.people:
#                 if self.max_people_num == 0:
#                     print('Sorry, we cannot accept any more participants.')
#                     return False
#                 else:
#                     #the person joined the raffle
#                     self.people.append(person)
#                     self.max_people_num -= 1
#             # the person can buy a ticket
#             # Add the ticket to person tickets, add the price to the earnings,and remove one ticket
#             person.add_ticket()
#             self.earnings += self.ticket_price
#             self.max_tickets_num -= 1
#         except TypeError as ve:
#             print("Error:", ve)
#         except Exception as e:
#             print("Error:", e)

#     def select_winner(self):
#         max_tickets = 0
#         winner = None
#         #find the person who bought the biggest number of tickets
#         for person in self.people:
#             if person.tickets > max_tickets:
#                 winner = person
#         return winner

        

