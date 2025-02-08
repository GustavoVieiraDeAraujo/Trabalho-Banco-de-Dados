CREATE TABLE Arbitro (
  id INTEGER PRIMARY KEY,
  apelido VARCHAR(255),
  nome VARCHAR(255),
  data_nascimento DATE,
  nacionalidade VARCHAR(255),
  imagemURL VARCHAR(255),
  contrato_inicio DATE
)

SELECT * FROM Arbitro;
TRUNCATE Arbitro;
DROP TABTLE Arbitro;