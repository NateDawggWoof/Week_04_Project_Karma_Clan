class User:
    def __init__(self,name, goal_daily,id =None):
        self.name = name
        self.goal_daily = goal_daily
        self.id = id
        self.total_daily = 0
        self.total_overall = 0