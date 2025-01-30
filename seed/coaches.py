from get_coaches_id import get_coaches_id
from get_coach_data import get_coach_data
from insert_coach_data import insert_coach_data

coaches_id = get_coaches_id('BRA1')
for index, coach_id in enumerate(coaches_id, start=1):
  coach_data = get_coach_data(coach_id)
  if coach_data:
    print(f"({index}/{len(coaches_id)}) Inserindo dados do tecnico no banco de dados...")
    insert_coach_data(coach_data)
  else:
    print("Não foi possível obter os dados do tecnico.")