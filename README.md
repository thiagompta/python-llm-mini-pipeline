📌 Desafio Final — Pipeline de Processamento de Resenhas com LLM Local

Este projeto implementa um pipeline completo em Python para leitura, processamento, análise de sentimento e agregação de resenhas de usuários utilizando um modelo de linguagem rodando localmente (LM Studio).

O desafio foi desenvolvido utilizando uma IDE e segue todas as etapas propostas no enunciado, desde a leitura de arquivos .txt até a geração de arquivos finais categorizados por sentimento.

🧠 Objetivo do Desafio

Construir um pipeline que:

Leia um arquivo .txt, onde cada linha representa uma resenha.

Envie cada resenha para um LLM local para:

Classificar o sentimento (Positiva, Negativa ou Neutra)

Traduzir a resenha para PT-BR

Retornar os dados em JSON válido

Transforme a resposta do modelo em estruturas Python.

Conte a quantidade de avaliações por sentimento.

Una os textos processados em arquivos .txt, separados por sentimento.

📂 Estrutura do Projeto
PYTHON-IA/
│
├── chamada-ao-llm.py        # Script principal do pipeline
├── mini-pipeline.py        # Versão simplificada / experimental
├── Resenhas.txt             # Arquivo de entrada (resenhas brutas)
├── resenhas.csv             # Dados processados (persistência)
├── positivas.txt            # Resenhas positivas agregadas
├── negativas.txt            # Resenhas negativas agregadas
├── neutras.txt              # Resenhas neutras agregadas
├── venv/                    # Ambiente virtual
└── README.md                # Documentação do projeto

📄 Formato do Arquivo de Entrada (Resenhas.txt)

Cada linha do arquivo deve seguir o padrão:

id$nome$review


Exemplo:

1$João$The product is very good and arrived fast

⚙️ Tecnologias Utilizadas

Python 3.10+

Pandas

JSON

OpenAI SDK

LM Studio (modelo local)

IDE (VSCode)

🔗 Integração com LLM Local

O projeto utiliza um modelo rodando localmente via LM Studio, configurado através do endpoint:

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

Modelo utilizado:
google/gemma-3-4b

🧩 Etapas do Pipeline
🔹 Etapa 1 — Leitura do Arquivo

Lê o arquivo Resenhas.txt

Cada linha vira um elemento de uma lista Python

🔹 Etapa 2 — Estruturação dos Dados

Transforma cada linha em um dicionário Python:

{
  "id": "...",
  "nome": "...",
  "review": "..."
}

🔹 Etapa 3 — Processamento com LLM

Para cada resenha, o modelo:

Classifica o sentimento

Traduz a resenha para PT-BR

Retorna somente JSON válido

Exemplo de retorno esperado:

{
  "id": "1",
  "nome": "João",
  "review": "The product is very good",
  "review_pt_br": "O produto é muito bom",
  "sentimento": "Positiva"
}

🔹 Etapa 4 — Validação e Parsing

Remove possíveis artefatos do modelo

Converte o JSON em dicionários Python

Trata erros de parsing

🔹 Etapa 5 — Persistência

Os dados processados são salvos em resenhas.csv

Possibilidade de evitar novas chamadas ao LLM usando a flag:

GERAR_COM_LLM = False

🔹 Etapa 6 — Análise com Pandas

Função responsável por:

Contar resenhas positivas, negativas e neutras

Retornar:

Quantidades

DataFrames separados por sentimento

🔹 Etapa 7 — Agregação de Texto

Une as resenhas traduzidas (review_pt_br)

Usa o separador #####

Gera três arquivos finais:

positivas.txt

negativas.txt

neutras.txt

📊 Saída Esperada no Terminal
Positivas: X
Negativas: Y
Neutras: Z

✅ Requisitos Atendidos do Desafio

✔ Leitura de arquivo .txt
✔ Conversão para lista Python
✔ Uso de LLM local
✔ Retorno em JSON
✔ Parsing e validação
✔ Contagem de sentimentos
✔ Agregação de texto com separador
✔ Persistência em CSV

🚀 Observações Finais

O projeto prioriza robustez, validação de dados e controle de custo, evitando chamadas desnecessárias ao modelo.

A arquitetura permite fácil extensão para outros tipos de análise.

Ideal para pipelines de NLP, análise de sentimento e automação com LLMs locais.