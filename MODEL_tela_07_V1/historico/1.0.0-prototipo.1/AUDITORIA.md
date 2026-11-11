# Auditoria independente07 — NÃO APROVADA

Data: 2026-11-11. Versão avaliada: **1.0.0-prototipo.1**. Nota visual independente **8,76/10** (soma8,755). Gate estrito >9,0 não atingido; meta9,5. **P1 de enquadramento fotográfico presente. Tela08 permanece aguardando.**

## Escopo e evidência

O auditor abriu obrigatoriamente por `view_image` a referência oficial201×317, as três capturas375×812,390×844,430×932 e a comparação390. Leu DESIGN_SPEC.md, ASSETS.md, PLANO.md, EVIDENCIAS.md, relatório Chromium e SHA256SUMS, além do CSS/JS e scripts de reprodução. Não alterou código, assets ou capturas, não publicou e não iniciou08.

Conferência independente com Pillow: referência RGB idêntica ao crop global[11,434,212,751]; zero diferenças RGB nos pixels alpha>0 de cada uma das três fotografias comparadas aos crops do JPEG. Hashes das três fotos coincidem com manifest. São três pessoas/enquadramentos originais, sem anatomia gerada, títulos ou metadados rasterizados. A baixa resolução e o matte JPEG são limites legítimos do insumo.

Dimensões raw e hashes atuais conferidos. O bloco direito da comparação em[559,30,949,874] coincide pixel a pixel com captura390; a referência à esquerda mantém sua própria proporção. `sha256sum -c SHA256SUMS` passou integralmente. Não houve segunda execução de browser/render pelo auditor; os resultados funcionais abaixo foram revisados nos logs e no script do implementador, sem certificação de aparelho físico, toque real ou VoiceOver.

## Rubrica visual

| Critério | Peso | Nota | Parcela |
|---|---:|---:|---:|
| Fotografia, identidade e enquadramento |35%|8,00|2,800|
| Geometria |25%|8,90|2,225|
| Tipografia, ícones e chips |20%|9,20|1,840|
| Cores, contraste e sobreposição |10%|9,60|0,960|
| Responsividade e acabamento |10%|9,30|0,930|
| **Total** |100%|**8,755 → 8,76**|**8,755**|

Identidades e conteúdo estão corretos. Header Castings/mais, Todos/Moda/Comercial/Editorial, três títulos, cidades, datas, chips e cachês são nativos e correspondem à referência. A navegação conserva cinco ícones e casa ativa. Espaços verticais dos três cards e posição da tabbar acompanham bem a referência. As fotos, porém, aparecem mais fechadas: cabeça e torso aumentam em relação à largura do próprio frame, sobretudo nos cards02/03; o corpo da foto01 também perde laterais de casaco. Essa diferença é material no critério de maior peso.

## P1 — corrigir enquadramento das três fotografias

Responsável: **implementador07**, no CSS `.photo` e sua relação com a altura do card. Coordenadas aproximadas na captura390: foto01[23,173,143,330], foto02[23,375,143,544], foto03[23,583,143,758]. Frames intrínsecos62×59,62×64,62×65 estão em caixas120×157,120×169,120×175, com `object-fit:cover;object-position:center top`. Não há alongamento anisotrópico: cover escala ambos eixos igualmente. Entretanto, a altura manda no fator de escala e elimina aproximadamente27–28% da largura original. A cabeça/corpo ficam cerca de37–39% maiores do que em uma exibição integral na mesma largura. Não é um mero aumento de resolução ou uma distorção H/W dos pixels; é mudança substancial do crop/composição. A diferença persiste nos três viewports.

Correção concreta: exibir o frame original integral proporcionalmente (altura intrínseca automática/aspect-ratio correto), sem cover em caixa com razão diferente. Na largura120 da captura390, alturas integrais seriam aproximadamente114,2/123,9/125,8px, não157/169/175. Reconciliar o respiro do card com a altura da foto mantendo as âncoras, sem inventar corpo, ampliar a imagem por eixo ou trocar o asset. Se outra composição for escolhida, preservar a mesma área fotográfica original e justificar a adaptação. Nova versão, três capturas raw e comparação devem voltar à auditoria; não presumir nota após a correção.

## P2 e rastreabilidade

- Texto e chips usam fonte nativa e têm rasterização/tamanho/espessura próprios; ícones aproximados são mais limpos e alguns menores visualmente que o raster. Pequenos símbolos de calendário/cachê não são confirmáveis integralmente na fonte. Não bloqueiam isoladamente.
- Comparação atual tem hash `6a2bfdfd434f0745c4473f9855dd70fcf2994b9b7bfbc15674e21a45d9424425`, correto em SHA256SUMS, mas `relatorio-browser.json.sha256.comparacao-390.png` contém o hash anterior `e831013fb97e9619ca078b976f5aa80438cdc499e6f18a59cd4f8424d9971731`. Responsável implementador: gerar comparação antes do inventário final de hashes ou atualizar esse campo e regenerar SHA256SUMS. A colagem atual corresponde à captura final; não é evidência de imagem errada.

## Verificação técnica revisada

Relatório Chromium156.0.8078.79/DPR1 e script registram filtros3/1/1/2, save isolado on/off sem abrir detalhes, reload limpa memória, cinco dialogs com Enter/Tab/Escape e foco restaurado, links reais03/06. Estado normal: documento=viewport nos três tamanhos, imagens carregadas, zero erros de console/rede HTTP ou pedidos externos, alvos medidos≥44×44px. Contexto separado bloqueia três fotos e usa reduced-motion; dialog permanece operacional. O código sustenta estado somente em memória e mensagens honestas sem candidatura/backend/envio externo. O RED inicial comprovou ausência de HTML, sem comprovar RED completo de cada caso; limite descrito sem alterar a nota visual. Esses resultados técnicos não eliminam o P1 de fotografia.

## Hashes das imagens avaliadas

| Arquivo | SHA256 |
|---|---|
| captura-375.png |423a0eebf2b7255c48ed10ea4fb0dcee4ae834258590f4c801eda40226667369|
| captura-390.png |80542d59af3bed6c5025c1ed690d007bf1f6432783ad32f72cfa9290a155fe9d|
| captura-430.png |09f7b857d9c37737031c0ac9c319229cdea5cfc5db9be21ad87e09aba068d861|
| comparacao-390.png |6a2bfdfd434f0745c4473f9855dd70fcf2994b9b7bfbc15674e21a45d9424425|

**Decisão: auditor07 concluído; devolver ao implementador07 para correção e recaptura.08 não liberada.03–06 aprovadas não foram alteradas.**
