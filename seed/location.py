from get_clubs_id import get_clubs_id
from get_club_location import get_club_location
from insert_location_data import insert_location_data

competition_id = 'BRA1'
locations = []
clubs_id = get_clubs_id(competition_id)
for index, club_id in enumerate(clubs_id, start=1):
  club_location_data = get_club_location(club_id)
  city = club_location_data.get("data", {}).get("mainFacts", {}).get("city")
  if city:
    clean_city = city.split(",")[0]
    clean_city = clean_city.split("-")[0].strip() 
    clean_city = clean_city.title()
    if city not in locations:
      locations.append(clean_city)
for index, location in enumerate(locations, start = 1):
  if location:
    print(f"({index}/{len(locations)}) Inserindo dados da localizacao no banco de dados...")
    insert_location_data(location)
  else:
    print("Não foi possível obter os dados da localizacao.")