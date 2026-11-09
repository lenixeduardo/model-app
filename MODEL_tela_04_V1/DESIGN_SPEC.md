# Tela04 — Perfil do modelo, V1

Data:2026-11-09. Etapa: planejamento após aceite da Tela03 (`2.0.0-prototipo.7`, auditoria independente9,13/10; soma9,125). A aprovação03 não se transfere à04. Gate04: nota **>9,0**, meta9,5, com capturas reais e rubrica própria.

## Referências e sistema de medidas

Foram abertas `../MODEL_assets_v1/referencias/04-perfil-modelo.png` (192×404) e `../MODEL_assets_v1/originais/mockup-geral.jpg` (1179×753). O painel04 é o cropglobal `[634,0,826,404]`. Coordenadas abaixo são locais ao painel, `(x1,y1,x2,y2)`, aproximadas e devem ser refinadas pelo agente de assets. Não são camada de aplicativo pronta.

A tela tem foto principal monocromática de Enzo no topo, faixa de miniaturas, conteúdo editorial claro e ações inferiores. **Não reutilizar a pose colorida da03 como foto principal.** O mockup04 já define a foto/identidade e os recortes; não gerar outra pessoa, pose ou corpo.

Usar `sx=largura/192` para distâncias horizontais/fontes e `sy=altura/404` para âncoras verticais. Fotos mantêm proporção natural (`cover`/`object-position` calibrados); caixas podem acompanhar o layout, mas pixels da pessoa não são esticados em dois eixos. A razão dos viewports exigidos difere somente≈2,8% da razão192/404; a adaptação não exige reconstruir corpo.

| Área | Box fonte aproximado | Conteúdo e hierarquia |
|---|---|---|
| Foto principal | `(0,0,192,156)` | Retrato monocromático, cabeça/rosto/ombro da referência04. |
| Status | hora`(14,4,34,14)`; ícones`(148,4,181,14)` | 9:41, sinal/Wi-Fi/bateria brancos. Simulados no navegador e ocultáveis em integração nativa. |
| Voltar | centro≈`(18,32)` | Chevron branco, área de toque>=44px. Link real à Tela03 aprovada. |
| Controle superior direito | centro≈`(175,31)` | Desenho muito pequeno na fonte; tratar como opções com SVG local aproximado, sem inventar menu no estado padrão. Registrar a incerteza do ícone. |
| Contador | `(160,132,182,150)` | Pill escura com **1/8**, tipografia branca pequena. Oito é o texto do mockup, não oito fotos novas disponíveis. |
| Miniaturas | faixa`(5,156,192,206)` | Três miniaturas completas e quarta parcial; separações claras finas, cantos≈3px fonte. Não fabricar a metade oculta da quarta nem as demais fotos do contador. |
| Nome e selo | texto≈`(12,215,69,229)`; selo≈`(72,216,82,227)` | **Enzo, 26**, sans-serif preta semibold/bold; selo azul. Fonte inicial Arial nativa, sem bitmap de legenda. |
| Localização | `(12,234,83,242)` | **São Paulo, SP**, cinza, menor que nome. Não incluir a altura nesta linha: ela aparece nos dados abaixo. |
| Categorias | faixa`(12,248,180,264)` | **Fashion**, **Editorial**, **Comercial**, **Fitness**. Quatro pills claras neutras; não repetir somente as três categorias da03. |
| Dados físicos | faixa`(12,279,180,304)` | Três colunas de mesma largura: **1,84 m / Altura**, **78 kg / Peso**, **42 / Manequim**. Valor preto bold, legenda cinza menor, alinhamento central. |
| Separação | y≈309 | Linha muito sutil/espaço de separação; confirmar na referência antes de adicionar borda visível. |
| Título da bio | `(12,319,75,327)` | **Sobre mim**, preto bold. |
| Bio | `(12,334,180,363)` | Texto corrido cinza em aproximadamente três linhas na fonte, sem card decorativo. |
| Ações | faixa`(10,373,183,397)` | Compartilhar, salvar, pill preta **Solicitar contato**, botão circular com avião de papel. Não é tab bar de navegação. |

## Conteúdo textual

Texto lido no painel, preservando palavras e acentos; quebras de linha responsivas, não imagem de texto:

