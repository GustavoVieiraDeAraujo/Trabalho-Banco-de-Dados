from get_competition_id import get_competition_id
from get_clubs_id import get_clubs_id
from get_players_id import get_players_id
from get_player_data import get_player_data
from insert_player_data import insert_player_data

competition_name = input("Digite o nome da competição: ")
competition_id = get_competition_id(competition_name)
clubs_id = get_clubs_id(competition_id)
players_id = get_players_id(clubs_id)
for index, player_id in enumerate(players_id, start=1):
  player_data = get_player_data(player_id)
  if player_data:
    print(f"({index}/{len(players_id)}) Inserindo dados do jogador no banco de dados...")
    insert_player_data(player_data)
  else:
    print("Não foi possível obter os dados do jogador.")