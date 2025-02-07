from locations_data import locations_data
from insert_location_data import insert_location_data
from get_clubs_id import get_clubs_id
from get_club_location import get_club_location
from competitions_id import competitions_id
from clubs_id import clubs_id

# locations = []
# for index, club_id in enumerate(clubs_id, start=1):
#   club_location_data = get_club_location(club_id)
#   city = club_location_data.get("data", {}).get("mainFacts", {}).get("city")
#   if city:
#     clean_city = city.split(",")[0]
#     clean_city = clean_city.split("-")[0].strip() 
#     clean_city = clean_city.title()
#     if city not in locations:
#       locations.append(clean_city)
# locations = list(dict.fromkeys(locations))
# for index, location in enumerate(locations, start = 1):
#   if location:
#     print(f"({index}/{len(locations)}) Inserindo dados da localizacao no banco de dados...")
#     insert_location_data(location)
#   else:
#     print("Não foi possível obter os dados da localizacao.")
insert_location_data(locations_data)