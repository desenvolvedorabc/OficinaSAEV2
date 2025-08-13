
# Oficina de IA SAEV


Esta oficina tem como objetivo apresentar o uso do GitHub Copilot integrado ao VS Code para a produção de painéis de BI, além do desenvolvimento de código em Python e R para análise de dados.

## Sobre as principais ferramentas utilizadas na oficina

**GitHub:** Plataforma de hospedagem de código-fonte e colaboração que utiliza o sistema de controle de versões Git. Permite o gerenciamento de projetos, versionamento de arquivos e trabalho colaborativo entre desenvolvedores.

**GitHub Copilot:** Ferramenta de inteligência artificial desenvolvida pela GitHub e OpenAI, integrada ao editor de código, que sugere trechos de código, funções e soluções automaticamente, acelerando o desenvolvimento e auxiliando na escrita de código.

**VS Code:** Visual Studio Code é um editor de código-fonte leve, gratuito e multiplataforma, amplamente utilizado por desenvolvedores. Oferece suporte a diversas linguagens de programação, extensões e recursos avançados para desenvolvimento de software.


## Preparação do Ambiente

Para começar a utilizar as ferramentas apresentadas nesta oficina, siga os passos abaixo para configurar seu ambiente:

### 1. Instalação do VS Code

1. Acesse o site oficial do Visual Studio Code: https://code.visualstudio.com/
2. Baixe a versão adequada para o seu sistema operacional (Windows, macOS ou Linux).
3. Siga as instruções de instalação apresentadas no site.
4. Após instalar, abra o VS Code.

### 2. Criar uma conta no GitHub ou ser adicionado a um repositório existente

1. Acesse https://github.com/ e clique em "Sign up" para criar uma conta gratuita.
2. Complete o cadastro com seu e-mail, nome de usuário e senha.
3. Após criar a conta, você pode criar um novo repositório ou solicitar ao responsável pelo projeto que adicione seu usuário a um repositório existente.
4. Recomenda-se configurar o Git localmente em seu computador. O VS Code facilita essa integração, mas você pode instalar o Git manualmente: https://git-scm.com/downloads
5. No VS Code, utilize a aba "Source Control" para clonar repositórios, fazer commits e sincronizar alterações com o GitHub.

### 3. Instalação do GitHub Copilot no VS Code

1. No VS Code, clique em "Extensões" (ícone de quadrado no menu lateral ou pressione `Ctrl+Shift+X`).
2. Pesquise por "GitHub Copilot".
3. Clique em "Instalar" na extensão oficial.
4. Após instalar, será solicitado que você faça login com sua conta do GitHub.
5. Siga as instruções para autorizar o uso do Copilot. Caso não possua uma licença, é possível solicitar acesso educacional ou utilizar o período de avaliação.
6. Após a configuração, o Copilot estará disponível para sugerir códigos enquanto você digita.


## Objetivos da Oficina

Apresentar o uso da Inteligência Artificial como apoio ao desenvolvimento de soluções tecnológicas, com foco em análise de dados, monitoramento e tomada de decisão. Serão utilizados componentes de software amplamente conhecidos, como o VS Code, GitHub, GitHub Copilot, a linguagem de programação Python, o Streamlit (ambiente web/Python para criação de painéis), o R (ambiente para análise estatística) e o banco de dados DuckDB (um ambiente de gerenciamento de banco de dados local de alto desempenho para realização de consultas).
Como exemplo prático, serão explorados os microdados do sistema SAEV, contendo informações de avaliações diagnósticas, formativas e somativas nas disciplinas de Língua Portuguesa, Matemática e Leitura (fluência leitora).

### Objetivos específicos

1. Com base nos microdados exportados do SAEV (tipo de exportação: Normalizada), construir todo o processo de ETL. Os dados exportados estão no formato CSV e seguem a arquitetura Star Schema;
2. Criar um banco de dados DuckDB (para uso local) com a arquitetura Star Schema conforme orientação na seção "Estrutura de Dados";
3. Criar painéis utilizando Streamlit e Python para apresentação em navegador web;
4. Desenvolver relatórios utilizando R;
5. Debater oportunidades de melhoria do produto da oficina;
6. Discutir a possibilidade de oferecer os produtos gerados por esta oficina aos parceiros do EPV.



## Estruturas de Dados

Esta seção apresenta as estruturas de dados de entrada (microdados do SAEV) e as estruturas de saída (Banco de Dados DuckDB e tabelas).


### Arquivos de Entrada (Microdados no formato CSV)

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


### Arquivo alunos.csv

Este arquivo contém os dados pessoais do aluno, bem como a situação corrente dele. É importante destacar que a situação corrente do aluno não necessariamente coincide com a situação dele durante uma avaliação. Neste contexto, para efeito das análises da avaliação e resultados de testes, a situação corrente do aluno é pouco relevante. 

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



### Arquivo de Saída (Banco de Dados DuckDB)
