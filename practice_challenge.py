# Complete the 'subscription_summary' function below.
from __future__ import print_function

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
    try:
        validate_inputs(months_subscribed, ad_free_months, video_on_demand_purchases)
    except BaseException as e:
        print(e)
        return

    accounts = make_accounts(months_subscribed, ad_free_months, video_on_demand_purchases)
    for account in accounts:
        account.calculate_costs()
        account.print_account()

    summarize_accounts(accounts)

def validate_inputs(months_subscribed, ad_free_months, video_on_demand_purchases):
    for x, x, x in zip(months_subscribed, ad_free_months, video_on_demand_purchases):
        if x < 0:
            raise ValueError("An input appears to be negative. Please check that all inputs are positive integers.")

    if not len(months_subscribed) == len(ad_free_months) == len(video_on_demand_purchases):  # We make sure each list is identical in length.
        raise ValueError("There is missing data. Please check that each list have the same number of inputs and try again.")
    
    if not all(isinstance(x,int) for x, x, x in zip(months_subscribed, ad_free_months, video_on_demand_purchases)): # We make sure each list has valid inputs.
            raise ValueError ("There is an error with an input. Please check that all inputs are valid integers.")

def make_accounts(months_subscribed, ad_free_months, video_on_demand_purchases):
    stored_accounts_temp = [] # A tuple to store information given.
    account_number = 1 

    for i in range(len(months_subscribed)): 
        account = Account(months_subscribed[i], ad_free_months[i], video_on_demand_purchases[i], account_number)
        stored_accounts_temp.append(account)
        account_number += 1 # Each loop increases account number for naming purposes.           
    return stored_accounts_temp

class Account:
    """Creating a way to represent an account."""

    def __init__(self, individual_months_subscribed, individual_adfree_costs, individual_vod_purchases, account_number):
        self.individual_months_subscribed = individual_months_subscribed
        self.individual_adfree_costs = individual_adfree_costs
        self.individual_vod_purchases = individual_vod_purchases
        self.account_number = account_number
            
    def calculate_costs(self):
        """
        Generates the costs for each factor within each individual account. 
        Returns 4 values for the account.
        """
        monthly_cost = 7.00
        single_bundle_cost = 18.00
        single_adfree_cost = 2.00
        vod_cost = 27.99

        total_monthly_cost = (self.individual_months_subscribed % 3) * monthly_cost
        total_bundle_cost = ((self.individual_months_subscribed - (self.individual_months_subscribed % 3)) / 3) * single_bundle_cost
        final_subscribed_cost = total_monthly_cost + total_bundle_cost

        total_adfree_cost = self.individual_adfree_costs * single_adfree_cost
        total_vod_cost = self.individual_vod_purchases * vod_cost
        
        final_account_cost = (final_subscribed_cost + total_adfree_cost + total_vod_cost)

        self.calculated_costs_tuple = (final_account_cost, final_subscribed_cost, total_adfree_cost, total_vod_cost)

    def print_account(self):            
        print("Account", self.account_number, "made",'${:,.2f}'.format(self.calculated_costs_tuple[0]), "total")
        print('>>> ${:,.2f}'.format(self.calculated_costs_tuple[1]), "from monthly subscription fees")
        print('>>> ${:,.2f}'.format(self.calculated_costs_tuple[2]), "from Ad-free upgrades")
        print('>>> ${:,.2f}'.format(self.calculated_costs_tuple[3]), "from Video on Demand purchases\n")

def summarize_accounts(accounts):
    account_names = []
    account_earnings = []
    premium_earnings = 0
    
    for x in accounts:
        account_names.append(x.account_number)
        account_earnings.append(x.calculated_costs_tuple[0])
        premium_earnings = premium_earnings + (x.calculated_costs_tuple[2] + x.calculated_costs_tuple[3])

    account_earnings_total = sum(account_earnings)
    
    accounts_dict = dict(zip(account_names, account_earnings))
    top_account_value = max(accounts_dict.values())

    top_accounts_list = []

    top_accounts = list(key for key, value in accounts_dict.items() if value == top_account_value)
    for x in top_accounts:
        top_accounts_list.append("#" + str(x))

    print("Combined all accounts made", '${:,.2f}'.format(account_earnings_total), "total")
    print("Premium content (Ad-free watching and Video on Demand) made", '${:,.2f}'.format(premium_earnings), "total\n")
    print('${:,.2f}'.format(top_account_value), "was the most earned by any single account")
    if len(top_accounts_list) == 1:
        print("The account that earned the most was:", *top_accounts_list)
    else:
        print("The accounts that earned the most were: ", end='')
        print(*top_accounts_list, sep = ", ")

#Testing the method:
months_subscribed = (10, 2, 3, 9, 1, 5, 4, 3)
ad_free_months = (2, 3, 1, 3, 4, 30, 5, 7)
video_on_demand_purchases = (3, 1, 7, 9, 9, 6, 3, 5)

subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases)