# Respostas do Trabalho - Pipeline de ML

## Identificação do Grupo

- **Integrantes:**
  - Filipe Ribeiro de Oliveira
  - Luis Eduardo Paes Salomão
  - Rômulo Ribeiro Moreira

---

## Parte 1: Resultados do Pipeline

### 1.1 O pipeline executou sem erros?

<!-- Marque com X a opção correta -->

- [x] Sim
- [ ] Não

### 1.2 F1-Score obtido:

<!-- Copie o valor exibido ao final da execução -->

```
F1-Score: 0,4043
```

### 1.3 Cole aqui o output final do pipeline:

<!-- Execute: python main.py e copie a saída -->

```
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
INICIANDO PIPELINE DE ML
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀


[ETAPA 1/4] Carregando dados...
==================================================       
              1. CARREGANDO DADOS
==================================================       
✅ Dados carregados do arquivo: data/clientes_campanha.csv

==================================================       
              EXPLORAÇÃO DOS DADOS
==================================================       

2. DATASET SHAPE
------------------------------
Shape:
    Linhas: 5000
    Colunas: 8


3. TIPOS DAS COLUNAS
------------------------------
cliente_id              int64
idade                   int64
renda_mensal          float64
tempo_conta_meses       int64
num_produtos            int64
tem_cartao_credito      int64
score_credito         float64
respondeu_campanha      int64
dtype: object


4. PRIMEIRAS 5 LINHAS DO DATAFRAME
--------------------------------------------------------------------------------------------------------------------------
   cliente_id  idade  renda_mensal  tempo_conta_meses  num_produtos  tem_cartao_credito  score_credito  respondeu_campanha
0           1     56      46917.46                229             4                   1          600.0                   1
1           2     69      41274.41                  9             3                   0          758.2                   0
2           3     46      40649.98                 25             2                   1          595.7                   1
3           4     32      44336.79                217             5                   1          584.3                   0
4           5     60      35301.68                225             4                   0          797.8                   0


==================================================
              DISTRIBUIÇÃO DO TARGET
==================================================


5. CONTAGEM DO TARGET
------------------------------
respondeu_campanha
0    2803
1    2197
Name: count, dtype: int64


6. PROPORÇÃO DO TARGET
------------------------------
respondeu_campanha
0    0.5606
1    0.4394
Name: proportion, dtype: float64

[ETAPA 2/4] Validando dados...
Validando dados...
✅ Dados válidos!

[ETAPA 3/4] Treinando modelo...


==================================================
              PREPARANDO DADOS
==================================================

                              VETOR X

    idade  renda_mensal  tempo_conta_meses  num_produtos  tem_cartao_credito  score_credito
0     56      46917.46                229             4                   1          600.0
1     69      41274.41                  9             3                   0          758.2
2     46      40649.98                 25             2                   1          595.7
3     32      44336.79                217             5                   1          584.3
4     60      35301.68                225             4                   0          797.8
...

 VETOR y

 0    1
1    0
2    1
3    0
4    0
Name: respondeu_campanha, dtype: int64
...
Dados de treino: 4000 registros
Dados de teste: 1000 registros
Treinando modelo...
✅ Modelo treinado!
Modelo salvo em: models/modelo_campanha.pkl

[ETAPA 4/4] Avaliando modelo...

==================================================
RESULTADOS DA AVALIAÇÃO
==================================================

📊 MÉTRICAS:
   Accuracy:  0.5550 (55.50%)
   Precision: 0.4951
   Recall:    0.3416
   F1-Score:  0.4043

📋 MATRIZ DE CONFUSÃO:
   Verdadeiros Negativos (TN): 404
   Falsos Positivos (FP):      154
   Falsos Negativos (FN):      291
   Verdadeiros Positivos (TP): 151

==================================================
🎯 F1-SCORE FINAL: 0.4043
==================================================

✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
PIPELINE CONCLUÍDO COM SUCESSO!
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅

📝 Anote o F1-Score no arquivo RESPOSTAS.md: 0.4043
```

---

## Parte 2: Interpretação dos Resultados

### 2.1 O modelo é bom ou ruim? Por quê?

