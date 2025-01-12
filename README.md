# Sobre o projeto

Este projeto de Banco de Dados foi desenvolvido para atender às [especificações](./pdf/especificacao_projeto.pdf) da disciplina Banco de Dados do Departamento de Ciência da Computação da Universidade de Brasília. O objetivo principal é criar um sistema funcional com um banco de dados relacional, utilizando boas práticas de modelagem e implementação.

# Participantes

- FELIPE COSTA DE SOUSA - 211055236
- GUSTAVO VIEIRA DE ARAÚJO - 211068440
- ADRIELLY VITORIA COSTA DE LIMA - 231018973
- PEDRO RODRIGUES DIOGENES MACEDO - 211042739

# Gerar SQL do schema do banco de dados

```python
# No Windows
python ./concatenate_sql/concatenar_sql_schema_bd.py

# No Linux ou Mac
python3 ./concatenate_sql/concatenar_sql_schema_bd.py
```

# Cardinalidade e Participação das Entidades

## 1. Relacionamento entre Jogo e Competição

-   **Cardinalidade:**
    -   Uma competição → vários jogos (1:N).
    -   Um jogo → uma competição (N:1).
-   **Participação:**
    -   **Jogo:** Obrigatório (sempre tem uma competição).
    -   **Competição:** Opcional (pode estar vinculado a um jogo, ou não).

## 2. Relacionamento entre Jogo e Árbitro

-   **Cardinalidade:**
    -   Um jogo → um árbitro (1:1).
    -   Um árbitro → vários jogos (N:1).
-   **Participação:**
    -   **Jogo:** Obrigatória (sempre tem um árbitro).
    -   **Árbitro:** Opcional (pode estar vinculado a um jogo, ou não).

## 3. Relacionamento entre Jogo e Estádio

-   **Cardinalidade:**
    -   Um jogo → um estádio (1:1).
    -   Um estádio → vários jogos (N:1).
-   **Participação:**
    -   **Jogo:** Obrigatória (sempre tem um estádio).
    -   **Estádio:** Opcional (pode estar vinculado a um jogo, ou não).

## 4. Relacionamento entre Jogo e Time

-   **Cardinalidade:**
    -   Um jogo → vários times (N:M).
    -   Um time → vários jogos (M:N).
-   **Participação:**
    -   **Jogo:** Obrigatória (sempre tem time vinculados).
    -   **Time:** Opcional (pode estar vinculado a um jogo, ou não).

## 5. Relacionamento entre Estádio e Localização

-   **Cardinalidade:**
    -   Um estádio → uma localização (1:1).
    -   Uma localização → vários estádios (N:1).
-   **Participação:**
    -   **Estádio:** Obrigatória (sempre tem uma localização).
    -   **Localização:** Opcional (pode estar vinculado a um estadio, ou não).

## 6. Relacionamento entre Estádio e Time

-   **Cardinalidade:**
    -   Um estádio → um time (1:1).
    -   Um time → um estádio (1:1).
-   **Participação:**
    -  **Estádio:** Opcional (pode estar vinculado a um time, ou não).
    -  **Time:** Opcional (pode estar vinculado a um estadio, ou não).

## 7. Relacionamento entre Time e Jogador

-   **Cardinalidade:**
    -   Um time → vários jogadores (1:N).
    -   Um jogador → um time (N:1).
-   **Participação:**
    -   **Time:** Opcional (pode estar vinculado a jogadores, ou não).
    -   **Jogador:** Opcional (pode estar vinculado a um time, ou não).

## 8. Relacionamento entre Time e Técnico

-   **Cardinalidade:**
    -   Um time → um técnico (1:1).
    -   Um técnico → um time (1:1).
-   **Participação:**
     -   **Time:** Opcional (pode estar vinculado a um tecnico, ou não).
     -   **Tecnico:** Opcional (pode estar vinculado a um time, ou não).

## 9. Relacionamento entre Jogador e Título

