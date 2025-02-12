import subprocess

arquivos = [
  r"C:\Users\felip\Documents\TrabalhoBD\banco\seed\referees.py", 
  r"C:\Users\felip\Documents\TrabalhoBD\banco\seed\competitions.py", 
  r"C:\Users\felip\Documents\TrabalhoBD\banco\seed\location.py", 
  r"C:\Users\felip\Documents\TrabalhoBD\banco\seed\stadiums.py", 
  r"C:\Users\felip\Documents\TrabalhoBD\banco\seed\clubs.py", 
  r"C:\Users\felip\Documents\TrabalhoBD\banco\seed\location.py", 
  r"C:\Users\felip\Documents\TrabalhoBD\banco\seed\players.py", 
  r"C:\Users\felip\Documents\TrabalhoBD\banco\seed\stats.py", 
  r"C:\Users\felip\Documents\TrabalhoBD\banco\seed\coaches.py", 
  r"C:\Users\felip\Documents\TrabalhoBD\banco\seed\achievements.py"
]

for arquivo in arquivos:
  resultado = subprocess.run(["python", arquivo], capture_output=True, text=True)