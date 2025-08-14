# Microdados SAEV 

Para baixar os microdados do SAEV para para ente ambiente siha os seguintes passos: 
1) Entre no sistema [SAEV](https://saev.abc.br); 
2) faça login; 
3) selecione no menu a opção **Exportar Microdados**;
4) Selecione no filtro **Tipo de Microdado** a opção **Avaliação Normalizada**; e
5) Nos demais filtros selecione as opções conforme a necessidade. 


A depender do seu perfil de acesso no sistema, você só poderá baixar os microdados do seu município. Se o seu perfil for de Regional, você poderá baixar os microdados de todos os municípios que abrange a sua região. Por fim, se o seu perfil for Estadual, voc6e poderá baixar os microdados de todos os municípios do estado. 

## Importante

Os microdados são exportados seguindo uma estrutura previamente planejada para facilitar a implementação de um modelo de dados no formato Star Schema. Nesse modelo, os registros numéricos e quantitativos — como contagem de questões certas e erradas, bem como contagem da classificação do nível de leitura — ficam concentrados em uma tabela fato, enquanto as informações descritivas associadas — como dados de aluno, escola, município, teste ou descritor — são organizadas em tabelas dimensão. Essa separação clara entre fatos e dimensões simplifica a modelagem, melhora o desempenho das consultas e garante maior flexibilidade para análises multidimensionais em ferramentas de Business Intelligence e Data Warehousing, permitindo que cortes e combinações de dados sejam realizados de forma ágil e consistente. A tabela a seguir apresenta os arquivos resultantes da exportação de microdados. 


| Nome do arquivo   |  Descrição |
| ----------------- | ---------- |  
| avaliacao.csv     | Resultado de Avaliação - este arquivo é a base para a criação da tabela fato (métricas de avaliação)  |
| testes.csv        | Tabela de teste do SAEV (dimensões teste e disciplina) |   
| municipios.csv    | Tabela de municípios (dimensão município) | 
| escolas.csv       | Tabela de escolas (dimensão escola) |     
| descritores.csv   | Tabela de descritores (dimensão descritores) | 
| alunos.csv        | Tabela de alunos (dimensão alunos) | 


## Estruturas de Dados

Esta seção apresenta as estruturas de dados de entrada (microdados do SAEV) e as estruturas de saída (Banco de Dados DuckDB e tabelas).


### Arquivos de Entrada (Microdados no formato CSV)

A seguir é apresentado em detalhe a estrutura dos arquivos CSV, seus campos, tipos de dados e descrição. Esta informação é útil para a criação das tabelas de banco de dados em DuckDB (banco de dados OLAP). 


Os arquivo no formato CSV possuem as seguintes características: 

1) a primeira linha contém os nomes dos campos;
2) o separador de campo é o caractere pipe '|'. É importante destacar que utilizar o '|' no lugar de ';' ou ',' reduz a chance de ocorrer erro durante a carga de dados;
3) O conteúdo de alguns campos como nome do Aluno, Escola e Endereço podem conter espaços em branco antes e depois do nome. Nestes casos, recomenda-se a exclusão destes espaços no processo de ETL


#### Arquivo avaliacao.csv

Este arquivo contém os resultados das avaliações dos alunos nos testes realizados no sistema SAEV. Existem dois tipos de testes nas avaliações do SAEV: Objetivas – realizadas nas disciplinas de Língua Portuguesa e Matemática; e Leitura – em que o aluno lê um texto e recebe uma classificação do avaliador. As provas objetivas admitem respostas do tipo "A", "B", "C", "D"; nas provas de leitura, os alunos podem ser classificados como "nao_leitor", "sílabas", "palavras", "frases", "não_fluente" e "fluente".

As métricas de avaliação devem ser obtidas deste arquivo. Ou seja, a tabela fato do modelo Star Schema utiliza como fonte os dados deste arquivo. A primeira linha do arquivo "avaliacao.csv" contém os nomes dos campos conforme a tabela a seguir:

