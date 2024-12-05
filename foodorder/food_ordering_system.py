class MenuItem:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability
        self.next = None 

class MenuLinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, name, price, availability):
        new_item = MenuItem(name, price, availability)
        if not self.head:
            self.head = new_item
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_item

    def display_menu(self):
        temp = self.head
        while temp:
            print(f"Name: {temp.name}, Price: ₹{temp.price}, Available: {temp.availability}")
            temp = temp.next

class OrderQueue:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def process_order(self):
        if self.orders:
            order = self.orders.pop(0)
            print(f"Processing Order: {order}")
        else:
            print("No orders to process.")

    def display_orders(self):
        if self.orders:
            print("Pending Orders:")
            for order in self.orders:
                print(order)
        else:
            print("No orders in the queue.")

class OrderStack:
    def __init__(self):
        self.stack = []

    def push_order(self, order):
        self.stack.append(order)

    def pop_order(self):
        if self.stack:
            order = self.stack.pop()
            print(f"Order Prepared: {order}")
        else:
            print("No orders to prepare.")

    def display_stack(self):
        if self.stack:
            print("Orders in preparation:")
            for order in self.stack:
                print(order)
        else:
            print("No orders in preparation.")

def main():
    menu = MenuLinkedList()
    menu.add_item("Pizza", 100, True)  
    menu.add_item("Burger", 80, True)  
    menu.add_item("Pasta", 200, False)  
    menu.add_item("Salad", 200, True)   

    print("Menu Items:")
    menu.display_menu()

    order_queue = OrderQueue()
    order_stack = OrderStack()

    order_queue.add_order("Pizza")
    order_queue.add_order("Burger")
    order_queue.add_order("Salad")

    print("\nOrder Queue:")
    order_queue.display_orders()

    order_stack.push_order(order_queue.orders[0])
    order_stack.push_order(order_queue.orders[1])
    order_stack.push_order(order_queue.orders[2])

    print("\nOrder Stack (Orders in preparation):")
    order_stack.display_stack()

    order_stack.pop_order()
    order_stack.pop_order()
    order_stack.pop_order()

    order_queue.process_order()

if __name__ == "__main__":
    main()