-   **Cardinalidade:**
    -   Um jogador → vários títulos (1:N).
    -   Um título → vários jogadores (N:M).
-   **Participação:**
    -   Ambos são opcionais.

## 10. Relacionamento entre Jogador e Estatística

-   **Cardinalidade:**
    -   Um jogador → uma estatística (1:1).
    -   Uma estatística → um jogador (1:1).
-   **Participação:**
    -   Ambos são obrigatórios.

## 11. Relacionamento entre Pessoa e Jogador

-   **Cardinalidade:**
    -   Um jogador → uma pessoa (1:1).
    -   Uma pessoa → um jogador (1:1).
-   **Participação:**
    -   **Pessoa:** Opcional (pode estar vinculado a um jogador, ou não).
    -   **Jogador:** Obrigatória (sempre tem pessoa).

## 12. Relacionamento entre Pessoa e Técnico

-   **Cardinalidade:**
    -   Um técnico → uma pessoa (1:1).
    -   Uma pessoa → um técnico (1:1).
-   **Participação:**
    -   **Pessoa:** Opcional (pode estar vinculado a um tecnico, ou não).
    -   **Tecnico:** Obrigatória (sempre tem pessoa).

## 13. Relacionamento entre Pessoa e Árbitro

-   **Cardinalidade:**
    -   Um árbitro → uma pessoa (1:1).
    -   Uma pessoa → um árbitro (1:1).
-   **Participação:**
    -   **Pessoa:** Opcional (pode estar vinculado a um arbitro, ou não).
    -   **Arbitro:** Obrigatória (sempre tem pessoa).

## 14. Relacionamento entre Localização e Time

-   **Cardinalidade:**
    -   Uma localização → varios times (1:N).
    -   Um time → uma localização (1:1).
-   **Participação:**
    -   **Localização:** Opcional (pode estar vinculado a um time, ou não).
    -   **Time:** Obrigatória (sempre tem localização).

# Modelo de Entidade Relacionamento

![Imagem Modelo de Entidade Relacionamento](./diagrams_images/modelo_entidade_relacionamento.jpeg)

# Modelo Relacional (MySQL Workbench)

![Imagem Modelo Relacional](./diagrams_images/modelo_relacional.png)

# Consultas em SQL e Algebra Relacional

## Primeira Consulta

Seleção de jogadores, seus respectivos times e competições em que participaram

### SQL

```sql
SELECT Jogador.id AS id_jogador, Jogador.posicao, Time.nome AS nome_time, Competicao.nome AS nome_competicao
FROM Jogador
JOIN Time ON Jogador.id_time = Time.id
JOIN Jogo_Time ON Jogo_Time.id_time = Time.id
JOIN Jogo ON Jogo_Time.id_jogo = Jogo.id
JOIN Competicao ON Jogo.id_competicao = Competicao.id;
```

### Álgebra Relacional
```txt
ρ id_jogador←Jogador.id, nome_time←Time.nome, competicao_nome←Competicao.nome 
π Jogador.id, Jogador.posicao, Time.nome, Competicao.nome ( 
    ( 
        ( 
            ( Jogador ⨝ Jogador.id_time = Time.id Time ) 
            ⨝ Jogo_Time.id_time = Time.id Jogo_Time ) 
        ⨝ Jogo_Time.id_jogo = Jogo.id Jogo ) 
    ⨝ Jogo.id_competicao = Competicao.id Competicao 
)
```

### Construção da Consulta

1. Parte 

A consulta começa juntando as tabelas Jogador e Time. Usamos a junção para relacionar o id_time da tabela Jogador com o id da tabela Time. 
Isso permite que possamos acessar as informações do jogador juntamente com o nome do time.

```
A = (Jogador ⨝ Jogador.id_time = Time.id Time) =
SELECT Jogador.id, Jogador.posicao, Time.nome 
FROM Jogador 
JOIN Time ON Jogador.id_time = Time.id;
```

2. Parte