| Nome do campo       | Tipo de Dados  | Descrição |
| ------------------- | -------------- | --------- |
| MUN_UF              | CHAR(2)        | Unidade da Federação do Município |
| MUN_IBGE            | INTEGER        | Código IBGE do Município |
| ESC_INEP            | INTEGER        | Código INEP da Escola |
| SER_NUMBER          | INTEGER        | Número da série |
| SER_NOME            | VARCHAR(15)    | Nome da Série |
| TUR_PERIODO         | VARCHAR(15)    | Turno ou período |
| TUR_NOME            | VARCHAR(20)    | Nome do Turno |
| ALU_ID              | INTEGER        | Código de identificação do aluno no sistema SAEV |
| AVA_NOME            | VARCHAR(25)    | Nome da Avaliação |
| AVA_ANO             | INTEGER        | Ano da Avaliação |

| TES_ID              | INTEGER        | Código de identificação do teste no sistema SAEV |
| DIS_NOME            | VARCHAR(20)    | Nome da disciplina |
| ALT_FINALIZADO      | INTEGER        | Se o valor for 0, indica que o aluno não participou do teste por alguma razão; se o valor for 1, indica que o aluno fez o teste |
| ALT_JUSTIFICATIVA   | VARCHAR(50)    | Texto descritivo sobre o motivo do aluno não ter realizado o teste |
| NR_QUESTAO          | VARCHAR(8)     | Para testes com questões objetivas (Língua Portuguesa ou Matemática), assume o código da questão na base do SAEV; para teste de fluência leitora, assume "N/A" |
| TEG_ORDEM           | VARCHAR(5)     | Para testes com questões objetivas, assume o número sequencial correspondente à questão; para teste de fluência leitora, assume "N/A" |
| ATR_RESPOSTA        | VARCHAR(15)    | Para testes de Língua Portuguesa e Matemática (questões objetivas), pode assumir os valores "A", "B", "C", "D", "-"; para teste de leitura (fluência leitora), pode assumir "nao_leitor", "sílabas", "palavras", "frases", "não_fluente", "fluente", "N/A". |
| ATR_CERTO           | VARCHAR(5)     | Para testes com questões objetivas, assume 1 se a resposta do aluno for correta ou 0 se for errada; para teste de fluência leitora, assume "N/A" |
| MTI_CODIGO          | VARCHAR(5)     | Para testes com questões objetivas, assume o código do descritor da questão; para teste de fluência leitora, assume "N/A" |


#### Arquivo alunos.csv

Este arquivo contém os dados pessoais do aluno, bem como a situação corrente dele. É importante destacar que a situação corrente do aluno não necessariamente coincide com a situação dele durante uma avaliação. Neste contexto, para efeito das análises da avaliação e resultados de testes, a situação corrente do aluno é pouco relevante. A tabela a seguir apresenta as informações sobre o arquivo alunos.csv.

| Nome do campo     | Tipo de dado | Descrição |
|-------------------|--------------|-----------|
| MUN_ID            | INTEGER      |  Código e identificação do Município no SAEV |
| MUN_NOME          | VARCHAR(60)  |  Nome do Município  |
| ESC_ID            | INTEGER      |  Código da Escola no SAEV          |
| ESC_NOME          | VARCHAR(60)  |  Nome da Escola         |
| ESC_INEP          | INTEGER      |  Código INEP da Escola         |
| SER_NUMBER        | INTEGER      |  Número da série (anos de 1 a 9)   |
| SER_NOME          | VARCHAR(15)  |  Nome da Série         |
| TUR_ID            | INTEGER      |  Código de identificação da turma corrente do aluno   |
| TUR_NOME          | VARCHAR(20)  |  Nome da turma corrente do aluno   |
| TUR_PERIODO       | VARCHAR(15)  |  Nome do turno da turma (Manhã, Tarde, Tempo Integral)        |
| ALU_ID            | INTEGER      |  Código de identificação do aluno no sistema SAEV          |
| ALU_INEP          | INTEGER      |  Código de identificação do aluno no sistema INEP (Censo Escolar) |
| ALU_NOME          | VARCHAR(60)  |  Nome do Aluno         |
| ALU_NOME_MAE      | VARCHAR(60)  |  Nome da Mãe do Aluno  |
| ALU_NOME_PAI      | VARCHAR(60)  |  Nome do Pai do Aluno  |
| ALU_NOME_RESP     | VARCHAR(60)  |  Nome do Responsável pelo Aluno   |
| ALU_DT_NASC       | DATE         |  Data de nascimento do Aluno no formato DD/MM/YYYY   |
| ALU_TEL1          | VARCHAR(15)  |  Telefone do Aluno (primeira opção)         |
| ALU_TEL2          | VARCHAR(15)  |  Telefone do Aluno (segunda opção)         |
| ALU_EMAIL         | VARCHAR(100) |  Email do aluno  |
| ALU_UF            | CHAR(2)      |  Unidade da Federação da residência do aluno         |
| ALU_ENDERECO      | VARCHAR(120) |  Endereço residencial do Aluno           |
| ALU_CIDADE        | VARCHAR(60)  |  Cidade de residência do Aluno           |
| ALU_NUMERO        | VARCHAR(15)  |  Número da residência do Aluno         |
| ALU_COMPLEMENTO   | VARCHAR(100) |  Complemento do endereço do aluno          |
| ALU_BAIRRO        | VARCHAR(100) |  Bairro da residência do Aluno           |
| ALU_CEP           | VARCHAR(15)  |  Código de endereçamento postal do Aluno (CEP)         |
| ALU_ATIVO         | VARCHAR(3)   |  Se "Sim" o aluno está ativo; se "Não" o aluno está inativo  |
| ALU_STATUS        | VARCHAR(20)  |  Indica se o aluno está enturmado (matriculado em uma turma) ou não enturmado  |
| ALU_CPF           | VARCHAR(15)  |  CPF do Aluno         |
| PEL_NOME          | VARCHAR(15)  |  Cor / raça do aluno  |
| GEN_NOME          | VARCHAR(20)  |  Gênero do aluno      |



