from get_clubs_id import get_clubs_id
from get_players_id import get_players_id
from get_player_data import get_player_data
from insert_player_data import insert_player_data

clubs_id = get_clubs_id('BRA1')
players_id = get_players_id(clubs_id)
dados = []
for index, player_id in enumerate(players_id, start=1):
  player_data = get_player_data(player_id)
  dados.append(player_data)
  if player_data:
    print(f"({index}/{len(players_id)}) Inserindo dados do jogador no banco de dados...")
    insert_player_data(player_data)
  else:
    print("Não foi possível obter os dados do jogador.")
print(dados)