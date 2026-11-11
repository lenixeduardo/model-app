# Auditoria independente07 — APROVADA VISUALMENTE

Data: 2026-11-11. Versão avaliada: **1.0.0-prototipo.2**. Nota **9,32/10**, soma ponderada **9,315**. Gate estrito **>9,0 atingido**, meta9,5 não atingida. **Nenhum P1 material. Auditor07 concluído; planejador08 LIBERADO.** A decisão da V1 foi8,76 e permanece histórica; esta avaliação usa exclusivamente as novas capturas V2.

## Escopo da reauditoria

Referência oficial201×317, três novas capturas375×812/390×844/430×932 e comparação390 foram novamente abertas por `view_image`. CHANGELOG.md, EVIDENCIAS.md, relatorio-browser.json e SHA256SUMS atuais foram lidos; conferidos CSS/JS relativos à correção. A V1 não serve de prova visual da V2. O auditor não alterou código, assets ou capturas, não publicou e não iniciou08.

Pillow confirmou novamente: painel RGB idêntico ao crop global[11,434,212,751]; zero diferenças RGB nos pixels alpha>0 das três fotografias perante o JPEG oficial; hashes das fotos iguais ao manifest. Fotografias independentes62×59/62×64/62×65, sem geração de anatomia, troca de pessoa ou títulos/metadados incorporados. Resolução baixa, cantos geométricos conservadores e matte JPEG residual permanecem documentados.

## Rubrica visual independente

| Critério | Peso | Nota | Parcela |
|---|---:|---:|---:|
| Fotografia, identidade e enquadramento |35%|9,60|3,360|
| Geometria |25%|8,90|2,225|
| Tipografia, ícones e chips |20%|9,20|1,840|
| Cores, contraste e sobreposição |10%|9,60|0,960|
| Responsividade e acabamento |10%|9,30|0,930|
| **Total** |100%|**9,315 → 9,32**|**9,315**|

A correção resolve o bloqueador sem transferir nota anterior: os três frames agora preservam cabeça, ombros, casaco/regata/camisa e torso conforme o original. Não há o zoom adicional provocado por cover; a escala é uniforme. A baixa definição é inerente aos assets62px, não substituição ou reconstrução. Arestas laterais e inferiores visíveis voltaram ao frame. O raio CSS ainda pode suavizar uma faixa periférica minúscula no canto, sem perda material de pessoa ou cenário; não se certifica cada pixel da máscara como integral na rasterização do browser.

Header Castings/mais, quatro filtros com Todos ativo, três títulos/cidades/datas/chips/cachês nativos e cinco ícones da navegação permanecem corretos. Topos aproximados das fotos em390:173/375/583px. Os novos frames120×114/124/126 seguem proporções naturais; não alongam pessoas para cobrir toda a altura das rows. Títulos e metadados mantêm suas âncoras e não colidem com bookmarks.

## P1 da V1 resolvido e P2 remanescentes

- **Resolvido:** `.photo{height:auto;object-fit:contain}` e dimensões intrínsecas no elemento retiram o crop de27–28% da largura. O relatório atual registra fração visível1,0 em todas fotos/viewports e erro de razão<0,007, explicado por dimensões arredondadas. Em390, alturas114/124/126 substituem157/169/175. A comparação e as três capturas mostram as bordas/pessoa coerentes com essa medição; não há estiramento por eixos.
- **P2 geométrico:** preservar altura intrínseca em viewport mais estreito torna fotos mais baixas que suas rows de157/169/175px. Em390, as bases ficam aproximadamente287/499/709px, enquanto metadados/chips/cachês continuam até326/539/753px. Há respiro vazio abaixo da fotografia e mais separação entre fotos. É adaptação visível da proporção201×317 para390×844, aceita sem fingir equivalência de geometria; explica a nota8,90 de geometria. Manter todos os pixels da pessoa tem precedência sobre preencher a altura por distorção/crop.
- **P2 tipográfico:** fontes nativas, tamanhos e rasterização diferem da referência pequena; chips/ícones locais têm traço mais limpo e alguns símbolos visualmente menores. Calendário/cachê originais são diminutos demais para confirmar cada traço. Nenhum texto foi rasterizado para mascarar essa diferença.
- **Resolvido:** hash antigo da comparação no JSON. Todos os hashes inventariados no JSON atual coincidem com arquivos atuais e SHA256SUMS passa integralmente.

## Verificação técnica e limites

Foram revisados resultados atuais do implementador no Chromium156.0.8078.79/DPR1: filtros3/1/1/2, save isolado on/off, reset ao reload, cinco dialogs com Enter/Tab/Escape e foco inicial/restaurado, links reais03/06. Documento=viewport nos três tamanhos, imagens carregadas, console/rede HTTP/pedidos externos zerados no contexto normal; alvos medidos≥44×44. Falha das três fotos e reduced-motion são verificações em contexto separado, com dialog operacional. Estado local em memória, sem candidatura/backend/envio externo. A regressão geométrica registrou RED da V1 e GREEN da V2; o primeiro RED histórico de implementação comprovou somente ausência do HTML, limite já documentado.

O auditor **não executou segunda renderização ou navegação independente de browser**. Interações, fallback e foco são resultados revisados do script/log atual, não retestes próprios. Não há certificação de aparelho físico, VoiceOver, toque real, todos navegadores ou safe-area com notch. A inspeção visual própria e verificações de RGB/hashes/colagem são independentes desses logs.

## Imagens V2 avaliadas e integridade

| Arquivo | Dimensões | SHA256 |
|---|---|---|
| captura-375.png |375×812|95d5074ee48416bd5355261a8aefecaaf7d7a49d30addb229861d62f7bd2b319|
| captura-390.png |390×844|75f1e5a0bfa75969a3a3c191348cb4411c15105b21c7c592425ec871e144776b|
| captura-430.png |430×932|f1b3770b97715590aa28fa10a397a3f197d96d3ee7f85e77902891a105824712|
| comparacao-390.png |949×874|043fa05940c7ed31b163b88c3826530438d17307c948e5d739f47c99c78e6486|

Bloco direito da comparação[559,30,949,874] RGB idêntico à captura390 atual. Referência ampliada à altura844 e screenshot mantêm suas proporções individuais;30px de cabeçalho externo não integram a tela. Capturas raw DPR1 declaradas pelo procedimento de browser, sem retoque observado ou nova geração pelo auditor.

**Decisão final da V2: APROVADA VISUALMENTE9,32/10.07 concluída; planejador08 liberado.03–06 aprovadas preservadas, nenhuma publicação ou implementação08 nesta auditoria.**