A consulta é expandida para incluir a tabela Jogo_Time. A junção agora é feita entre Time e Jogo_Time com base no campo id_time. 
Isso permite que, além das informações do jogador e do time, possamos acessar o id_jogo da tabela Jogo_Time, que indica o jogo em que o time participou.

```
B = (A ⨝ Jogo_Time.id_time = Time.id Jogo_Time) = 
SELECT Jogador.id, Jogador.posicao, Time.nome, Jogo_Time.id_jogo 
FROM Jogador 
JOIN Time ON Jogador.id_time = Time.id 
JOIN Jogo_Time ON Jogo_Time.id_time = Time.id;
```

3. Parte

A consulta é expandida para incluir a tabela Jogo. Usamos uma junção com base no campo id_jogo de Jogo_Time e o id de Jogo. Isso nos dá acesso aos dados do jogo, como a competição na qual ele ocorreu. Agora temos as informações do jogador, do time e do jogo.

```
C = (B ⨝ Jogo_Time.id_jogo = Jogo.id Jogo) =
SELECT Jogador.id, Jogador.posicao, Time.nome, Competicao.nome
FROM Jogador
JOIN Time ON Jogador.id_time = Time.id
JOIN Jogo_Time ON Jogo_Time.id_time = Time.id
JOIN Jogo ON Jogo.id = Jogo_Time.id_jogo;
```

4. Parte

Adicionamos a tabela Competicao à consulta. A junção é feita entre Jogo e Competicao com base no campo id_competicao. Agora, podemos acessar o nome da competição junto com as informações do jogador, time e jogo.

```
D = (C ⨝ Jogo.id_competicao = Competicao.id Competicao) =
SELECT Jogador.id, Jogador.posicao, Time.nome, Competicao.nome
FROM Jogador
JOIN Time ON Jogador.id_time = Time.id
JOIN Jogo_Time ON Jogo_Time.id_time = Time.id
JOIN Jogo ON Jogo.id = Jogo_Time.id_jogo
JOIN Competicao ON Jogo.id_competicao = Competicao.id;
```

5. Parte

Faz uma projeção que seleciona especificamente as colunas que queremos ver no resultado final: Jogador.id, Jogador.posicao, Time.nome e Competicao.nome. 
Ou seja, estamos filtrando as colunas que serão exibidas no resultado da consulta.

```
E = (π Jogador.id, Jogador.posicao, Time.nome, Competicao.nome) = 
SELECT Jogador.id, Jogador.posicao, Time.nome, Competicao.nome
```

6. Parte

Aqui, a operação de renomeação é aplicada. Estamos renomeando as colunas.

```
F = (ρ id_jogador←Jogador.id, nome_time←Time.nome, competicao_nome←Competicao.nome) = 
SELECT 
Jogador.id AS id_jogador, 
Time.nome AS nome_time, 
Competicao.nome AS competicao_nome
```

## Segunda Consulta

Seleção de títulos conquistados pelos jogadores em um time específico.

### SQL

```sql
SELECT Jogador.id AS id_jogador, Pessoa.nome AS nome_jogador, Titulo.nome AS titulo_nome
FROM Jogador
JOIN Pessoa ON Jogador.id_pessoa = Pessoa.id
JOIN Jogador_Titulo ON Jogador.id = Jogador_Titulo.id_jogador
JOIN Titulo ON Jogador_Titulo.id_titulo = Titulo.id
JOIN Time ON Jogador.id_time = Time.id
WHERE Time.nome = 'TimeTeste1';
```

### Álgebra Relacional
```txt
ρ id_jogador←Jogador.id, nome_jogador←Pessoa.nome, titulo_nome←Titulo.nome 
π Jogador.id, Pessoa.nome, Titulo.nome 
σ Time.nome = 'TimeTeste1' ( 
    ( 
        ( 
            (Jogador ⨝ Jogador.id_pessoa = Pessoa.id Pessoa) 
            ⨝ Jogador.id = Jogador_Titulo.id_jogador Jogador_Titulo 
        ) 
        ⨝ Jogador_Titulo.id_titulo = Titulo.id Titulo 
    ) 
    ⨝ Jogador.id_time = Time.id Time 
)
```

