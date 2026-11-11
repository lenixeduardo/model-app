# Tela08 — assets utilizáveis

Referência200×317 e original1179×753 abertos, incluindo zoom4× para conferir lupa, chevron e status. Crop global `[220,434,420,751]` (direita/inferior exclusivas) confirmado RGB idêntico, `ImageChops.difference().getbbox() == None`. SHA256 e dimensões integrais em `assets/manifest.json`. Zoom temporário foi apenas diagnóstico, não asset da interface.

Sem fotografia na fonte: nenhum recorte fotográfico, pessoa gerada, preenchimento ou imagem de UI foi produzido. Fotografia/identidade/enquadramento N/A; o auditor deve normalizar os65% restantes conforme DESIGN_SPEC, sem nota gratuita por ausência de foto.

## Seis SVGs locais

| Arquivo em assets/ | Uso/adequação | Proveniência |
|---|---|---|
| back.svg | Chevron fino para esquerda; header centro≈[17,27] | Cópia byte idêntica06/back.svg |
| location.svg | **Lupa**, círculo e haste; campo início≈[23,65]. Nome do arquivo denota o campo, não um pin | Cópia byte idêntica07/search.svg |
| chevron.svg | Pequeno V para seletor50km; centro≈[177,65] | Vetor local novo |
| cellular.svg | Barras crescentes pretas na faixa de status | Cópia byte idêntica06/cellular.svg |
| wifi.svg | Wi-Fi preto | Cópia byte idêntica06/wifi.svg |
| battery.svg | Bateria preenchida preta | Cópia byte idêntica06/battery.svg |

Todos viewBox24×24 e `currentColor`, sem Unicode ou fontes. São **aproximações vetoriais**, não extrações exatas: JPEG200px não resolve a espessura e todos detalhes subpixel. O zoom confirma lupa no campo; não reutilizar o pin de06. Status deve ser dimensionado com proporções próprias observadas na referência, evitando seis ícones quadrados do mesmo tamanho. Origem, hash da cópia e hash do original no manifest comprovam reutilização sem editar pacotes aprovados. SVGs possuem role/img e title; na implementação, ícones decorativos precisam aria-hidden e controles precisam nome acessível próprio. SVG externo conserva preto; inline herda currentColor.

## Cores amostradas

Amostras exatas RGB do JPEG recortado, sem ajuste, com boxes/método/contagem reproduzíveis no manifest. Valores são pontos de partida; a fonte contém pequenas variações/compressão.

| Token | Cor | Local e interpretação |
|---|---|---|
| Papel | #f9f8f4 | Moda no patch[70,35,120,42] |
| Texto principal | #1c1b19 | Moda dos pixels escuros do título[81,21,111,31] |
| Campo/chip claro | #eeede9 | Moda no interior de campo[35,57,120,61] |
| Trilho | #e0dfdb | Moda no segmento inativo[105,102,180,105] |
| Texto secundário | #9d9c9a | Moda com intensidade70–180 na região de valor[128,89,185,94]; antialias torna esta estimativa menos estável |
| Preto CTA/ativo | #0d0d0d | Moda em[25,283,65,296] |

Textos, hora9:41, labels, valores, chips, CTA, trilhos, segmentos e thumbs permanecem HTML/CSS nativos na implementação. Não usar referência como fundo; não rasterizar botões ou headings. Textos cinza podem precisar avaliação de contraste pelo implementador preservando a hierarquia visual e registrando desvios necessários.

## Reprodução e handoff

Da raiz: `python MODEL_tela_08_V1/assets/prepare_assets.py` (Python3 e Pillow). Reconfirma dimensões/RGB do crop, copia os cinco vetores aprovados sem alterá-los, escreve chevron e manifest determinísticos, amostra cores e calcula hashes. Nenhum PNG é entregue. Os avisos de depreciação de getdata em Pillow não afetam o resultado.

Assets08 concluído; **implementador08 liberado**. Não há insumo ausente bloqueando a tela. Sem HTML/CSS/JS, capturas de aplicativo, nota ou publicação nesta etapa;03–07 preservadas e09–11 aguardam gate08.
