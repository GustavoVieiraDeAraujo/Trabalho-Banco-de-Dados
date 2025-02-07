from clubs_data import clubs_data
from insert_club_data import insert_club_data
from get_clubs_id import get_clubs_id
from get_club_data import get_club_data
from competitions_id import competitions_id
from clubs_id import clubs_id

# for index, club_id in enumerate(clubs_id, start=1):
#   club_data = get_club_data(club_id)
#   if club_data:
#     print(f"({index}/{len(clubs_id)}) Inserindo dados do clube no banco de dados...")
#     insert_club_data(club_data)
#   else:
#     print("Não foi possível obter os dados do clube.")
insert_club_data(clubs_data)