> Modelo profissional com experiência em campanhas de moda, editoriais e publicidade. Disponível para trabalhos nacionais e internacionais.

A fonte pequena limita a comprovação da família/peso exatos; Arial/Helvetica/sans-serif é aproximação técnica, não identificação da fonte original. Não adicionar sobrenome, disponibilidade, telefone, cachê, agência ou novos dados. Rótulos acessíveis podem descrever a função de um ícone, sem adicionar informação ao perfil.

## Tipografia, cor e acabamento

- Fundo claro amostrado≈`#f8f7f3`; texto principal≈`#111`; secundário≈`#777`; pills≈`#eeede9`. Variações mínimas da compressão do mockup não devem virar manchas artificiais.
- Nome≈13–14px fonte (≈26–28px em390), localização≈7px (≈14px), chips≈6,5–7px (≈13–14px), números≈8px bold (≈16px), labels≈6,5px (≈13px), bio≈7px com entrelinha≈9,5px (≈14/19px).
- CTA≈23px fonte de altura, raio de pill, texto branco≈7px. Em390, botão≈48px de altura. Área total aproximada `(62,373,157,397)`; círculos laterais e ícones não devem apertar o rótulo. Conferir bordas reais no asset antes de fixar larguras.
- Não usar os PNGs tipográficos da03: aqui a tipografia está sobre fundo uniforme claro, sem lacunas fotográficas. HTML/CSS nativos resolvem conteúdo e integração.
- Ícones SVG locais/embutidos; sem glifos Unicode como substitutos. Alvos>=44px, foco visível, contraste e safe areas. Não adicionar home-indicator se a inspeção não confirmar uma barra no painel04; o mockup não mostra uma barra inferior tão evidente quanto03.

## Âncoras nos três viewports

Valores arredondados; alturas/posições finais devem ser auditadas na captura, não aprovadas pela tabela.

| Âncora y | Fonte | 375×812 | 390×844 | 430×932 |
|---|---:|---:|---:|---:|
| Fim da foto / início miniaturas |156|314|326|360|
| Início conteúdo claro |206|414|430|475|
| Nome |216|434|451|498|
| Categorias |249|500|520|574|
| Valores físicos |279|561|583|644|
| Sobre mim |319|641|666|736|
| Bio |334|671|698|771|
| Topo ações |373|750|779|860|
| Base ações |397|798|829|916|

Margem lateral12px fonte corresponde aproximadamente a23/24/27px. A folha deve caber nos três viewports sem overflow indevido; em alturas menores ou texto aumentado, permitir rolagem vertical útil em vez de cortar conteúdo/ações. Não sacrificar legibilidade para forçar altura fixa.

## Assets para o próximo agente

Crops locais propostos; globais obtidos adicionando634ao x:

1. `hero-enzo-perfil.png`: região `(0,0,192,156)` →global`[634,0,826,156]`, sem UI. A fonte tem status, chevron, opções e contador incorporados. Remover somente esses elementos por alpha documentado se necessário; não inventar o fundo sob eles. As peças DOM independentes devem recobrir as respectivas lacunas sem halos. Não usar o painel integral como fundo.
2. Miniatura1: local`[5,157,56,205]` →global`[639,157,690,205]`.
3. Miniatura2: local`[59,157,111,205]` →global`[693,157,745,205]`.
4. Miniatura3: local`[114,157,166,205]` →global`[748,157,800,205]`.
5. Miniatura4 visível: local`[169,157,192,205]` →global`[803,157,826,205]`; **parcial**, não esticar horizontalmente para fingir foto completa. Confirmar/refinar bordas antes de exportar. Se houver duplicata exata noutra área já fornecida, só usar após prova visual de que é o mesmo enquadramento.
6. SVGs: voltar, opções, selo azul, compartilhar, bookmark, avião de papel. Reutilizar vetores já existentes somente quando corresponderem ao desenho04; criar variantes independentes e declarar aproximações. O símbolo de compartilhar/opções na fonte pequena precisa de inspeção ampliada, não de novos rótulos visíveis.

Entregar `ASSETS.md`, coordenadas, hashes, dimensões e máscaras/proveniência reproduzíveis. Toda porção fotográfica visível preservada deve manterRGB da fonte. Não repetir a rota de UI tipográfica raster da03 sem necessidade.
