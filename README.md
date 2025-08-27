
# Oficina de IA SAEV2


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




