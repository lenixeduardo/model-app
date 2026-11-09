# Assets05 — Portfólio

Entregue em 2026-11-09. Cinco caixas fotográficas completas e duas parciais inferiores, extraídas do JPEG oficial. Fonte `../MODEL_assets_v1/originais/mockup-geral.jpg` (1179×753); referência `../MODEL_assets_v1/referencias/05-portfolio.png` (172×404). Ambas abertas visualmente. O painel global `[836,0,1008,404]` é RGB idêntico à referência. Hashes SHA-256 integrais das duas fontes, sete PNGs, três SVGs e script constam de `assets/manifest.json`.

## Coordenadas refinadas

Todos os intervalos são half-open `[esquerda,topo,direita,base]`. Somar836 às coordenadas x locais para obter as globais, registradas também no manifesto. Geometria refinada por inspeção ampliada e amostragem das transições JPEG; não há precisão subpixel recuperável.

| Arquivo em assets/ | Box local | Dimensões | Proporção | Estado |
|---|---|---|---|---|
| foto-01-camisa-aberta.png | [3,77,109,256] |106×179|106:179|Caixa completa |
| foto-02-torso-interior.png | [111,77,169,163] |58×86|29:43|Caixa completa |
| foto-03-perfil-praia.png | [111,165,169,246] |58×81|58:81|Caixa completa |
| foto-04-monocromatica.png | [3,258,109,359] |106×101|106:101|Caixa completa |
| foto-05-camiseta-branca.png | [111,247,169,327] |58×80|29:40|Caixa completa |
| foto-06-rosto-parcial-inferior.png | [3,360,109,404] |106×44|53:22|Parcial inferior |
| foto-07-sentado-parcial-inferior.png | [111,329,169,404] |58×75|58:75|Parcial inferior |

A coluna direita começa em111, e não112 como estimado no planejamento. O limite inferior01 é256; foto03 começa165 e termina246; foto04 termina359; foto05 começa247 e termina327. Esses ajustes preservam as faixas fotográficas observáveis sem incluir as linhas centrais dos separadores. JPEG mistura pixels nas bordas: resíduos de compressão não são reparados.

## Contrato dos PNGs

Cada PNG é RGBA lossless na resolução nativa. Todos os pixels RGB, inclusive os transparentes, são cópias exatas do crop decodificado do JPEG. A única alteração é alpha binário para excluir cantos externos do tile: rounded rectangle raio3px. Nos parciais, o retângulo se estende10px abaixo do crop para não inventar cantos inferiores. Interseção com máscara do painel raio10 remove as áreas externas nos cantos inferiores06/07; os cantos da própria prancha não viram fotografia. Essa máscara geométrica é uma aproximação documentada da borda de baixa resolução; não cria pixels ou anatomia. Não há UI ou texto sobre as fotografias, nem lacunas internas que precisem de preenchimento.

“Completa” significa somente caixa inteira visível na referência. Não implica original integral, corpo inteiro ou alta resolução. Foto06/07 terminam emy404 porque o painel termina: o restante não existe nos insumos. Não completar, esticar, restaurar ou repetir pixels. O recorte07 inclui somente a porção disponível da pose sentada. Quantidade total do álbum desconhecida.

Implementação: usar as coordenadas refinadas para posicionar os tiles. Preservar proporção da fotografia; sem scaleX/scaleY independente. Alpha já elimina os cantos, evitando preencher pixels inexistentes. O clip externo do viewport deve preservar o corte inferior dos parciais. Um dialog só pode mostrar o mesmo crop disponível. Nenhuma fotografia alternativa de03/04 foi reutilizada.

## Ícones e texto

`icons/voltar.svg` é cópia byte a byte do vetor04 (origem03); `icons/busca.svg` e `icons/status-sinais.svg` são aproximações vetoriais manuais da referência05 com currentColor. Sinais contém somente celular/Wi-Fi/bateria, sem hora. Não são vetores originais recuperados. Hora9:41, Portfólio e abas Fotos/Vídeos/Trabalhos ficam em HTML nativo; não existem bitmaps com esses textos ou interface completa.

## Reprodução e validação

Executar da raiz do projeto: `python MODEL_tela_05_V1/assets/extract_assets.py` (Python3 e Pillow). O script localiza a raiz pelo próprio caminho, confirma igualdade RGB painel/referência, extrai sete crops sem resampling, aplica apenas alpha, confere igualdade integral dos canais RGB e grava manifesto com dimensões/proporções/coordenadas/hashes. Verificação executada com sucesso nesta entrega. PNGs não são screenshots do aplicativo.

Insumos ausentes: originais fotográficos de alta resolução, extensão abaixo do painel das fotos06/07, vetores originais e fonte exata. Esses limites permanecem explícitos para implementação/auditoria; nenhuma geração foi usada. Próximo papel: implementador05; não há código de interface, capturas, nota ou publicação nesta entrega.