#### Arquivo testes.csv 

O Arquivo teste.csv contem informações sobre o teste aplicado. A tabela a seguir apresenta as informações sobre o arquivo testes.csv.   

| Nome do Campo | Tipo de Dado |  Descrição | 
| ------------- | ------------ | ---------- |
| TES_ID        | INTEGER      | Código de identificação do Teste |  
| TES_NOME      | VARCHAR(25)  | Nome do teste / Avaliação |
| TES_ANO       | INTEGER      | Ano de aplicação do Teste | 
| DIS_ID        | INTEGER      | Código de identificação da disciplina | 
| DIS_NOME      | VARCHAR(20)  | Nome da Disciplina |     


#### Arquivo escolas.csv 

Este arquivo contém as informações de escolas. A tabela a seguir apresenta informações sobre o arquivo. 

| Nome do Campo   | Tipo do Campo   |  Descrição   | 
| --------------- | --------------- | ------------ | 
| ESC_ID          | INTEGER         | Código de Identificação da Escola | 
| ESC_NOME        | VARCHAR(60)     | Nome da Escola | 
| ESC_INEP        | INTEGER         | Código INEP da escola | 
| ESC_UF          | CHAR(2)         | Sigla da Unidade da Federação / Estado | 
| ESC_TIPO        | VARCHAR(15)     | Dependência Administrativa da Escola: Municipal ou Estadual | 



#### Arquivo municipios.csv 

Este arquivo contém as informações do município. A tebela a seguir tem informações sobre os campos do arquivo municipios.csv.  

| Nome do Campo  | Tipo de Dados | Descrição | 
| -------------- | ------------- | --------- | 
| MUN_ID         | INTEGER       | Código de identificação do Município no SAEV |    
| MUN_NOME       | VARCHAR(100)  | Nome do Município | 
| MUN_COD_IBGE   | INTEGER       | Código do município segundo o IBGE | 
| MUN_UF         | CHAR(2)       | Unidade da Federação do município |  


#### Arquivo descritor.csv 

Este arquivo contém informações sobre os descritores relacionados aos itens das provas objetivas. A tabela a seguir apresenta as informações sobre as colunas do arquivo descritor.csv. 

| Nome do Campo  | Tipo de Dado  | Descrição       | 
| -------------- | ------------- | --------------- |
| MTI_ID         | INTEGER       | Código sequencial de identificação do descritor no SAEV | 
| MTI_CODIGO     | VARCHAR(5)    | Código do Descritor | 
| MTI_DESCRITOR  | VARCHAR(2048) | Explicação textual sobre o descritor | 
| MTO_ID         | INTEGER       | Código do complemento do descritor  | 
| MTO_NOME       | VARCHAR(256)  | Texto do complemento do descritor | 
| MAR_ID         | INTEGER       | Código de Identificação da Matriz do Descritor |    
| MAR_NOME       | VARCHAR(128)  | Descrição da Matriz | 


### Arquivo de Saída (Banco de Dados DuckDB)