O F1-Score de 0.4043 está abaixo de 0.5. Isso indica que o modelo não está conseguindo capturar padrões suficientes para distinguir as classes de forma eficaz, sendo considerado fraco.

<!-- Considere: F1 de 0.5 seria jogar moeda. Acima de 0.5 = melhor que aleatório. -->

### 2.2 O dataset é balanceado ou desbalanceado? Como você descobriu?

O dataset é considerado balanceado pois a coluna target 'respondeu_campanha' possui uma distribuição de classes relativamente uniforme, com a proporção 56%/43%.

| respondeu_campanha |  %     |
| ------------------ |--------|
| 0                  | 0.5606 |
| 1                  | 0.4394 |

<!-- Dica: veja a proporção da variável target na exploração dos dados -->

### 2.3 Por que usamos F1-Score e não apenas Accuracy neste caso?

Quando olhamos simplesmente para a Accuracy, com a proporção de "respondeu" e "nao respondeu", caso o modelo previsse para todos os casos como não respondeu, acertaria 56% das vezes, o que pode ser considerado aceitavel. Utilizando o F1, que é a media harmônica entre o Precision e o Recall, no cenário de prever tudo "não respondeu" o F1 seria 0. 

Portanto o F1 evita modelos burros que apenas preveem a classe majoritaria, nos obrigando a ter um bom desempenho tanto em acertar quem vai responder a campanha (precision) sem deixar ninguem pra trás (recall).

<!-- Dica: pense no que aconteceria se o modelo previsse sempre 0 -->

---

## Parte 3: Validação de Dados

### 3.1 Liste as validações Pandera que você implementou:

<!-- Descreva cada validação que você adicionou -->

1. cliente_id: int, nullable=False, unique=True
2. idade: int, Check.in_range(18, 80)
3. renda_mensal: float, Check.in_range(1000, 50000)
4. score_credito: float, Check.in_range(300, 850)
5. respondeu_campanha: int, Check.isin([0, 1])

### 3.2 Por que validar dados ANTES de treinar o modelo?

Para garantir segurança e confiabilidade do modelo, evitando que dados inválidos o contaminem e previnindo as previsões erradas, o que pode afetar o ambiente produtivo.

<!-- Pense no contexto de produção: o que aconteceria se dados inválidos entrassem no modelo? -->

---

## Parte 4: Versionamento

### 4.1 Liste os commits que vocês fizeram (copie do git log):

```
0a97f0d (HEAD -> main, origin/main, origin/HEAD) fix import
3053f22 Merge branch 'main' of https://github.com/romulorm/trabalho-final-pipelines
bfd6ccc Inicio das respostas.md e cosmetico no carregar.py
a2d5945 RESPOSTAS update
ac1d6b4 Update validar.py
7d8ff63 Atualiza treinar.py com correções da fonte do modelo
b2b1dac Atualiza carregar.py e treinar.py com correções da fonte do CSV
d4da95e Evitar sincronizar os modelos com o git
4080934 treinar.py Completo
2dc18de Alteração da didatica do Shape do DATASET
fec5871 Merge branch 'main' of https://github.com/romulorm/trabalho-final-pipelines
5875654 Alteração do caminho para o .csv
52ae6a9 carregar.py update
e2d4d8c carregar.py concluído
262bdbf commit inicial
```

### 4.2 Por que mensagens de commit descritivas são importantes?

É importante para poder localizar o código em um momento anterior, caso precise consultar ou até mesmo retornar ao seu estado anterior.

---

## Parte 5: Reflexão (Opcional)

É um pipeline muito interessante que pode ser utilizado para predições em diversas áreas.

### 5.1 Qual foi a maior dificuldade do grupo?

Entender os passos de cada etapa.

### 5.2 O que vocês fariam diferente se fossem refazer?

Seria interessante utilizar o stratify=y no treinamento para garantir a mesma proporção entre as classes nos conjuntos de treinamento e teste. Com a adição do stratify e a alteração do tamanho do conjunto de teste para 30%, o F1-Score aumentou para 0.4510.

**Data de entrega:** 15/12/2025
