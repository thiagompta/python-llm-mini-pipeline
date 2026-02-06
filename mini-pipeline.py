from openai import OpenAI
import json
import pandas as pd


client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def gerar_resenhas():
    resenhas_processadas = []
    resenhas = []
### ETAPA 1 — Leitura do arquivo
    with open("Resenhas.txt", "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.split("$")
            if len(partes) != 3:
                continue 

            user_id, user_name, review = partes
########### ETAPA 2 — Estruturação em Python             
            resenhas.append({
                "id": user_id.strip(),
                "nome": user_name.strip(),
                "review": review.strip()
            })
### ETAPA 3 — Processamento com LLM
    for linha in resenhas:
        response = client.chat.completions.create(
            model="google/gemma-3-4b",
            messages=[
                {"role": "system", "content": "Você é uma API. Retorne somente JSON válido. Nunca use markdown,não use vírgula após o último campo listas ou texto fora do JSON."},
                {"role": "user", "content": f"""
            Analise a resenha abaixo.

            TAREFAS:
            1. Classifique o sentimento em um dos tipo: Positiva, Negativa ou Neutra. Nunca repita. 
            2. Traduza a resenha para português do Brasil.
            3. Retorne APENAS um JSON válido.

            FORMATO:
            {{
            "id": "{linha['id']}",
            "nome": "{linha['nome']}",
            "review": "{linha['review']}",
            "review_pt_br": "...",
            "sentimento": "Positiva | Negativa | Neutra"
            }}
            RESENHA:
            {linha['review']}
            """}
                    ],
                    temperature=0
                )
####### ETAPA 4 — Validação e Parsing        
        conteudo = response.choices[0].message.content
        conteudo = conteudo.replace("```json","").replace("```","")
        try:
            resultado = json.loads(conteudo)
            resenhas_processadas.append(resultado)
        except json.JSONDecodeError:
            print("Erro ao converter JSON:")
            print(conteudo)
            break
    return resenhas_processadas
# Se True, gera os dados usando a LLM.
# Se False, carrega os dados já salvos em CSV (evita novas chamadas à LLM).
GERAR_COM_LLM = False 
# ETAPA 5 — Persistência
if GERAR_COM_LLM:
    dados = gerar_resenhas()
    df = pd.DataFrame(dados)
    df.to_csv("resenhas.csv", index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv("resenhas.csv")

# ETAPA 6 — Análise com Pandas
def contagem(df):
    positivas = df[df['sentimento'] == 'Positiva']
    negativas = df[df['sentimento'] == 'Negativa']
    neutras   = df[df['sentimento'] == 'Neutra']
    return {"quantidades":{"positivas": len(positivas), "negativas": len(negativas),"neutras": len(neutras),}, "positivas": positivas,"negativas": negativas,"neutras": neutras}

resultado = contagem(df)
print("Positivas:", resultado["quantidades"]["positivas"])
print("Negativas:", resultado["quantidades"]["negativas"])
print("Neutras:", resultado["quantidades"]["neutras"])
# ETAPA 7 — Agregação de Texto
positivas_texto = "#####".join(resultado["positivas"]["review_pt_br"].tolist())
negativas_texto = "#####".join(resultado["negativas"]["review_pt_br"].tolist())
neutras_texto = "#####".join(resultado["neutras"]["review_pt_br"].tolist())
with open("positivas.txt", "w", encoding="utf-8") as f:
    f.write(positivas_texto)
with open("negativas.txt", "w", encoding="utf-8") as f:
    f.write(negativas_texto)
with open("neutras.txt", "w", encoding="utf-8") as f:
    f.write(neutras_texto)
#print(positivas_texto)
#print(negativas_texto)
#print(neutras_texto)

