# Tela07 — assets originais entregues

Fonte: `../MODEL_assets_v1/originais/mockup-geral.jpg` (1179×753), aberta junto à referência07 (201×317), seu zoom e três crops individuais. Painel global `[11,434,212,751]` confirmado RGB idêntico à referência inteira. Coordenadas com direita/inferior exclusivas. SHA256 integrais e provas por foto em `assets/manifest.json`.

| PNG local em assets/ | Box local | Box global | Dimensão | Inspeção independente |
|---|---|---|---|---|
| campanha-inverno-2025.png | [12,65,74,124] | [23,499,85,558] | 62×59 | Cabelo escuro, casaco preto aberto, peito visível, fundo cinza; identidade/enquadramento originais |
| marca-esportiva.png | [12,140,74,204] | [23,574,85,638] | 62×64 | Cabelo curto, regata escura, ombro e peito originais; olhos escuros/sombreados, óculos não confirmáveis na fonte |
| editorial-masculino.png | [12,218,74,283] | [23,652,85,717] | 62×65 | Cabelo escuro volumoso, cabeça inclinada, camisa clara aberta; enquadramento original distinto |

Refinamento frente aos boxes iniciais: fotos02/03 começam um pixel acima para preservar o início visível do frame. Três arquivos independentes, sem reaproveitar outra pessoa ou fotografia. Cada quadro visível termina na borda original: nenhum corpo/cabelo/fundo foi completado. Não há título, data, valor, bookmark ou label da interface dentro dos arquivos. Nenhuma legenda PNG foi criada; todos os textos pertencem à implementação nativa.

PNG RGBA sem reamostragem, cor derivada diretamente do JPEG. Alpha binário por retângulo arredondado geométrico conservador de raio5px, removendo cantos de papel; RGB de todo pixel alpha>0 é idêntico ao crop fonte, RGB de alpha0 é zero. Pequenos resíduos de matte/antialias/compressão JPEG junto à borda estão preservados e não são recuperáveis sem alterar pixels. Baixa resolução é limite do insumo; ampliar não recupera detalhes. Não há geração, inpainting, troca de face ou nova anatomia. Fotos podem ser exibidas proporcionalmente; nunca alongar eixos independentemente.

## Vetores locais

Treze SVGs, viewBox24×24, sem fontes/glifos Unicode: `cellular`, `wifi`, `battery`, `location`, `bookmark`, `calendar`, `currency`, `top-plus`, `plus`, `nav-home`, `search`, `chat`, `profile`. Todos são aproximações vetoriais declaradas, não extrações exatas. Status, localização e bookmark copiados byte a byte de06/04, com origem e SHA256 no manifest; pastas aprovadas intactas. Calendário07 tem data sem check da duração06; moeda07 usa círculo com cifrão, evitando o pictograma de casa aproximado de06. A minúscula fonte não permite confirmar todos detalhes internos desses dois símbolos.

`top-plus` traz círculo preto e cruz branca como no header; `plus` é a cruz simples da tabbar. `nav-home` é preenchido e demais navegações são contornos. `currentColor` resulta preto nativo ao usar inline e permite cinza herdado; SVG externo `<img>` mantém preto nativo, exigindo estilo/filtro se desejado cinza. Nenhum SVG de linha foi desenhado branco sobre fundo claro. Espessura aproximada1,55 unidades; a fonte não resolve fielmente todos traços subpixel.

## Reprodução e prova

Executar da pasta do projeto: `python MODEL_tela_07_V1/assets/extract_assets.py` (Python3 + Pillow). Script reconfirma painel, extrai os três PNGs, aplica apenas alpha geométrico, verifica RGB visível e RGB oculto zero, e reescreve manifest determinístico com SHA256 de fonte/referência/PNGs/SVGs, caixas, dimensões e contagem de pixels de cada foto. SVGs são fontes vetoriais versionadas; script inventaria seus hashes e reconhece cópias idênticas de04/06.

Entrega utilizável: três fotos e13 vetores. Nenhum insumo ausente bloqueia implementação. Próximo papel implementador07; auditoria visual e gate>9,0 pendentes, meta9,5. Sem código de interface, captura de aplicativo, nota, publicação ou trabalho08.
