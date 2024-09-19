# Edit the snippet on the following slide to include two or more
# parameters, a running order count that updates when the function
# is called and change the .format method to f string.

# order_count = 0

# def take_order (topping) :
#     global order_count
#     print("Pizzawith{}".format(topping))
#     order_count += 1

# take_order ("pineapple" )

order_count = 0

def take_order (topping1, topping2, topping3) :
    global order_count
    print(f'Pizza with {topping1} ,{topping2}, {topping3}')
    order_count += 1
    print(f'Order count is {order_count}')

take_order ("Peppers","Red Onions","extra Cheese" )
take_order ("Pineapple","Sweetcorn","extra Cheese" )
take_order ("Pepperoni","Red Onions","extra Cheese" )