import pdb

from models.action import Action
from models.deed import Deed
from models.user import User

import repositories.user_repository as user_repo
import repositories.action_repository as action_repo
import repositories.deed_repository as deed_repo




user1 = User("Nathan", "Pianu", 1000)

user1.total_daily = 100
user1.total_overall = 1100
user_repo.save(user1)

user2 = User("Lauren", "Fraser", 1000)

user2.total_daily = 250
user2.total_overall = 2100
user_repo.save(user2)

user3 = User("Steven", "Swan", 1000)

user3.total_daily = 50
user3.total_overall = 500
user_repo.save(user3)

user4 = User("Ghandi", "Bhuda", 1000)

user4.total_daily = 2000
user4.total_overall = 5000000
user_repo.save(user4)


print(user_repo.select_all())

user2.total_daily = 500
user_repo.update(user2)

print(user_repo.select(2))

action1 = Action("Greet Stranger","Say hello to a stranger and ask how they are.","Social", 100)
action_repo.save(action1)

action2 = Action("pick up trash","Pick up a single piece of trash and dispose of it correctly","Enviromental", 100)
action_repo.save(action2)

print(action_repo.select_all())
print(action_repo.select(2))

action2.value =150
action_repo.update(action2)

deed1 = Deed(user1,action1,"14/08/2021")
deed_repo.save(deed1)

deed2 = Deed(user2,action2,"14/08/2021")
deed_repo.save(deed2)

deed2.date = "16/08/2021"
deed_repo.update(deed2)

print(action_repo.select_all())
print(action_repo.select(2))


pdb.set_trace()
