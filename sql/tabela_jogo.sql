CREATE TABLE Jogo (
  id INTEGER PRIMARY KEY,
  data DATE,
  horario TEXT,
  publico INT,
  rodada INT,
  gols_mandante INT,
  gols_visitante INT,
  id_competicao INT,	
  id_estadio INT,
  id_arbitro INT,
  CONSTRAINT fk_estadio FOREIGN KEY (id_estadio) REFERENCES Estadio(id),
  CONSTRAINT fk_arbitro FOREIGN KEY (id_arbitro) REFERENCES Arbitro(id),
  CONSTRAINT fk_competicao FOREIGN KEY (id_competicao) REFERENCES Competicao(id)
);