from matches_data import matches_data
from insert_match_data import insert_match_data
from get_matches_id import get_matches_id
from get_match_data import get_match_data
from matches_id import matches_id
from competitions_id import competitions_id

# matches_id = get_matches_id("BRA1", 2023)
# for index, match_id in enumerate(matches_id, start=1):
#   match_data = get_match_data(match_id)
#   if match_data:
#     insert_match_data(match_data)
#   else:
#     print("Não foi possível obter os dados do jogo.")
insert_match_data(matches_data)