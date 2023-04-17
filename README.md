# political-bias

A Transformers-based model that classifies the political bias of Brazilian Portuguese tweets as either conservative, liberal, or neutral. This work was presented as part of a subject at system engineering and computer science and masters program.

# Methodology:
This work proposes an approach to classify political bias on Twitter by utilizing [BERTimbau](https://github.com/neuralmind-ai/portuguese-bert), a Portuguese implementation of Google's BERT, using a Post-Based Method strategy. Specifically, posts were gathered from users who had already been categorized according to their political leanings. Additionally, it was supposed that all posts made by an account were inherently aligned with the same political bias as the account's categorization. This led to the collection of 243,624 tweets, with 95,630 classified as conservative, 22,233 as neutral, and 125,761 as liberal. It should be noted that not all tweets collected from an account are necessarily related to politics.

## Results:
Accuracy: 80\%
F1-Score: 75\%

## Examples:

| **Pre-processed tweet**                                                                                                                                                                                                                                                   | **Prediction** | **Actual**   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|--------------|
| "O que há de antidemocrático em pedir o aprimoramento do processo eleitoral?"                                                                                                                                                                                             | conservative   | conservative |
| "Por ser conservador, Filipe Martins está sendo perseguido"                                                                                                                                                                                                               | conservative   | conservative |
| "O trunfo de Bolsonaro para tentar crescer na cidade de São Paulo (índice da mão traseira apontando para baixo: tom de pele médio)"                                                                                                                                       | neutral        | neutral      |
| "Meu Deus, que gente chata! Boa noite!"                                                                                                                                                                                                                                   | liberal        | liberal      |
| "Bolsonaro fala AO VIVO na Globo que acabou com a mamata da Globo! rolando de rir no chão"                                                                                                                                                                                | neutral        | liberal      |
| "Enquanto Lula louva, elogia e agradece aqueles que agridem opositores políticos para defendê-lo, o Presidente sempre deixou claro que dispensa esse tipo de  apoio. Desde 2018. A diferença entre os dois é cristalina e não comporta nenhum tipo de falsa equivalência. | liberal        | conservative |
| "(luz do carro da policia) FAMOSOS Julia Fox diz que só namorou Kanye West para que ele deixasse Kim Kardashian em paz."                                                                                                                                                  | neutral        | liberal      |
