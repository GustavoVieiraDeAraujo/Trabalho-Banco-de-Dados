CREATE TABLE Competicao (
  id VARCHAR(10) PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  ano INT,
  confederacao VARCHAR(255),
  imagemURL VARCHAR(255),
  divisao VARCHAR(255)
);

SELECT * FROM Competicao;
TRUNCATE Competicao;
DROP TABLE Competicao;