### Construção da Consulta

1. Parte 

Relacionamos a tabela Jogador com Pessoa utilizando o campo id_pessoa da tabela Jogador e o campo id da tabela Pessoa.
Isso permite acessar o nome do jogador associado ao seu registro na tabela Pessoa.

```
A = (Jogador ⨝ Jogador.id_pessoa = Pessoa.id Pessoa) = 
SELECT Jogador.id, Pessoa.nome
FROM Jogador
JOIN Pessoa ON Jogador.id_pessoa = Pessoa.id;
```

2. Parte

Expandimos a consulta para incluir informações sobre os títulos conquistados pelos jogadores. 
A junção ocorre entre Jogador e Jogador_Titulo com base no campo id da tabela Jogador e id_jogador da tabela Jogador_Titulo.

```
B = (A ⨝ Jogador.id = Jogador_Titulo.id_jogador Jogador_Titulo) = 
SELECT Jogador.id, Pessoa.nome, Jogador_Titulo.id_titulo
FROM Jogador
JOIN Pessoa ON Jogador.id_pessoa = Pessoa.id
JOIN Jogador_Titulo ON Jogador.id = Jogador_Titulo.id_jogador;
```

3. Parte

A consulta é estendida para incluir informações sobre os títulos, como o nome dos títulos conquistados pelos jogadores. 
A junção é feita entre Jogador_Titulo e Titulo com base nos campos id_titulo e id.

```
C = (B ⨝ Jogador_Titulo.id_titulo = Titulo.id Titulo) = 
SELECT Jogador.id, Pessoa.nome, Titulo.nome
FROM Jogador
JOIN Pessoa ON Jogador.id_pessoa = Pessoa.id
JOIN Jogador_Titulo ON Jogador.id = Jogador_Titulo.id_jogador
JOIN Titulo ON Jogador_Titulo.id_titulo = Titulo.id;
```

4. Parte

Incluímos a tabela Time para relacionar os jogadores aos seus respectivos times. 
A junção é feita com base no campo id_time da tabela Jogador e o campo id da tabela Time.

```
D = (C ⨝ Jogador.id_time = Time.id Time) = 
SELECT Jogador.id, Pessoa.nome, Titulo.nome, Time.nome
FROM Jogador
JOIN Pessoa ON Jogador.id_pessoa = Pessoa.id
JOIN Jogador_Titulo ON Jogador.id = Jogador_Titulo.id_jogador
JOIN Titulo ON Jogador_Titulo.id_titulo = Titulo.id
JOIN Time ON Jogador.id_time = Time.id;
```

5. Parte

Aplicamos a seleção para filtrar apenas os jogadores que pertencem ao time "TimeTeste1".

```
E = (σ Time.nome = 'TimeTeste1') =
WHERE Time.nome = 'TimeTeste1';
```

6. Parte

Selecionamos apenas as colunas para mostrar, sendo elas: o ID e nome do jogador, bem como seu respectivo titulo.

```
F = (π Jogador.id, Pessoa.nome, Titulo.nome) = 
SELECT Jogador.id AS id_jogador, Pessoa.nome AS nome_jogador, Titulo.nome AS nome_titulo
```

## Terceira Consulta

Exibição dos árbitros, os jogos que apitaram e os estádios onde os jogos ocorreram

### SQL

```sql
SELECT Arbitro.id AS id_arbitro, Jogo.id AS id_jogo, Jogo.data AS data_jogo, Estadio.nome AS nome_estadio
FROM Arbitro
JOIN Jogo ON Arbitro.id = Jogo.id_arbitro
JOIN Estadio ON Jogo.id_estadio = Estadio.id;
```

