from players_data import players_data
from insert_player_data import insert_player_data
from get_clubs_id import get_clubs_id
from get_players_id import get_players_id
from get_player_data import get_player_data
from competitions_id import competitions_id
from clubs_id import clubs_id
from players_id import players_id

# clubs_id = get_clubs_id('BRA1')
# players_id = get_players_id(clubs_id)
# for index, player_id in enumerate(players_id, start=1):
#   player_data = get_player_data(player_id)
#   if player_data:
#     insert_player_data(player_data)
#   else:
#     print("Não foi possível obter os dados do jogador.")
insert_player_data(players_data)