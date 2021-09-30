def delivery_summary(deliveries_ordered, rush_deliveries, meals_purchased):
    """
    Parameters:
      deliveries_ordered: How many deliveries each customer ordered.
      rush_deliveries: How many deliveries each customer rushed.
      meals_purchased: How many total meals the customer purchased.
    """
    print("Welcome to the Ada Meal Delivery Dashboard")
    print()
    
    # Write your code here
    # validate inputs given
    try:
        validate_inputs(deliveries_ordered, rush_deliveries, meals_purchased)
    except BaseException as error:
        print(error)
        return
    
    run_report()

def validate_inputs(deliveries_ordered, rush_deliveries, meals_purchased):
    # We make sure each list is identical in length (no customer is missing data).
    if not len(deliveries_ordered) == len(rush_deliveries) == len(meals_purchased): 
        raise ValueError("Please check that each list has the same number of inputs.") 

    for x, y, z in zip(deliveries_ordered, rush_deliveries, meals_purchased):
        # We make sure each list has whole numerical inputs.
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
            raise ValueError("Please check that all inputs are valid integers.")
        # We make sure there are no negative inputs.
        if x < 0 or y < 0 or z < 0:
            raise ValueError("Please check that all inputs are positive integers.")

def run_report():    
    customers_dict = make_customers_dict(deliveries_ordered, rush_deliveries, meals_purchased)
    customers = generate_accounts(customers_dict)
    calculate_and_print_account_reports(customers)
    
    end_summary = calculate_end_summary(customers)
    print_end_summary(end_summary)
    
def make_customers_dict(deliveries_ordered, rush_deliveries, meals_purchased):
    num_of_customers = len(deliveries_ordered)
    customers_dict = {}
    # Creates dictionary where KEY is customer_id and VALUE is list of customer_purchases
    for customer_id in range(num_of_customers):
        customers_dict[customer_id+1] = [deliveries_ordered[customer_id], rush_deliveries[customer_id], meals_purchased[customer_id]]

    return customers_dict

def generate_accounts(customers_dict):
    #Passes customer information through Account class and stores & returns all customers account info
    all_accounts = []
    
    for customer_id, customer_purchases in customers_dict.items():
        account = Account(customer_id, customer_purchases)
        all_accounts.append(account)

    return all_accounts

def calculate_and_print_account_reports(all_accounts):
    for account in all_accounts:
        account.calculate_customer_costs()
        account.print_customer_summary()

class Account:
    '''Creates a represention each customer's account'''
    def __init__(self, customer_id, customer_purchases):
        self.customer_id = customer_id

        #Break the customer purchases into their respective category
        self.deliveries_ordered = customer_purchases[0]
        self.rush_deliveries = customer_purchases[1]
        self.meals_purchased = customer_purchases[2]

    def calculate_customer_costs(self):
        '''Calculates the cost of each customer purchase.'''
        single_delivery = 7.25
        bundle = 60.00
        rush = 2.00
        meal = 12.50

        # Automatically bundles deliveries if possible
        customer_single_order = self.deliveries_ordered % 10
        customer_bundle_order = (self.deliveries_ordered - customer_single_order) / 10

        #Customer's cost of single and/or bundle deliveries
        total_single_orders = customer_single_order * single_delivery
        total_bundle_orders = customer_bundle_order * bundle

        # Total costs of each purchase category
        self.total_delivery_fees = total_single_orders + total_bundle_orders
        self.total_rushes = self.rush_deliveries * rush
        self.total_meals = self.meals_purchased * meal

        # Total overall spent by customer
        self.customer_spending = self.total_delivery_fees + self.total_rushes + self.total_meals

    def print_customer_summary(self):
        customer_total = '${:.2f}'.format(self.customer_spending)
        customer_delivery = '${:.2f}'.format(self.total_delivery_fees)
        customer_rushes = '${:.2f}'.format(self.total_rushes)
        customer_meals = '${:.2f}'.format(self.total_meals)

        print(f"Customer {self.customer_id} paid {customer_total} total")
        print(f">>> {customer_delivery} in delivery fees")
        print(f">>> {customer_rushes} in rush delivery fees")
        print(f">>> {customer_meals} in meal fees\n")

    def get_end_calculation(self):
        '''Returns relevant values we use to calculate the end of summary report'''
        self.delivery_and_rush = self.total_delivery_fees + self.total_rushes
        spending_breakdown = ['#'+ str(self.customer_id), self.customer_spending, self.delivery_and_rush]
        
        return spending_breakdown

def calculate_end_summary(accounts):
    accounts_total_spending = {}
    accounts_total_delivery = {}

    for account in accounts:
        end_calculation = account.get_end_calculation()

        customer_id_index = 0
        total_spending_index = 1
        total_delivery_index = 2
        accounts_total_spending[end_calculation[customer_id_index]] = end_calculation[total_spending_index]
        accounts_total_delivery[end_calculation[customer_id_index]] = end_calculation[total_delivery_index]
    
    total_profit = 0
    for customer_id, total_spent in accounts_total_spending.items():
        total_profit += float(total_spent)

    delivery_profit = 0    
    for customer_id, delivery_spent in accounts_total_delivery.items():
        delivery_profit += float(delivery_spent)
    
    top_account_value = max(accounts_total_spending.values())
    top_accounts = list(customer_id for customer_id, total_spent in accounts_total_spending.items() if total_spent == top_account_value)

    return total_profit, delivery_profit, top_account_value, top_accounts

def print_end_summary(end_summary):
    total_profit = '${:.2f}'.format(end_summary[0])
    delivery_profit = '${:.2f}'.format(end_summary[1])
    top_account_value = '${:.2f}'.format(end_summary[2])
    top_accounts = end_summary[3]

    print(f"Combined all customers paid {total_profit} total")
    print(f"Delivery fees (standard and Rush Delivery) were {delivery_profit} total\n")
    print(f"{top_account_value} was the most paid by any single customer")
    print("The customer(s) that paid the most were: ", end="")
    print(*top_accounts, sep=", ")

deliveries_ordered = (10, 2, 3, 9, 1, 5, 4, 3)
rush_deliveries = (2, 3, 1, 3, 4, 30, 5, 7)
meals_purchased = (3, 1, 7, 9, 9, 6, 3, 5)



delivery_summary(deliveries_ordered, rush_deliveries, meals_purchased)