CREATE TABLE Estatistica (
  id SERIAL PRIMARY KEY,
  jogos INT,
  gols INT,
  assistencias INT,
  vermelhos INT,
  amarelos INT,
  minutos INT,
  id_jogador INT,
  CONSTRAINT fk_jogador FOREIGN KEY (id_jogador) REFERENCES Jogador(id)
)

SELECT * FROM Estatistica;
TRUNCATE Estatistica;
DROP TABLE Estatistica;