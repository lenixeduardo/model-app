# Auditoria independente06 — aprovada visualmente

2026-11-09. Versão **1.0.0-prototipo.1**. Nota **9,28/10** (soma9,275); gate estrito>9,0 atingido, meta9,5 não atingida. Nenhum P1 material identificado. **Auditor06 concluído; planejador07 LIBERADO.** Esta decisão não inicia07 nem publica a aplicação.

## Evidência e método

O auditor abriu obrigatoriamente via view_image a referência156×404, as três capturas raw375×812,390×844,430×932 e comparacao-390.png. Leu DESIGN_SPEC, ASSETS, PLANO, README, EVIDENCIAS, relatórios final/candidato, código e script de teste. Aplicou verification-before-completion à conferência documental e executou verificações novas de dimensões, hashes, composição da comparação e RGB dos quatro crops. Todos os hashes do relatório final conferem com os arquivos atuais; a captura390 colada em[350,40,740,884] da comparação é exatamente a raw, diferença bbox=None. A referência foi ampliada proporcionalmente para326×844; a comparação tem740×884 incluindo40px de rótulo.

Não houve segunda navegação, segunda renderização nem teste independente em browser pelo auditor. Os resultados funcionais abaixo são evidências revisadas do implementador, sustentadas pelo código/testes examinados. Capturas finais são Chromium156.0.8078.79, DPR1. Candidata antiga não é evidência de aprovação: o relatório-candidato registra overflow anterior; a avaliação usa somente as finais com scrollHeight=clientHeight.

## Rubrica visual

| Critério | Peso | Nota | Parcela |
|---|---:|---:|---:|
| Fotografia, identidade e enquadramento |35%|9,60|3,360|
| Geometria e composição |25%|9,10|2,275|
| Tipografia e ícones |20%|8,80|1,760|
| Cores e contraste |10%|9,40|0,940|
| Responsividade e acabamento |10%|9,40|0,940|
| **Total** |100%|**9,275**|**9,275**|

A identidade, os três enquadramentos de retrato e o escritório correspondem à fonte, sem pessoa ou cenário novos. Conferência independente: zero diferenças RGB em todos os pixels alpha>0 dos quatro PNGs comparados aos respectivos boxes do JPEG oficial. Avatares recebidos18×19 permanecem separados e proporcionais45×47,5 em390; header≈55×55; escritório335×110 mantém134/44. O desfoque provém da ampliação de fotografias muito pequenas e não de detalhe maior disponível.

Conversa, card, header e compositor conservam a hierarquia e os principais alinhamentos da fonte. Em390 os balões iniciam aproximadamente y130/232/641, e o card y345; correspondem às âncoras verticais. Todos os textos, quebras, horas10:24/10:25/10:29, Enzo26, Online agora, localização/duração/cachê e CTA estão presentes e legíveis. Arial nativa e pictogramas reconstruídos mantêm o caráter simples; cores marfim, cinza quente e preto coerentes. Nas três capturas todo o estado inicial cabe, sem clipping, balões sobrepostos, corte de metadados ou composer encobrindo a hora final.

## P2 e limites visíveis

- Escritório proporcional tem110px em390 contra≈92px ao escalar verticalmente a referência. A linha inferior da foto passa de alvo≈437 a≈455; título e primeiros metadados ficam≈14–20px abaixo. O conteúdo interno foi compactado, mantendo base do card≈630 contra alvo≈627. Diferença visível, mas preserva fotografia, dados, CTA e leitura; não constitui P1. Não corrigir por estiramento da foto.
- Último avatar está aproximadamente20px acima da posição proporcional vertical da fonte: ref topo325×844/404≈679, render≈659. Fica na altura da primeira linha do último balão, enquanto a referência o situa mais próximo da segunda. Primeiro avatar e header estão coerentes; nenhuma troca de retrato.
- Fonte dos balões e metadados parece mais regular/leve e ligeiramente menor que os contornos engrossados da referência JPEG ampliada; CTA mais nítido e caixa um pouco mais alta. Não há motivo para rasterizar textos para imitar compressão.
- Clipe e avião possuem traços mais contrastados e desenhos menos delicados; calendário/cachê/opções são aproximações já declaradas. A baixa resolução impede afirmar o desenho exato do miolo do cachê.
- Painel implementado ocupa viewport integral sem a borda externa arredondada do recorte de apresentação. Mantém o conteúdo e as margens internas; diferença de acabamento.

## Evidência funcional revisada

Relatório final e render.py cobrem cada viewport: quatro fotos carregadas, document=viewport, conversa624/624,649/649 e717/717, alvos>=44px e ausência de erros de console/rede externa. Cinco dialogs são acionados por teclado, Tab permanece no fechar, Escape restaura foco. Retorno é link real para05. Vazio é ignorado; comum/literal HTML/longo criam uma bolha por envio, input conserva foco, longo produz scroll interno, reload restaura a conversa original. Código usa textContent, memória local transitória, sem fetch/backend/upload/chamada/resposta ou recibo de entrega. Novas mensagens não recebem horário ou indicação fictícia.

Contexto separado de fallback bloqueia quatro PNGs e usa reduced-motion: relatório registra compositor/dialog utilizáveis. O auditor confirmou a implementação CSS/JS correspondente; não repetiu o contexto. O teste não prova falha de todos os SVGs, zoom de texto extremo, safe-area física, teclado virtual móvel ou todos os leitores de tela. Fallback não conserva fotografia ausente e a foto aberta em dialog não tem listener próprio de falha: limitação técnica secundária, fora do estado normal avaliado. Não alegar cobertura universal de acessibilidade.

## Hashes das evidências avaliadas (SHA256)

| Arquivo | SHA256 |
|---|---|
| referência06 |e26142ed93c525807ef91392d9dd5479c4e49eecd8614e0c2dbf28f027b188dc|
| screenshots/375x812.png |28f64c6b1955907564a1daaf391bdd9328fb3ae5f3fbe93c91d56827e044a38f|
| screenshots/390x844.png |aac6d46f3c49e1a96184c56671008a8102e664734fab12f6670ec8f1c088788f|
| screenshots/430x932.png |8116aac22690ba216934e1d6cddb417217a59bfe4c86b90226b052d34cc49e2e|
| comparacao-390.png |eb681be84a7c2211ad0591b6cefb2c747a7972d4ea90cf0e94bc341c502b492a|

Código, assets e capturas não foram editados nesta auditoria.03/04/05 preservadas. A nota é estimativa visual independente, não métrica pixel-perfect automatizada, e não se transfere à07.
