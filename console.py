import pdb

from models.action import Action
from models.deed import Deed
from models.user import User

import repositories.user_repository as user_repo




user1 = User("Nathan Pianu", 1000)

user1.total_daily = 100
user1.total_overall = 1100
user_repo.save(user1)

user2 = User("Lauren Fraser", 1000)

user2.total_daily = 250
user2.total_overall = 2100
user_repo.save(user2)

print(user_repo.select_all())

print(user_repo.select(2))



pdb.set_trace()
