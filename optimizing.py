def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
    print("Welcome to the Ada+ Account Dashboard")
    print()
    
    # Write your code here
    # validate inputs given
    try:
        validate_inputs(months_subscribed, ad_free_months, video_on_demand_purchases)
    except BaseException as error:
        print(error)
        return
    
    run_report()

def validate_inputs(months_subscribed, ad_free_months, video_on_demand_purchases):
    # Maybe to allow this more inputs, this function takes in one parameter, which is a list 
    # of lists (where each list is one type of customer purchase)
    # then we can search through each one and validate each list

    # We make sure each list is identical in length (no customer is missing data).
    all_inputs = zip(months_subscribed, ad_free_months, video_on_demand_purchases)

    if not len(months_subscribed) == len(ad_free_months) == len(video_on_demand_purchases): 
        raise ValueError("Please check that each list has the same number of inputs.") 

    for x, y, z in all_inputs:
        # We make sure each list has whole numerical inputs.
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
            raise ValueError("Please check that all inputs are valid integers.")
        # We make sure there are no negative inputs.
        if x < 0 or y < 0 or z < 0:
            raise ValueError("Please check that all inputs are positive integers.")

def run_report():    
    customers_dict = make_customers_dict(months_subscribed, ad_free_months, video_on_demand_purchases)
    customer_accounts = generate_accounts(customers_dict)
    calculate_and_print_account_reports(customer_accounts)
    
    end_summary = calculate_end_summary(customer_accounts)
    print_end_summary(end_summary)
    
def make_customers_dict(months_subscribed, ad_free_months, video_on_demand_purchases):
    customers_dict = {}

    customer_purchases = list(zip(months_subscribed, ad_free_months, video_on_demand_purchases))
    # Creates dictionary where KEY is customer_id and VALUE is list of customer_purchases
    for customer_id in range(len(customer_purchases)):
        customers_dict[customer_id+1] = customer_purchases[customer_id]

    return customers_dict

def generate_accounts(customers_dict):
    #Passes customer information through Account class and stores & returns all customers account info
    #Stored as a list of references to each account
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
    #Creates a represention each customer's account
    def __init__(self, customer_id, customer_purchases):
        self.customer_id = customer_id

        #Break the customer purchases into their respective category
        self.months_subscribed = customer_purchases[0]
        self.ad_free_months = customer_purchases[1]
        self.video_on_demand_purchases = customer_purchases[2]

    def calculate_customer_costs(self):
        monthly_cost = 7.00
        bundle = 18.00
        single_adfree_cost = 2.00
        vod_cost = 27.99

        # Automatically bundles deliveries if possible
        customer_months_ordered = self.months_subscribed % 3
        customer_bundle_order = (self.months_subscribed - customer_months_ordered) / 3

        #Customer's cost of single and/or bundle deliveries
        total_monthly_cost = customer_months_ordered * monthly_cost
        total_bundle_orders = customer_bundle_order * bundle

        # Total costs of each purchase category
        self.total_subscription_fees = total_monthly_cost + total_bundle_orders
        self.adfree_cost = self.ad_free_months * single_adfree_cost
        self.total_vod_cost = self.video_on_demand_purchases * vod_cost

        # Total overall spent by customer
        self.customer_spending = self.total_subscription_fees + self.adfree_cost + self.total_vod_cost

    def print_customer_summary(self):
        customer_total = '${:,.2f}'.format(self.customer_spending)
        customer_subscriptions = '${:,.2f}'.format(self.total_subscription_fees)
        customer_adfree = '${:,.2f}'.format(self.adfree_cost)
        customer_vod = '${:,.2f}'.format(self.total_vod_cost)

        print(f"Account {self.customer_id} made {customer_total} total")
        print(f">>> {customer_subscriptions} from monthly subscription fees")
        print(f">>> {customer_adfree} from Ad-free upgrades")
        print(f">>> {customer_vod} from Video on Demand purchases\n")

    def get_end_calculation(self):
        '''Returns relevant values we use to calculate the end of summary report'''
        self.adfree_and_vod =  self.adfree_cost + self.total_vod_cost
        spending_breakdown = ['#'+ str(self.customer_id), self.customer_spending, self.adfree_and_vod]
        
        return spending_breakdown

def calculate_end_summary(accounts):
    accounts_total_spending = {}
    accounts_total_adfree_vod = {}

    for account in accounts:
        end_calculation = account.get_end_calculation()
        # end calculation returns 3 values per customer account
        customer_id = end_calculation[0]
        total_spending = end_calculation[1]
        adfree_vod = end_calculation[2]
        # add customer_id and relevant value to respective dictionaries
        accounts_total_spending[customer_id] = total_spending
        accounts_total_adfree_vod[customer_id] = adfree_vod
    
    total_profit = 0
    for customer_id, total_spent in accounts_total_spending.items():
        total_profit += float(total_spent)

    adfree_vod_profit = 0    
    for customer_id, adfree_vod_spent in accounts_total_adfree_vod.items():
        adfree_vod_profit += float(adfree_vod_spent)
    
    top_account_value = max(accounts_total_spending.values())
    top_accounts = list(customer_id for customer_id, total_spent in accounts_total_spending.items() if total_spent == top_account_value)

    return total_profit, adfree_vod_profit, top_account_value, top_accounts

def print_end_summary(end_summary):
    total_profit = '${:,.2f}'.format(end_summary[0])
    adfree_vod_profit = '${:,.2f}'.format(end_summary[1])
    top_account_value = '${:,.2f}'.format(end_summary[2])
    top_accounts = end_summary[3]

    print(f"Combined all accounts made {total_profit} total")
    print(f"Premium content (Ad-free watching and Video on Demand) made {adfree_vod_profit} total\n")
    print(f"{top_account_value} was the most earned by any single account")
    if len(top_accounts) == 1:
        print("The account that earned the most was:", *top_accounts)
    else:
        print("The accounts that earned the most were: ", end='')
        print(*top_accounts, sep = ", ")

months_subscribed = (10, 2, 3)
ad_free_months = (2, 3, 1)
video_on_demand_purchases = (3, 1, 7)

subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases)