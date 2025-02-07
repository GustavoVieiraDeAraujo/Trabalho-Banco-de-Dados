from competitions_data import competitions_data
from insert_competition_data import insert_competition_data
from get_competition_data import get_competition_data
from competitions_id import competitions_id

# for index, competition_id in enumerate(competitions_id, start=1):
#   competition_data = get_competition_data(competition_id)
#   if competition_data:
#     print(f"({index}/{len(competitions_id)}) Inserindo dados da competicao no banco de dados...")
#     competition_data = json.loads(json.dumps(competition_data, ensure_ascii=False))
#     insert_competition_data(competition_data)
#   else:
#     print("Não foi possível obter os dados da competicao.")
insert_competition_data(competitions_data)