### Álgebra Relacional
```txt
ρ id_arbitro←Arbitro.id, id_jogo←Jogo.id, data_jogo←Jogo.data, nome_estadio←Estadio.nome 
π Arbitro.id, Jogo.id, Jogo.data, Estadio.nome ( 
    ( Arbitro ⨝ Arbitro.id = Jogo.id_arbitro Jogo ) 
    ⨝ Jogo.id_estadio = Estadio.id Estadio
)
```

### Construção da Consulta

1. Parte

Começamos relacionando a tabela Arbitro com a tabela Jogo. 
A junção ocorre utilizando o campo id da tabela Arbitro e o campo id_arbitro da tabela Jogo. 
Isso nos permite identificar quais jogos foram apitados por quais árbitros.

```
A = (Arbitro ⨝ Arbitro.id = Jogo.id_arbitro Jogo) = 
SELECT Arbitro.id AS id_arbitro, Jogo.id AS id_jogo, Jogo.data
FROM Arbitro
JOIN Jogo ON Arbitro.id = Jogo.id_arbitro;
```

2. Parte

Expandimos a consulta para incluir os dados sobre os estádios onde os jogos ocorreram. 
A junção é feita utilizando o campo id_estadio da tabela Jogo e o campo id da tabela Estadio.

```
B = A ⨝ Jogo.id_estadio = Estadio.id Estadio = 
SELECT Arbitro.id AS id_arbitro, Jogo.id AS id_jogo, Jogo.data AS data_jogo, Estadio.nome AS nome_estadio
FROM Arbitro
JOIN Jogo ON Arbitro.id = Jogo.id_arbitro
JOIN Estadio ON Jogo.id_estadio = Estadio.id;
```

3. Parte

Selecionamos apenas as colunas para mostrar, sendo elas: o ID do árbitro, o ID do jogo, a data do jogo, e o nome do estádio.

```
C = π Arbitro.id, Jogo.id, Jogo.data, Estadio.nome B = 
SELECT Arbitro.id ,Jogo.id ,Jogo.data ,Estadio.nome
```

4. Parte

Finalmente, renomeamos as colunas para os nomes desejados no resultado :

```
D = ρ id_arbitro←Arbitro.id, id_jogo←Jogo.id, data_jogo←Jogo.data, nome_estadio←Estadio.nome C =
SELECT Arbitro.id AS id_arbitro, Jogo.id AS id_jogo, Jogo.data AS data_jogo, Estadio.nome AS nome_estadio
```

## Quarta Consulta

Listagem de jogadores, suas estatísticas e o time ao qual pertencem.

### SQL

```sql
SELECT Jogador.id AS id_jogador, Pessoa.nome AS nome_jogador, Estatistica.quantidade_jogos_jogados, Time.nome AS nome_time
FROM Jogador
JOIN Pessoa ON Jogador.id_pessoa = Pessoa.id
JOIN Estatistica ON Jogador.id_estatistica = Estatistica.id
JOIN Time ON Jogador.id_time = Time.id;
```

### Álgebra Relacional
```txt
ρ id_jogador←Jogador.id, nome_jogador←Pessoa.nome, nome_time←Time.nome 
π Jogador.id, Pessoa.nome, Estatistica.quantidade_jogos_jogados, Time.nome 
( 
    ( 
        ( Jogador ⨝ Jogador.id_pessoa = Pessoa.id Pessoa ) 
        ⨝ Jogador.id_estatistica = Estatistica.id Estatistica 
    ) 
    ⨝ Jogador.id_time = Time.id Time
)
```

### Construção da Consulta

1. Parte 

Relacionamos a tabela Jogador com a tabela Pessoa. 
A junção ocorre utilizando o campo id_pessoa da tabela Jogador e o campo id da tabela Pessoa. 
Isso permite que possamos associar as informações pessoais ao jogador.

```
A = (Jogador ⨝ Jogador.id_pessoa = Pessoa.id Pessoa) =
SELECT Jogador.id AS id_jogador, Pessoa.nome AS nome_jogador
FROM Jogador
JOIN Pessoa ON Jogador.id_pessoa = Pessoa.id;
```

