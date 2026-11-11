# Evidências de implementação07

Versão1.0.0-prototipo.2; Chromium 156.0.8078.79, Playwright Python, DPR1. Comandos: `python MODEL_tela_07_V1/render.py --candidate`, depois `python MODEL_tela_07_V1/render.py` e `python MODEL_tela_07_V1/compare.py`. Servidor HTTP serve raiz do repositório.

Antes do HTML, `render.py` falhou com `AssertionError: HTML absent: TDD red`. Limite do primeiro RED: ele verificou ausência de HTML; os casos comportamentais completos foram acrescentados durante a implementação, portanto não se afirma uma fase RED completa para cada comportamento. Durante execução, casos de foco identificaram falta de contenção explícita de Tab e corrida de restauração de foco; corrigidos usando contenção explícita e restauração nativa do dialog.

Candidata390 real aberta antes das finais; espaçamento de linhas corrigido para aproximar âncoras da fonte. Três capturas finais375×812,390×844,430×932 e comparação390 abertas. Comparação mantém fonte e captura à altura844, com proporções individuais intactas e30px de rótulo exterior.

Verificações verdes nos três tamanhos: Todos3/Moda1/Comercial1/Editorial2, save isolado on/off sem abrir detalhes, reload limpa saves e filtros, cinco dialogs por teclado, foco inicial/Tab/Escape/restauração, links reais03/06. Sem overflow do documento, imagens ausentes, console com erro, respostas HTTP400+ ou rede externa em estado normal. Todos alvos visíveis medidos >=44×44. Botão de card e bookmark são irmãos, com áreas de clique separadas. Contexto distinto verifica falha das três fotos e reduced-motion, dialog operacional.

Relatório JSON inclui viewport/documento, targets, dimensão natural/renderizada e object-fit de fotos, ações, navegador, versão e SHA256. Finais são raw PNG sem retoque; estado inicial Todos, nenhum salvo e dialogs fechados.

V2: frame integral com altura intrínseca, sem crop lateral ou do torso. A referência é201×317, proporção diferente. Fotos de62px continuam com detalhe baixo. Ícones nativos SVG são aproximações; fontes nativas não replicam rasterização do mockup. Nenhuma nota própria, publicação ou início08. Auditor independente deve avaliar fidelidade, limites e gate.

## Revisão V2 após auditoria

P1 corrigido sem refazer tipografia, ícones, cores, âncoras de cards ou navegação. `.photo` usa altura automática e proporção natural; width/height intrínsecos preservam geometria também no fallback. Três fotografias integrais, sem reconstrução. V1 e suas três capturas preservadas em `historico/1.0.0-prototipo.1/`.

Regressão de enquadramento usa dimensões naturais e caixas efetivamente renderizadas pelo Chromium para calcular fração de área-fonte visível e erro de razão. Rodou antes da correção e falhou: foto01 natural62×59 em120×157 mostrava0,727347 da fonte, erro de razão0,286516. Depois passou nos três tamanhos: fração visível1,0 em todas, erro de razão<0,015 (arredondamento a pixels inteiros), sem estiramento. Em390 os frames são120×114,120×124,120×126. Candidata V2 aberta antes das finais.

P2 corrigido: `render.py` gera comparação final antes de inventariar SHA256. JSON e SHA256SUMS conferidos contra arquivos atuais. Auditoria V1 permanece como registro histórico; V2 aguarda nova decisão independente, sem nota própria.
