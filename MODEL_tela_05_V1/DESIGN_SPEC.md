# Tela05 — Portfólio (bento), V1

Planejamento: 2026-11-09. Tela04 aprovada visualmente9,30/10; preservar integralmente código/assets/capturas03/04. Esta etapa não atribui nota à05. Gate próprio: >9,0/10, meta9,5.

## Fonte e sistema de medidas

Referência aberta visualmente: `../MODEL_assets_v1/referencias/05-portfolio.png`,172×404. Original aberto: `../MODEL_assets_v1/originais/mockup-geral.jpg`,1179×753. Painel global **[836,0,1008,404]**, confirmado por comparação PIL pixel a pixel: crop RGB idêntico à referência. Coordenadas half-open [x1,y1,x2,y2], locais ao painel salvo indicação global. Medidas geométricas abaixo são aproximações de borda JPEG; assets deve refiná-las sem acrescentar pixels.

Tela escura com status, header compacto, três abas e mosaico assimétrico de fotografias de Enzo. Não contém nome sobre as fotos, contador, legenda, CTA, tab bar inferior ou home indicator visível. Não acrescentar esses elementos ao estado inicial. O rodapé de identificação “05. PORTFÓLIO (BENTO)” pertence à prancha geral e fica fora do painel.

## Estrutura e conteúdo exato

| Elemento | Geometria fonte aproximada | Conteúdo |
|---|---|---|
| Painel | [0,0,172,404] | Preto levemente quente, cantos externos≈10px; viewport recorta a última fileira |
| Status | hora[12,4,29,12], sinais[130,4,161,12] | **9:41**, sinal celular, Wi-Fi, bateria claros |
| Header | y18–41; título central≈[67,25,105,33] | **Portfólio**, semibold branco |
| Voltar | centro[14,29] | Chevron fino claro; link à04 aprovada |
| Busca | centro[156,29] | Lupa fina clara; sem input aberto no estado inicial |
| Abas | y46–65 | **Fotos**, **Vídeos**, **Trabalhos**, nessa ordem |
| Fotos | [10,46,57,65] | Pill branca, texto escuro bold, aba ativa |
| Vídeos | [60,46,105,65] | Pill quase preta, texto claro menor |
| Trabalhos | [108,46,162,65] | Pill quase preta, texto claro menor |
| Mosaico | x3–169, y77–404 | Duas colunas independentes, esquerda≈106px e direita≈57px, gap≈3px |

O espaço entre abas e mosaico é≈12px fonte. A coluna esquerda tem retrato claro grande, retrato monocromático e retrato parcial inferior; a direita tem quatro fotos. **Há sete regiões fotográficas visíveis**, cinco completas em suas caixas e duas cortadas pela borda inferior do painel. São sete recortes disponíveis, não prova de total do portfólio. Nenhum contador total deve ser inventado.

## Contrato dos sete recortes

Extrair somente fotografia, sem fundo do painel. Não usar referência integral como bitmap de interface. Os limites abaixo incluem as caixas visíveis; preservar raio por CSS, podendo refinar 1px para excluir separadores JPEG. Cada arquivo mantém proporção/RGB da região extraída. Coordenadas globais somam836 ao x.

| ID | Identificação visual | Box local proposto | Box global | Condição |
|---|---|---|---|---|
| foto01 | Enzo, camisa branca aberta, rosto frontal/inclinado | [3,77,109,255] | [839,77,945,255] | Caixa completa;106×178 |
| foto02 | Enzo, torso nu frontal, fundo interior quente | [112,77,169,163] | [948,77,1005,163] | Caixa completa;57×86 |
| foto03 | Enzo de perfil, torso nu, mar/areia ao fundo | [112,166,169,245] | [948,166,1005,245] | Caixa completa;57×79 |
| foto04 | Enzo monocromático, roupa escura, braço à frente | [3,258,109,357] | [839,258,945,357] | Caixa completa;106×99 |
| foto05 | Enzo, camiseta branca e colar | [112,248,169,326] | [948,248,1005,326] | Caixa completa;57×78 |
| foto06 | Enzo, rosto/cabelos castanhos e olhar lateral | [3,360,109,404] | [839,360,945,404] | **Parcial inferior**,106×44; a imagem continua além do painel e não está disponível |
| foto07 | Enzo sentado, roupa preta sem mangas, céu/água | [112,329,169,404] | [948,329,1005,404] | **Parcial inferior**,57×75; não completar corpo/pernas/base |

