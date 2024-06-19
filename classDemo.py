
class Customer:
    def __init__(self, name):
        self.Id = 5
        self.name = name

    def get_Id(self):
        return self.Id, self.name
    
class Manager:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name  

manager = Manager("Ove")


class Store:
    def __init__(self, store_name, manager):
        self.store_name = store_name
        self.customer_visiting = []
        self.manager = manager

    def customer_enter(self, customer):
        if isinstance(customer, Customer):
            self.customer_visiting.append(customer)
            print(customer.name)
        else:
            print(f'Note to {self.manager.name} non customer {customer} is visiting')
    
    def customer_exits(self, customer, time):
        if isinstance(customer, Customer) and customer in self.customer_visiting:
            self.customer_visiting.remove(customer)
            print(customer.get_Id(), time)

oscar = Customer('Oscar')
lina = Customer('Lina')


candy_store = Store('CandyStore', manager)
candy_store.customer_enter(lina)
candy_store.customer_enter(oscar)

candy_store.customer_exits(lina, "Five")

visiting_manager = Manager('Lana')

candy_store.customer_enter(visiting_manager)