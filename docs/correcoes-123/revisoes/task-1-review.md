# Revisão independente — tarefa 1

Commit revisado: `a82f1790e0eb1bb05952d25958ed44656ee4923b`, diff `b49b77d..a82f179`. Revisão estática do diff, referências, seis capturas reais e duas comparações. Runtime, assets, capturas e Git não foram alterados. Os quatro testes GREEN do implementador foram considerados como evidência relatada; não foram repetidos. A revisão não abrange backend, estado compartilhado nem a tarefa posterior de acessibilidade.

## Veredictos

- **Spec compliance: REQUEST CHANGES.** Entrada demonstrativa, rotas nomeadas, jornadas principais, entradas Salvos/Notificações e retorno explícito de 06/10 estão implementados. Entretanto, o aceite inclui fidelidade visual >9,0 e comparação proporcional; ambos ainda falham.
- **Code/implementation quality: REQUEST CHANGES.** Nenhum defeito crítico novo de navegação encontrado no diff. As falhas importantes são visuais e na evidência de comparação, detalhadas abaixo.
- **Gate visual: REPROVADO. Tela 01: 8,17/10; tela 02: 6,76/10.** Não há autorização para avançar com essas notas. Meta 9,5; aprovação exige estritamente >9,0 por tela.

## Achados

### Important — 02 remove fotografia disponível em faixas inteiras

`MODEL_assets_v1/extrair_entrada.py:11` e `MODEL_tela_02_V1/styles.css:1`.

As máscaras `(0,115,106,155)`, `(0,72,78,110)`, `(0,79,106,116)` e `(0,125,78,162)` descartam aproximadamente 23–35% da altura dos recortes. Nas três larguras isso produz cortes horizontais abruptos: Enzo perde torso; Gabriel perde gola/roupa; Theo perde camisa e peito; Rafael perde a continuação do casaco. Não é apenas falta de resolução: os pixels estão presentes na referência e foram removidos. A referência tem texto sobre fotografia contínua; a implementação tem fotografia sobre grandes rodapés quase pretos.

Correção viável com os assets existentes: refazer os quatro crops integrais das mesmas coordenadas e preservar seus RGB, mascarando somente regiões pequenas de UI raster e usando rótulos/ícones nativos co-registrados. Bboxes globais iniciais em `02-descoberta.png` (199×404), a refinar visualmente antes da exportação: Enzo nome/verificado `(11,208,71,223)`, cidade `(11,224,73,238)`, bookmark `(93,219,107,237)`; Gabriel nome `(119,166,173,180)`, cidade `(119,181,193,194)`; Theo nome `(11,331,57,345)`, cidade `(11,346,88,360)`; Rafael nome `(119,331,172,345)`, cidade `(119,346,174,360)`, bookmark `(175,340,190,359)`. Não apagar novamente toda a largura/altura residual. Cobertura opaca pequena sob UI nativa pode ocultar o raster sem inventar fotografia, mas deve ser auditada quanto à naturalidade.

Investiguei `originais/mockup-geral.jpg`, as fontes/recortes 03, 04, 05 e 09. O recorte maior `03/assets/enzo-swipe-referencia.png` preserva a mesma pose de Enzo e pode auxiliar se o alinhamento for demonstrado. `05/assets/foto-01-camisa-aberta.png` mostra a foto de camisa usada no card Theo02, porém os rótulos entre telas são inconsistentes: não concluir identidade pelo nome do arquivo. As quatro fotos09 são outras poses; não substituí-las por igualdade de nome. `originais/login-referencia.jpg` também é outra fotografia/composição. Não há necessidade comprovada de pedir nova foto para resolver as faixas: os próprios crops02 contêm a maior parte dos pixels necessários. As áreas exatamente sob texto raster continuam sendo uma limitação real, que não autoriza inpainting ou distorção.

### Important — 01 perde continuidade do ombro e comprime os controles

`MODEL_assets_v1/extrair_entrada.py:6` e `MODEL_tela_01_V1/styles.css:1`.

O crop termina em y=205 da referência, antes do logotipo. A camada `.portrait` termina em 55% da altura, e o gradiente escurece a região antes disso. A referência conserva o ombro/fundo atrás e abaixo do logotipo; a captura termina em preto homogêneo. A pessoa e a proporção do rosto são preservadas, mas a composição fotográfica fica mais curta. Pode-se extrair uma área maior da mesma referência, mantendo somente regiões fotográficas e mascarando UI raster pontualmente, sem usar a tela inteira como fundo e sem gerar corpo.

Em 390×844, o botão Entrar aparece aproximadamente y=590–636 em vez do intervalo proporcional y=625–678; o Criar conta fica ~42 px acima e o contratante ~58 px acima. Os botões têm 46–48 px fixos, versus cerca de 52 px na referência proporcional. Tagline, textos dos botões e status ficam pequenos; a diferença aumenta em430 porque esses tamanhos ficam fixos. Recalibrar usando coordenadas da referência188×404: topo dos botões aproximadamente y=299 e331, contratante y=374; escalar alturas, fontes e espaçamentos de forma coerente. A face está razoavelmente alinhada; não corrigir o bloco inferior esticando o retrato.

