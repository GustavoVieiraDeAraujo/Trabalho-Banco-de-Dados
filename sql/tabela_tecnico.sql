CREATE TABLE Tecnico (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(255),
  apelido VARCHAR(255),
  data_nascimento DATE,
  nacionalidade VARCHAR(255),
  imagemURL VARCHAR(255),
  contrato_inicio DATE,
  contrato_fim DATE,
  cidade_nascimento VARCHAR(255),
  id_time INT,
  CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES Time(id)
)

SELECT * FROM Tecnico;
TRUNCATE Tecnico;
DROP TABLE Tecnico;