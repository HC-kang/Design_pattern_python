from abc import ABCMeta, abstractmethod

# AbstractClass
class Trip(metaclass = ABCMeta):
    @abstractmethod
    def setTransport(self):
        pass
    
    @abstractmethod
    def day1(self):
        pass
    
    @abstractmethod
    def day2(self):
        pass
    
    @abstractmethod
    def day3(self):
        pass
    
    @abstractmethod
    def returnHome(self):
        pass
    
    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()
      
# ConcreteClass1 
class VeniceTrip(Trip):
    def setTransport(self):
        print("Take a boat and find your way in the Grand Canal")
        
    def day1(self):
        print("Day1: Visit St Mark's Basilica in St Mark's Square")
        
    def day2(self):
        print("Day2: Appreciate Doge's Palace")
        
    def day3(self):
        print("Day3: Enjoy the food near the Rialto Bridge")
        
    def returnHome(self):
        print("Get Souvenirs for friends and get back")
        

# ConcreteClass2
class MaldivesTrip(Trip):
    def setTransport(self):
        print("On foot, on any island, Wow!")
        
    def day1(self):
        print("Day1: Enjoy the marine life of Banana Reef")
        
    def day2(self):
        print("Day2: Go for the water sports and snorkelling")
        
    def day3(self):
        print("Day3: Relax on the beach and enjoy the sun")
        
    def returnHome(self):
        print("Don't fell like leaving the beach..")
        
# Client
class TravelAgency:
    def arrange_trip(self):
        choice = input("What kind of place you'd like to go historical or to a beach?")
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        elif choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()
            
TravelAgency().arrange_trip()