### Important — a comparação02 distorce a referência

`.superpowers/sdd/correcao-123/task-1-report.md:10` e `docs/correcoes-123/capturas/02-comparacao-390.png`.

A referência199×404 foi redimensionada para390×844. Verifiquei igualdade exata dos pixels da metade esquerda com `PIL.resize((390,844), BICUBIC)`. Os fatores horizontal e vertical são1,9598 e2,0891, diferença de6,60%; isso alonga rostos/corpos na evidência. Para uma comparação proporcional por largura, usar390×791,76 (arredondado792), preservando a razão e explicitando a área adicional do viewport; alternativamente comparar regiões equivalentes com escala uniforme. A referência01 também deve manter razão188:404 (390×838,09) em vez de esticar até844. A classificação abaixo considera as referências originais abertas separadamente, não pressupõe que a metade esquerda deformada seja a geometria correta da fotografia.

### Important — 02 reduz a hierarquia de tipografia/ícones

`MODEL_tela_02_V1/styles.css:1`, `MODEL_tela_02_V1/styles.css:9`, `MODEL_tela_02_V1/index.html:1`.

Chips, nomes, cidades e ícones usam tamanhos fixos, enquanto os cards crescem. Na referência, os chips têm cerca de20 px de altura para199 px de largura; no alvo390 correspondem a~39 px, contra~28 px da captura. Por isso Editorial passa a caber completamente e a fileira perde a escala/hierarquia original. As cidades de11 px e nomes de15 px estão menores que o proporcional da fonte. A grade ocupa a área geral esperada, mas a barra inferior tem desenho de Home vazado em vez do ativo preenchido e os dois controles do header foram trocados por sliders/reticências. Reusar SVG compatível/estado ativo; manter as ações de filtros e menu em controles que preservem a composição original. Redimensionar tokens de tipografia e UI proporcionalmente, sem aumentar ou estreitar as fotografias para compensar.

## Rubrica visual

Notas abaixo usam subnotas de0–10 e pesos foto35%, geometria25%, tipografia20%, cores10%, responsividade10%. São julgamento visual independente, não medição automática de similaridade.

| Tela | Foto35 | Geometria25 | Tipografia20 | Cores10 | Responsividade10 | Total |
|---|---:|---:|---:|---:|---:|---:|
|01|8,3|8,0|7,4|9,0|8,8|**8,17**|
|02|5,2|8,0|6,3|7,8|9,0|**6,76**|

01: rosto e pose originais reconhecíveis e sem alongamento evidente; perda do ombro/fundo e deslocamento dos CTAs impedem aprovação. 02: quatro pessoas presentes e proporção intrínseca preservada; áreas fotográficas ausentes por máscara impedem aprovação mesmo sem foto inteiramente ausente. Não encontrei evidência de pessoa gerada ou reconstrução no script. As três larguras mantêm a estrutura sem overflow horizontal visível; isso não compensa fotografia ou hierarquia incorretas. UI textual é nativa e ícones são SVG, preservando a possibilidade de corrigir escala sem rasterizar controles.

## Evidências e hashes SHA-256

Os hashes identificam exatamente as imagens abertas nesta revisão; qualquer alteração requer captura/evidência nova e nova auditoria.

- `MODEL_assets_v1/referencias/01-splash.png`: `ee9b8b3511592c36c66bd8da1b9d6936aeb0c1264b6fb97bdb8d830017126f80`
- `MODEL_assets_v1/referencias/02-descoberta.png`: `a152aeca87a53a5a1890f0bc04a9710bb7838741c076f999e3fa5c1d1a6d0a39`
- `docs/correcoes-123/capturas/01-375.png`: `8aa539cfdeeb1f14020d12a09a283f0a7ba6bc82a1ba3212d2f9552996b9643b`
- `docs/correcoes-123/capturas/01-390.png`: `aaed97968d17ddbecf48bd1ed522b1e33c2227d1f58d5de3a99d6ce880c635c9`
- `docs/correcoes-123/capturas/01-430.png`: `f5b30d91329121374df5cc83c5eb54e00cc24a7878e0962121764db4909cce80`
- `docs/correcoes-123/capturas/01-comparacao-390.png`: `e34fc0321eeffdc922fc1ef960c9377932412dd48b25ac670f25da357aa8665b`
- `docs/correcoes-123/capturas/02-375.png`: `e72b015e7cce26bfa37c058856bd56cac870494f28d9c1af9661d5a6f8726677`
- `docs/correcoes-123/capturas/02-390.png`: `b89167b5422fc64a70552293a5205c8660e41066128f7128802765d430a9a97d`
- `docs/correcoes-123/capturas/02-430.png`: `a8b688c5afaf24e6d6d2fd595a4cf35adecd2f8e431e977ee9401bcf74952e76`
- `docs/correcoes-123/capturas/02-comparacao-390.png`: `967a75091ffe9904adcd13d24f5d05cd6d2b0bf60a008921412e7dc2f7bb194c`
