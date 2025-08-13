# Oficina de IA SAEV

Esta Oficina visa apresentar o uso do Copilot Github integrado ao VS Code para produção de painéis de BI, bem como a produção de código em Python e R para aálise de Dados.


##  Objetivos

1. Com base nos microdados exportados do SAEV (Tipo da exportação: Normalizada) construir todo o processo de ETL (Os dados exportados edstão no formato CSV e segue a arquitetura STAR SCHEMA);
2. Criar um Banco de Dados DuckDB (para uso no computador local) com a arquiterura STAR SCHEMA conforme orientação a seguir (seção: Estrutura de Dados)
3. Criar painéis utilizando o Streamlit e Python para apresentação em navegador WEB;
4. Desenvolver relatórios utilizando o R;
5. Debater sobre oportunidades de melhorias;
6. Debater sobre a possibilidade de oferecer os produtos gerados por esta oficina aos parceiros do EPV.


## Estruturas de dados 

Esta seção apresenta as estruturas de dados de entrada (microdados do SAEV) e as estruturas de saída (Banco de Dados DuckDB e Tabelas)

### Arquivos de entrada (Microdados no formato CSV) 

#### Arquivo avaliacao.csv 

Este arquivo contém os resultados das avaliações dos alunos nos testes realizados. As métricas de avaliação dervem ser obtidas deste arquivo. Ou seja, a tabela fato do modelo Star Schema utiliza utiliza como fonte os dados deste arquivo. A primeira linha do arquivo "avaliacao.csv" contém os nomes dos campos conforme a tabela a seguir: 

| Nome do campo       | Tipo de Dados  | Descrição | 
| ------------------- | -------------- | --------- | 
| MUN_UF              | CHAR(2)        | Unidade da Federação do Município | 
| MUN_IBGE            | INTEGER        | Código IBGE do Município | 
| ESC_INEP            | INTEGER        | Código INEP da Escola | 
| SER_NUMBER          | CHAR(1)        | Número da Série | 
| SER_NOME            | VARCHAR(15)    | Nome da Série | 
| TUR_PERIODO         | VARCHAR(15)    | Turno o período |  
| TUR_NOME            | VARCHAR(20)    | Nome do Turno | 
| ALU_ID              | INTEGER        | Código de Identificação do Aluno no sistema SAEV | 
| AVA_NOME            | VARCHAR(25)    | Nome da Avaliação | 
| AVA_ANO             | INTEGER        | Ano da Avaliação | 
| TES_ID              | INTEGER        | Código de Identificação do teste no sistema SAEV | 
| DIS_NOME            | VARCHAR(20)    | Nome da Disciplina | 
| ALT_FINALIZADO      | INTEGER        | Se o valor for 0, indica que o aluno não participou do teste por alguma razão; Se o valor for 1 indica que o aluno fez o teste |  
| ALT_JUSTIFICATIVA   | VARCHAR(50)    | Texto descritivo sobre o motivo do aluno não ter realizado o teste | 
| NR_QUESTAO          | VARCHAR(8)     | Quanto o teste for com questões objetivas (Lingua Portuguesa ou Matemática) assume o número assume o código da questão na base do SAEV; se for um teste de fluência leitora, assume "N/A" | 
| TEG_ORDEM           | VARCHAR(5)     | Quanto o teste for com questões objetivas (Lingua Portuguesa ou Matemática) assume o número sequencial correspondente a questão; se for um teste de fluência leitora assume "N/A" |    
| ATR_RESPOSTA        | VARCHAR(15)    | Para teste de Lingua Portuguesa e Matemática (com questões objetivas) pode assumir os valores "A", "B", "C", "D", "-"; para Teste de Leitura (fluência leitora), pode assumir "nao_leitor", "silabas", "palavras", "frases", "nao_fluente", "fluente", "N/A". |  
| ATR_CERTO           | VARCHAR(5)     | Quanto o teste for com questões objetivas (Lingua Portuguesa ou Matemática) assume 1 se a resposta do aluno for correta ou 0 se a resposta for errada; Para teste de fluência leitora, assume "N/A" |  
| MTI_CODIGO          | VARCHAR(5)     | Quanto o teste for com questões objetivas (Lingua Portuguesa ou Matemática) assume assume o código do descritor da questão; se for um teste de fluência leitora, asusme "N/A" | 







### Arquivo de Saída ( Banco de Dados DuckDB )