“Completa” significa caixa do tile inteira visível, não fotografia original integral ou corpo inteiro. Foto06/07 devem terminar no limite visível, sem inventar extensão, repetir faixas ou ampliar para fingir conteúdo oculto. Não reutilizar pose semelhante de outra tela sem identidade exata demonstrável. A referência é de baixa resolução; upscaling não recupera detalhe. Não gerar imagens, pessoas, poses, anatomia ou fundo. Registrar se a borda arredondada inferior do próprio painel já corta pixels dos dois últimos crops; reproduzir via clip e não preenchimento sintético.

## Layout responsivo e acabamento

Base172×404; âncoras horizontais usam sx=W/172, verticais sy=H/404. Manter as relações bento e o recorte inferior nos três viewports. Não aplicar transform scaleX/scaleY à fotografia: cada crop como img com proporção natural e object-fit:cover calibrado em caixa responsiva. A razão do painel≈0,426 difere das capturas≈0,462; há ajuste de enquadramento necessário. Priorizar rosto e composição visível; documentar qualquer corte adicional. Para os parciais, apresentar só pixels existentes e manter o limite de recorte; nunca revelar área supostamente oculta.

| Âncora y | Fonte | 375×812 | 390×844 | 430×932 |
|---|---:|---:|---:|---:|
| Centro header |29|58|61|67|
| Topo abas |46|92|96|106|
| Topo mosaico |77|155|161|178|
| Início foto03 |166|334|347|383|
| Início foto05 |248|498|518|572|
| Início foto04 |258|519|539|595|
| Início foto07 |329|661|687|759|
| Início foto06 |360|724|752|830|

Cantos dos tiles≈3px fonte. Fundo estimado #11110f/#151512; abas inativas #1b1b19; texto #f5f5f1; aba ativa #fafaf8 e texto #171715. Cores são aproximações de JPEG, refináveis por amostragem no estágio assets/implementação. Sem sombras decorativas novas.

Fontes nativas Arial/Helvetica/sans-serif. Status≈6,5px fonte; título≈8,5px semibold; abas≈6,5px, Fotos bold. Em390: título≈19px, abas≈15px, status≈14px. Confirmar pela comparação, sem rasterizar textos sobre fundo uniforme. SVGs locais finos para voltar, lupa e status; documentar aproximação vetorial. Alvos de interação>=44×44 CSSpx, mesmo se desenho menor; hit areas de voltar/busca não sobrepõem título, abas têm largura suficiente. Foco visível e nomes acessíveis não devem virar novos rótulos no estado inicial. Status simulado não é status real do aparelho.

## Interações locais exigidas

- Voltar é link real `../MODEL_tela_04_V1/index.html`; não modificar a04 para acomodar a05.
- Abas com estado selecionado acessível. Fotos inicia ativa e mostra sete crops; Vídeos/Trabalhos respondem com estado vazio honesto após clique, sem vídeos ou trabalhos fictícios. Troca de volta restaura mosaico.
- Clicar foto abre dialog local com **o mesmo crop disponível**, sem tentar completar as fotos parciais. Fechar por botão e Escape; foco preso/restaurado. Sem contador total; se navegar entre crops, descrevê-los como recortes locais, sem alegar álbum integral.
- Lupa abre dialog local de busca, com input/fechar e comportamento frontend documentado. Pode filtrar somente os recortes disponíveis com metadados descritivos locais; não alegar busca em servidor. Resultado vazio explícito após busca sem correspondência. Não inserir placeholder/input visível antes da abertura.
- Sem backend, banco, autenticação, upload, chamadas externas, arquivos de vídeos/trabalhos inventados ou publicação nesta etapa.
