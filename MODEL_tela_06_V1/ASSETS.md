# Assets06 — Chat / Negociação

Entrega de assets concluída em2026-11-09. Consome DESIGN_SPEC.md/PLANO.md, Task1. Próximo papel: implementador06. Não atribui nota visual nem libera07.

## Fonte e prova

Referência `../MODEL_assets_v1/referencias/06-chat.png`,156×404, e JPEG original `../MODEL_assets_v1/originais/mockup-geral.jpg`,1179×753, abertos visualmente. O painel global half-open `[1018,0,1174,404]` é RGB idêntico à referência: `ImageChops.difference(...).getbbox() == None`. Fonte SHA256 `9120f379280879ca9c7695eeccba7288630b6956b39708eb94311080dbedf3dd`. Hash da referência e hashes individuais completos constam de `assets/manifest.json`.

Reproduzir a partir da raiz model-app: `python MODEL_tela_06_V1/assets/extract_assets.py` (Python3/Pillow). O script reconstrói os quatro PNGs e onze SVGs, confirma identidade do painel, testa todos pixels com alpha>0 contra RGB da fonte e exige RGB=(0,0,0) nos pixels totalmente transparentes. Nenhum RGB visível é pintado, corrigido, interpolado ou gerado. Apenas alpha geométrico em resolução16× seguido de redução Lanczos; ringing externo dos discos é eliminado. PNGs foram abertos individualmente depois da extração e não contêm legenda, balão, texto ou CTA.

| Asset | Dimensão | Box local | Box global | Uso |
|---|---|---|---|---|
| `avatar-header.png` |22×22|[29,22,51,44]|[1047,22,1069,44]|Retrato original do cabeçalho|
| `avatar-received-first.png` |18×19|[8,69,26,88]|[1026,69,1044,88]|Primeiro retrato do remetente|
| `avatar-received-last.png` |18×19|[8,325,26,344]|[1026,325,1044,344]|Último retrato do remetente|
| `campaign-office.png` |134×44|[16,165,150,209]|[1034,165,1168,209]|Foto de escritório/estúdio do card|

As três instâncias mostram visualmente o mesmo retrato da referência06, sem recorrer a fotografias das outras telas. Não existe igualdade RGB entre os dois crops pequenos: diferença bbox[0,0,18,19], causada por contexto/compressão e possível reenquadramento subpixel. Por isso **usar arquivos separados**, sem substituir a última instância pela primeira. Header é maior e não há prova de transformação exata para os pequenos. Não foi comprovada uma foto independente maior deste retrato ou escritório.

Discos: header centro(11,11), raio10,2; recebidos centro(9,9,5), raio8,05 em coordenadas locais. Máscaras conservadoras retiram o matte claro exterior. Restos de mistura JPEG/antialias junto à borda pertencem à própria fonte e não foram descontaminados, pois isso alteraria RGB. Pode haver perda inferior a1px da borda escura por prudência; rosto/cabelo não foram reconstruídos. Os canvases18×19 preservam a caixa original: usar dimensões proporcionais ou `object-fit:contain` num suporte quadrado, nunca esticar para18×18. O disco fotografado já é circular.

Escritório: pixels reais das janelas à esquerda, tripés/equipamentos e painel escuro à direita. Alpha arredonda apenas cantos superiores em raio6px fonte. Foto termina emy208 inclusive; y209 não foi incluído. A região não contém título/metadados/CTA. Manter razão134/44≈3,04545, com altura automática. Não recortar para uma altura arbitrária nem preencher região externa/canto transparente com fotografia fabricada. Nenhuma UI cobre a região fotográfica extraída; o recorte não necessita inpainting.

## Vetores locais

Todos SVGs usam viewBox0 0 24 24, `currentColor`, `<title>` em português e `role=img`. Quando usados decorativamente ao lado de label nativo, aplicar `aria-hidden=true` ao elemento de imagem; o botão externo deve ter nome acessível próprio. São **aproximações vetoriais**, não pixels exatos dos pictogramas.

- `back.svg`: chevron fino; `phone.svg`: handset inclinado.
- `options.svg`: cinco pontos em cruz/retículo, conforme a leitura ampliada; não é menu de três pontos.
- `location.svg`: marcador com centro circular; `calendar.svg`: contorno de calendário com traço/check interno aproximado.
- `money.svg`: medalhão circular com forma central semelhante a casa/moeda; a baixa resolução não permite distinguir com certeza símbolo monetário. Evita inventar cifra textual.
- `paperclip.svg`: clipe vertical; `send.svg`: avião de papel em contorno, pintar branco no botão preto.
- `cellular.svg`, `wifi.svg`, `battery.svg`: status simulado vetorial. Hora9:41 permanece texto nativo.

Incertezas observadas no zoom4×: opções pode ter pequenos traços em vez de discos; duração parece uma caixa/calendário com check; cachê é um círculo com miolo angular, sem cifra legível. Essas reconstruções priorizam posição e peso de traço, sem alegar identificação exata. Títulos/labels/horas/mensagens devem ser texto nativo Arial; nenhum asset de caption foi produzido.

## Handoff e limites

Quatro PNGs utilizáveis e onze SVGs locais entregues com provas em manifest. Sem bloqueio de asset para implementar o estado visível06; baixa resolução permanece um limite material de nitidez, ampliação não recupera detalhe. Sem conteúdo oculto, pessoas trocadas, geração de imagem ou fonte externa. Pacotes03/04/05 preservados. Não foram produzidos HTML/CSS/JS, capturas de navegador, auditoria, nota ou publicação.

Ruling da execução: o escopo autorizado deste papel é somente Task1; Tasks2–4 permanecem com os próximos papéis. A prova de repetição não sustenta deduplicação, portanto as três instâncias são entregues independentes.
