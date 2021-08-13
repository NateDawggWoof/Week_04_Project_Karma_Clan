import pdb

from models.action import Action
from models.deed import Deed
from models.user import User

import repositories.user_repository as user_repo




user1 = User("Nathan Pianu", 1000)

user1.total_daily = 100
user1.total_overall = 1100
user_repo.save(user1)

pdb.set_trace()
