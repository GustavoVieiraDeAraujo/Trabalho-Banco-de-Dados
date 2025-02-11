CREATE TABLE Estadio (
  id INTEGER PRIMARY KEY,
  data_fundacao INT,
  nome VARCHAR(255),
  capacidade INT,
  id_localizacao INT,
  CONSTRAINT fk_localizacao FOREIGN KEY (id_localizacao) REFERENCES Localizacao(id)
);