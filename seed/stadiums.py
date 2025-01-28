from get_clubs_id import get_clubs_id
from get_club_stadium import get_club_stadium
from insert_stadium_data import insert_stadium_data

competition_id = 'BRA1'
stadiums = []
stadiums_name = []
clubs_id = get_clubs_id(competition_id)
for index, club_id in enumerate(clubs_id, start=1):
  club_stadium_data = get_club_stadium(club_id)
  stadium = club_stadium_data.get("data", {}).get("stadium", {})
  stadium_name = club_stadium_data.get("data", {}).get("stadium", {}).get("name")
  if stadium_name not in stadiums_name:
    stadiums_name.append(stadium_name)
    stadiums.append(stadium)
for index, stadium in enumerate(stadiums, start = 1):
  if stadium:
    print(f"({index}/{len(stadiums)}) Inserindo dados do estadio no banco de dados...")
    insert_stadium_data(stadium)
  else:
    print("Não foi possível obter os dados do estadio.")