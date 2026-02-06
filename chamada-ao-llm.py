from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)
resposta = client.chat.completions.create(
    model= "google/gemma-3-4b",
    messages=[
        {"role":"system", "content": "Sera direto, não usará listas e poucas palavras. e respondera em portugues"},
        {"role":"user", "content": "O que é AI Generativa?"}
    ],temperature=1.0,)
print(resposta.choices[0].message.content)