2. Parte

Expandimos a consulta para incluir as informações de estatísticas do jogador, como o número de jogos jogados. 
A junção é feita utilizando o campo id_estatistica da tabela Jogador e o campo id da tabela Estatistica.

```
B = (A ⨝ Jogador.id_estatistica = Estatistica.id Estatistica) = 
SELECT Jogador.id AS id_jogador, Pessoa.nome AS nome_jogador, Estatistica.quantidade_jogos_jogados
FROM Jogador
JOIN Pessoa ON Jogador.id_pessoa = Pessoa.id
JOIN Estatistica ON Jogador.id_estatistica = Estatistica.id;
```

3. Parte

Expandimos ainda mais a consulta para incluir informações sobre o time ao qual o jogador pertence.
A junção é feita utilizando o campo id_time da tabela Jogador e o campo id da tabela Time.

```
C = (B ⨝ Jogador.id_time = Time.id Time) = 
SELECT Jogador.id AS id_jogador, Pessoa.nome AS nome_jogador, Estatistica.quantidade_jogos_jogados, Time.nome AS nome_time
FROM Jogador
JOIN Pessoa ON Jogador.id_pessoa = Pessoa.id
JOIN Estatistica ON Jogador.id_estatistica = Estatistica.id
JOIN Time ON Jogador.id_time = Time.id;
```

4. Parte

Selecionamos apenas as colunas relevantes para o resultado.

```
D = (π Jogador.id, Pessoa.nome, Estatistica.quantidade_jogos_jogados, Time.nome) = 
SELECT Jogador.id , Pessoa.nome, Estatistica.quantidade_jogos_jogados, Time.nome
```

5. Parte

Renomeamos as colunas para os aliás desejados. 

```
E = (ρ id_jogador←Jogador.id, nome_jogador←Pessoa.nome, nome_time←Time.nome) =
SELECT Jogador.id AS id_jogador, Pessoa.nome AS nome_jogador, Estatistica.quantidade_jogos_jogados, Time.nome AS nome_time
```


## Quinta Consulta

Seleção de jogos, os times que participaram e o estádio onde o jogo ocorreu.

### SQL

```sql
SELECT Jogo.id AS id_jogo, TimeCasa.nome AS nome_time_casa, TimeVisitante.nome AS nome_time_visitante, Jogo.data, Estadio.nome AS nome_estadio
FROM Jogo
JOIN Jogo_Time AS Jogo_Time_Casa ON Jogo.id = Jogo_Time_Casa.id_jogo
JOIN Time AS TimeCasa ON Jogo_Time_Casa.id_time = TimeCasa.id
JOIN Jogo_Time AS Jogo_Time_Visitante ON Jogo.id = Jogo_Time_Visitante.id_jogo
JOIN Time AS TimeVisitante ON Jogo_Time_Visitante.id_time = TimeVisitante.id
JOIN Estadio ON Jogo.id_estadio = Estadio.id;
```

### Álgebra Relacional
```txt
ρ id_jogo←Jogo.id, nome_time_casa←TimeCasa.nome, nome_time_visitante←TimeVisitante.nome, nome_estadio←Estadio.nome 
π Jogo.id, TimeCasa.nome, TimeVisitante.nome, Jogo.data, Estadio.nome 
( 
    ( 
        ( 
            ( 
                (Jogo ⨝ Jogo.id = Jogo_Time_Casa.id_jogo ρ Jogo_Time_Casa Jogo_Time) 
                ⨝ Jogo_Time_Casa.id_time = TimeCasa.id ρ TimeCasa Time 
                )
            ⨝ Jogo.id = Jogo_Time_Visitante.id_jogo ρ Jogo_Time_Visitante Jogo_Time 
        )
        ⨝ Jogo_Time_Visitante.id_time = TimeVisitante.id ρ TimeVisitante Time 
    )
    ⨝ Jogo.id_estadio = Estadio.id Estadio 
)
```

