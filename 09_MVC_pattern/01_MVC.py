class Model:
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15}
    }

class View:
    def list_services(self, services):
        for i, svc in enumerate(services, 1):
            print(f'  {i}.',svc, ' ')
    
    def list_pricing(self, services):
        for svc in services:
            print("  For", Model.services[svc]['number'], 
                  svc, 'message you pay $', Model.services[svc]['price'])

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        
    def get_services(self):
        services = self.model.services.keys()
        return (self.view.list_services(services))
    
    def get_pricing(self):
        services = self.model.services.keys()
        return (self.view.list_pricing(services))
    
class Client:
    controller = Controller()
    print("[View]: Services Provided")
    controller.get_services()
    print("[View]: Pricing for Service")
    controller.get_pricing()