class User:
    def __init__(self,name_first,name_last, goal_daily,id =None):
        self.name_first = name_first
        self.name_last = name_last
        self.goal_daily = goal_daily
        self.id = id
        self.total_daily = 0
        self.total_overall = 0