### Construção da Consulta

1. Parte 

Associamos os jogos à tabela de relação Jogo_Time, que mapeia quais times participaram de cada jogo.
A junção é feita utilizando o campo id da tabela Jogo e o campo id_jogo da tabela Jogo_Time.

```
A = (Jogo ⨝ Jogo.id = Jogo_Time_Casa.id_jogo ρ Jogo_Time_Casa Jogo_Time) = 
SELECT Jogo.id AS id_jogo, Jogo.data
FROM Jogo
JOIN Jogo_Time AS Jogo_Time_Casa ON Jogo.id = Jogo_Time_Casa.id_jogo;
```

2. Parte

Expandimos a consulta para incluir as informações do time. 
A junção é feita utilizando o campo id_time da tabela Jogo_Time e o campo id da tabela Time.

```
B = A ⨝ Jogo_Time_Casa.id_time = TimeCasa.id ρ TimeCasa Time = 
SELECT Jogo.id AS id_jogo, Jogo.data, Time.nome AS nome_time_casa
FROM Jogo
JOIN Jogo_Time AS Jogo_Time_Casa ON Jogo.id = Jogo_Time_Casa.id_jogo
JOIN Time AS TimeCasa ON Jogo_Time_Casa.id_time = TimeCasa.id;
```

3. Parte

Incluímos o time visitante ao jogo criando um aliás para as tabelas Jogo_Time_Casa e TimeCasa, chamadas de Jogo_Time_Visitante e TimeVisitante.
Assim, conseguimos associar um segundo time ao mesmo jogo.

```
C = (B ⨝ Jogo.id = Jogo_Time_Visitante.id_jogo ρ Jogo_Time_Visitante Jogo_Time ⨝ Jogo_Time_Visitante.id_time = TimeVisitante.id ρ TimeVisitante Time) = 
SELECT Jogo.id AS id_jogo, Jogo.data, Time.nome AS nome_time_casa, TimeVisitante.nome AS nome_time_visitante
FROM Jogo
JOIN Jogo_Time AS Jogo_Time_Casa ON Jogo.id = Jogo_Time_Casa.id_jogo
JOIN Time AS TimeCasa ON Jogo_Time_Casa.id_time = TimeCasa.id
JOIN Jogo_Time AS Jogo_Time_Visitante ON Jogo.id = Jogo_Time_Visitante.id_jogo
JOIN Time AS TimeVisitante ON Jogo_Time_Visitante.id_time = TimeVisitante.id;
```

4. Parte

Associamos os estádios onde os jogos ocorreram utilizando o campo id_estadio da tabela Jogo e o campo id da tabela Estadio.

```
D = (C ⨝ Jogo.id_estadio = Estadio.id Estadio) = 
SELECT Jogo.id AS id_jogo, Time.nome AS nome_time_casa, TimeVisitante.nome AS nome_time_visitante, Jogo.data, Estadio.nome AS nome_estadio
FROM Jogo
JOIN Jogo_Time AS Jogo_Time_Casa ON Jogo.id = Jogo_Time_Casa.id_jogo
JOIN Time AS TimeCasa ON Jogo_Time_Casa.id_time = TimeCasa.id
JOIN Jogo_Time AS Jogo_Time_Visitante ON Jogo.id = Jogo_Time_Visitante.id_jogo
JOIN Time AS TimeVisitante ON Jogo_Time_Visitante.id_time = TimeVisitante.id
JOIN Estadio ON Jogo.id_estadio = Estadio.id;
```

5. Parte

Selecionamos apenas as colunas relevantes para o resultado.

```
E = (π Jogo.id, TimeCasa.nome, TimeVisitante.nome, Jogo.data, Estadio.nome) = 
SELECT Jogo.id, TimeCasa.nome, TimeVisitante.nome, Jogo.data, Estadio.nome
```