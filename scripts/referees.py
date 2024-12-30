from get_referee_data import get_referee_data
from insert_referee_data import insert_referee_data

referees_id = [ "48285", "37656", "47698", "3762", "16466", "1576", "45958", "5643", "42130", "9076",  "6184", "43058", "35943", "43029", "1133", "38902", "42395", "1487", "37002", "42813",  "4334", "28500", "42801", "23502", "23498", "42667", "31295", "31799", "42296", "42521", "46927", "48578", "64645", "68981", "37071", "42796", "42871", "47610", "63817"]

for index, referee_id in enumerate(referees_id, start=1):
  referee_data = get_referee_data(referee_id)
  if referee_data:
    print(f"({index}/{len(referees_id)}) Inserindo dados do arbitro no banco de dados...")
    insert_referee_data(referee_data)
  else:
    print("Não foi possível obter os dados do arbitro.")