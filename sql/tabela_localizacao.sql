CREATE TABLE Localizacao (
    id SERIAL PRIMARY KEY,
    continente VARCHAR(255),
    pais VARCHAR(255),
    regiao VARCHAR(255),
    estado VARCHAR(255),
    cidade VARCHAR(255)
);