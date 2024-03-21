import pytest
import src.raffle as r
import src.person as p
import unittest


class TestRaffle(unittest.TestCase):
    def setUp(self):
        self.raffle = r.Raffle(max_people_num=5, max_tickets_num=10, earnings = 0,ticket_price = 10,people = [] )
        self.person = p.Person()

    def test_sell_tickets_success(self):
        people_list  = [p.Person() for _ in range(5)]
        #sell one ticket to the same 5 people again
        for person in people_list:
            self.assertTrue(self.raffle.sell_ticket(person))
        for person in people_list:
            self.assertTrue(self.raffle.sell_ticket(person))
        self.assertEqual(self.raffle.max_people_num, 0)  
        self.assertEqual(self.raffle.max_tickets_num, 0)  
        self.assertEqual(self.raffle.earnings, 100)  
        self.assertEqual(self.raffle.people, people_list) 
        for person in people_list:
            self.assertEqual(person.tickets,2)

    def test_sell_tickets_max_participants_reached(self):
        people_list  = [p.Person() for _ in range(5)]
        #sell one ticket to the same 5 people again
        for person in people_list:
            self.assertTrue(self.raffle.sell_ticket(person))
        p1 = p.Person()
        self.assertFalse(self.raffle.sell_ticket(p1))
    
    def test_sell_tickets_max_tickets_reached(self):
        people_list  = [p.Person() for _ in range(5)]
        # sell one ticket to the same 5 people again
        for person in people_list:
            self.assertTrue(self.raffle.sell_ticket(person))
        # sell 5 tickets more
        for i in range(5):
            self.assertTrue(self.raffle.sell_ticket(people_list[0]))
        # tickets sold out
        self.assertFalse(self.raffle.sell_ticket(people_list[0]))

    # def test_sell

        















    # def test_sell_tickets_insufficient_funds(self):
    #     buyer = MockPerson(money=5)
    #     self.assertFalse(self.raffle.sell_tickets(buyer, 2))  # Buyer doesn't have enough money

    # def test_sell_tickets_max_participants_reached(self):
    #     buyer1 = MockPerson(money=30)
    #     buyer2 = MockPerson(money=30)
    #     self.assertTrue(self.raffle.sell_tickets(buyer1, 2))
    #     self.assertTrue(self.raffle.sell_tickets(buyer2, 2))
    #     self.assertFalse(self.raffle.sell_tickets(MockPerson(money=30), 2))  # Max participants reached

    # def test_sell_tickets_max_tickets_reached(self):
    #     buyer = MockPerson(money=50)
    #     self.assertTrue(self.raffle.sell_tickets(buyer, 3))
    #     self.assertFalse(self.raffle.sell_tickets(buyer, 1))  # Max tickets reached

if __name__ == '__main__':
    unittest.main()