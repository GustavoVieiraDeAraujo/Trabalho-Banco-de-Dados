CREATE TABLE Jogador_Titulo (
  id SERIAL PRIMARY KEY,
  id_jogador INT,
  id_titulo INT,
  CONSTRAINT fk_jogador FOREIGN KEY (id_jogador) REFERENCES Jogador(id),
  CONSTRAINT fk_titulo FOREIGN KEY (id_titulo) REFERENCES Titulo(id)
);