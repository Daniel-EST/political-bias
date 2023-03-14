# political-bias

A Transformers-based model that classifies the political bias of Brazilian Portuguese tweets as either conservative, liberal, or neutral. This work was presented as part of a subject at computer and system engineering masters program.

# Methodology:
TODO

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
