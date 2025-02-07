from referees_data import referees_data
from insert_referee_data import insert_referee_data
from get_referee_data import get_referee_data
from referees_id import referees_id

# for index, referee_id in enumerate(referees_id, start=1):
#   referee_data = get_referee_data(referee_id)
#   if referee_data:
#     print(f"({index}/{len(referees_id)}) Inserindo dados do arbitro no banco de dados...")
#     referee_data = json.loads(json.dumps(referee_data, ensure_ascii=False))
#     insert_referee_data(referee_data)
#   else:
#     print("Não foi possível obter os dados do arbitro.")
insert_referee_data(referees_data)