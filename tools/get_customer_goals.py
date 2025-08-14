import pandas as pd

from agents import function_tool
from utils import DataLoader

@function_tool
def get_customer_goals(customer_id:str):
    data_loader = DataLoader()
    config = data_loader.load_config()
    """
       We get the customer's goals to evaluate the buy/sell opportunity.
    """
    stockfile_dir = config['PORTFOLIO']['portfolio']
    excel_file = f"{stockfile_dir}"
    sheet_name = 'goals'
    data_goals = data_loader.load_data(excel_file,sheet_name)
    
    data_goals = data_goals.loc[data_goals['CustomerId']==int(customer_id)]
    customer_goals = data_goals.to_dict(orient='records')
    
    customer_goals_struct = []
    for goal in customer_goals:
        dict_goal = {}
        dict_goal["CustomerGoal"] = goal["GoalName"]
        dict_goal["GoalDueInYears"] = goal["GoalDueInYears"]
        dict_goal["GoalAccomplishmentMinimumProbabliy"] = goal["ProbablityOfAchieving"]
        dict_goal["GoalAmount"] = goal["GoalAmount"]

        customer_goals_struct.append(dict_goal)

    return_dict = {"CustomerGoals":customer_goals_struct}
    
    return return_dict