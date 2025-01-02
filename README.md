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
    -   **Jogo:** Opcional (pode estar vinculado a uma competição, ou não).
    -   **Competição:** Obrigatório (sempre tem um jogo).

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
    -   **Localização:** Opcional (pode estar vinculado a uma localização, ou não).

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
    -   **Time:** Obrigatória (sempre tem  jogadores).
    -   **Jogador:** Opcional (pode estar vinculado a um time, ou não).

## 8. Relacionamento entre Time e Técnico

-   **Cardinalidade:**
    -   Um time → um técnico (1:1).
    -   Um técnico → um time (1:1).
-   **Participação:**
     -   **Time:** Obrigatória (sempre tem tecnico).
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
    -   Ambos são obrigatórios.

## 12. Relacionamento entre Pessoa e Técnico

-   **Cardinalidade:**
    -   Um técnico → uma pessoa (1:1).
    -   Uma pessoa → um técnico (1:1).
-   **Participação:**
    -   Ambos são obrigatórios.

## 13. Relacionamento entre Pessoa e Árbitro

-   **Cardinalidade:**
    -   Um árbitro → uma pessoa (1:1).
    -   Uma pessoa → um árbitro (1:1).
-   **Participação:**
    -   Ambos são obrigatórios.

# Modelo de Entidade Relacionamento

![Imagem Modelo de Entidade Relacionamento](./diagrams_images/modelo_entidade_relacionamento.jpeg)

# Modelo Relacional (MySQL Workbench)

![Imagem Modelo Relacional](./diagrams_images/modelo_relacional.png)

# Consultas em SQL e Algebra Relacional

## Primeira Consulta

Essa consulta retorna uma lista de jogadores, suas posições, os nomes dos times aos quais pertencem, e as competições nas quais eles estão vinculados.

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
ρ jogador_id←Jogador.id, time_nome←Time.nome, competicao_nome←Competicao.nome 
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
A = ( Jogador ⨝ Jogador.id_time = Time.id Time ) =
SELECT Jogador.id, Jogador.posicao, Time.nome 
FROM Jogador 
JOIN Time ON Jogador.id_time = Time.id;
```

2. Parte

A consulta é expandida para incluir a tabela Jogo_Time. A junção agora é feita entre Time e Jogo_Time com base no campo id_time. 
Isso permite que, além das informações do jogador e do time, possamos acessar o id_jogo da tabela Jogo_Time, que indica o jogo em que o time participou.

```
B = A ⨝ Jogo_Time.id_time = Time.id Jogo_Time = 
SELECT Jogador.id, Jogador.posicao, Time.nome, Jogo_Time.id_jogo 
FROM Jogador 
JOIN Time ON Jogador.id_time = Time.id 
JOIN Jogo_Time ON Jogo_Time.id_time = Time.id;
```

3. Parte

A consulta é expandida para incluir a tabela Jogo. Usamos uma junção com base no campo id_jogo de Jogo_Time e o id de Jogo. Isso nos dá acesso aos dados do jogo, como a competição na qual ele ocorreu. Agora temos as informações do jogador, do time e do jogo.

```
C = B ⨝ Jogo_Time.id_jogo = Jogo.id Jogo
SELECT Jogador.id, Jogador.posicao, Time.nome, Competicao.nome
FROM Jogador
JOIN Time ON Jogador.id_time = Time.id
JOIN Jogo_Time ON Jogo_Time.id_time = Time.id
JOIN Jogo ON Jogo.id = Jogo_Time.id_jogo;
```

4. Parte

Adicionamos a tabela Competicao à consulta. A junção é feita entre Jogo e Competicao com base no campo id_competicao. Agora, podemos acessar o nome da competição junto com as informações do jogador, time e jogo.

```
D = C ⨝ Jogo.id_competicao = Competicao.id Competicao
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
E = π Jogador.id, Jogador.posicao, Time.nome, Competicao.nome = 
SELECT Jogador.id, Jogador.posicao, Time.nome, Competicao.nome
```

6. Parte

Aqui, a operação de renomeação é aplicada. Estamos renomeando as colunas.

```
F = ρ jogador_id←Jogador.id, time_nome←Time.nome, competicao_nome←Competicao.nome = 
SELECT 
Jogador.id AS jogador_id, 
Time.nome AS time_nome, 
Competicao.nome AS competicao_nome
```