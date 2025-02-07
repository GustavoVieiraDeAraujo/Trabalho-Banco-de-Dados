from players_stats import players_stats
from insert_players_stats import insert_players_stats
from get_clubs_id import get_clubs_id
from get_players_id import get_players_id
from get_player_stats import get_player_stats
from prepare_player_stats import prepare_player_stats
from competitions_id import competitions_id
from clubs_id import clubs_id
from players_id import players_id

# clubs_id = get_clubs_id('BRA1')
# players_id = get_players_id(clubs_id)
# for index, player_id in enumerate(players_id, start=1):
#   player_stats_general = None
#   player_stats_summary = None
#   player_stats_general = get_player_stats(player_id)
#   if player_stats_general:
#     player_stats_summary = prepare_player_stats(player_stats_general)
#     player_stats_summary["idPlayer"] = player_id
#   if player_stats_summary:
#     insert_player_stats(player_stats_summary)
#   else:
#     print(f"({index}/{len(players_id)}) Não foi possível obter os dados da estatística...")
#     continue
insert_players_stats(players_stats)