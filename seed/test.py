from matches_data import matches_data
from estadios import estadios

estadios1 = []
estadios2 = []
faltando = []

for i in range(len(matches_data)):
  estadios1.append(matches_data[i][8])

for estadio in estadios:
  estadios2.append(estadio[0])

for estadio in estadios1:
  if estadio not in estadios2:
    faltando.append(estadio)
faltando = list(dict.fromkeys(faltando))
print(faltando)
print(len(faltando))
[3938, 1086, 1095, 2236, 2228, 6876, 12937, 8974, 1385, 11811, 1097, 5987, 3011, 5975, 5572, 2242]