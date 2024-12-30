pasta_sql = './sql'

arquivos_sql = [
    './sql/criar_banco_dados.sql', 
    './sql/tabela_competicao.sql', 
    './sql/tabela_localizacao.sql', 
    './sql/tabela_estatistica.sql', 
    './sql/tabela_titulo.sql', 
    './sql/tabela_pessoa.sql', 
    './sql/tabela_estadio.sql', 
    './sql/tabela_time.sql', 
    './sql/tabela_arbitro.sql', 
    './sql/tabela_tecnico.sql', 
    './sql/tabela_jogo.sql', 
    './sql/tabela_jogador.sql', 
    './sql/tabela_jogo_time.sql',
    './sql/tabela_jogador_titulo.sql'
]

arquivo_saida = './schema_banco_dados.sql'

with open(arquivo_saida, 'w') as f_saida:
    for arquivo in arquivos_sql:
        with open(arquivo, 'r') as f_entrada:
            f_saida.write(f_entrada.read())
            f_saida.write('\n\n')