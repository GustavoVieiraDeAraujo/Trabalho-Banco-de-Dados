CREATE TABLE Jogador (
  id INTEGER PRIMARY KEY,
  nome VARCHAR(255),
  apelido VARCHAR(255),
  data_nascimento DATE,
  nacionalidade VARCHAR(255),
  imagemURL VARCHAR(255)
  posicao VARCHAR(255),
  altura DOUBLE PRECISION,
  pe_dominante VARCHAR(10) CHECK (pe_dominante IN ('Esquerda', 'Direita', 'Ambos')),
  valor_mercado MONEY,
  cidade_nascimento VARCHAR(255)
  numero_camisa INTEGER,
  agente VARCHAR(255)
  patrocinador VARCHAR(255),
  redes_sociais VARCHAR(255),
  contrato_incio DATE,
  contrato_fim DATE,
  id_time INT,
  CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES Time(id),
);