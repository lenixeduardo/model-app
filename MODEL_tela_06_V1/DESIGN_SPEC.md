# Tela06 — Chat / Negociação, V1

Planejamento: 2026-11-09. Gate05 aprovado9,34/10; preservar integralmente03/04/05. Sem nota06 nesta etapa. Gate06>9,0, meta9,5.

## Fonte e coordenadas

Abertas visualmente `../MODEL_assets_v1/referencias/06-chat.png` (156×404) e `../MODEL_assets_v1/originais/mockup-geral.jpg` (1179×753). Painel global **[1018,0,1174,404]** confirmado RGB idêntico à referência por PIL/ImageChops, diferença bbox=None. Boxes half-open locais [x1,y1,x2,y2]; globais somam1018 ao x. Bordas abaixo aproximadas a1–2px por JPEG, refináveis pelo agente assets. Não incluir legenda externa “06. CHAT / NEGOCIAÇÃO”.

Estado inicial: fundo marfim claro, status, header de Enzo, conversa de três balões e card da campanha, compositor inferior. Sem tab bar, novos contatos, contador, novas abas ou conteúdo oculto inventado. Texto de interface permanece nativo e selecionável; nenhuma captura da tela como fundo.

## Geometria e texto

| Região | Box/âncora fonte | Conteúdo/estilo |
|---|---|---|
| Painel | [0,0,156,404] | Marfim, cantos≈10px fonte |
| Status | hora[15,4,30,12], sinais[118,4,149,12] | **9:41**, celular/Wi-Fi/bateria pretos |
| Voltar | centro[15,34] | Chevron escuro fino; destino05 aprovada |
| Avatar header | [29,22,51,44] | Foto circular original; não trocar por retrato semelhante |
| Identificação | x55, y25–42 | **Enzo, 26** em bold; **Online agora** menor/cinza |
| Telefone | centro[117,34] | Contorno de handset inclinado |
| Opções | centro[140,34] | Símbolo fino pontilhado/cruz de pequenos traços como referência; não inserir texto visível |
| Primeiro avatar | [8,69,26,88] | Foto circular original do remetente |
| Balão recebido01 | [31,62,146,96] | **Olá! Gostaria de conversar** / **sobre um projeto de campanha.** |
| Hora01 | direita≈142, y100–105 | **10:24** cinza minúsculo |
| Balão enviado | [34,111,149,146] | **Claro! Me conta mais detalhes** / **sobre o projeto.** em branco sobre quase preto |
| Hora02 | direita≈146, y151–157 | **10:25** |
| Card campanha | [16,165,150,300] | Container claro com raio≈6, borda/sombra muito sutil |
| Foto escritório | [16,165,150,209] | Interior claro com equipamentos, janelas à esquerda e fundo escuro à direita; topo arredondado |
| Título card | x25, y217–224 | **Campanha Moda Verão 2025**, bold |
| Linha localização | ícone x25, texto x38, y233–239 | **São Paulo, SP** |
| Linha duração | ícone x25, texto x38, y247–253 | **1 dia de gravação** |
| Linha cachê | ícone x25, texto x38, y261–267 | **Cachê a combinar** |
| CTA card | [24,274,144,292] | **Ver detalhes**, central bold, fundo cinza quente muito claro |
| Último avatar | [8,325,26,344] | Foto circular original; conferir se pixels repetem primeiro avatar antes de reutilizar |
| Balão recebido02 | [31,307,146,351] | **Perfeito! Tenho interesse.** / **Podemos alinhar os detalhes** / **ainda hoje.** |
| Hora03 | direita≈143, y355–361 | **10:29** |
| Compositor | y374–398 | Campo pill claro [8,374,125,397], enviar circular preto [129,375,150,396] |
| Clipe | centro[17,385] | Clipe fino cinza |
| Placeholder | x30, y382–389 | **Digite uma mensagem...** |
| Enviar | centro[140,385] | Avião de papel branco de contorno |

Quebras acima reproduzem referência; permitir reflow mínimo sem alterar redação. Não acrescentar pontuação às horas, nome de agência, moeda, orçamento numérico, endereço, data de produção ou telefone. “Online agora” e horas originais são conteúdo do mockup, não indicadores reais de rede. Não acrescentar ticks/checks de entrega.

## Assets e proveniência exigidos

Extrair três regiões de avatar separadamente até provar repetição RGB. Boxes iniciais: header[29,22,51,44], recebido01[8,69,26,88], recebido02[8,325,26,344]. Preservar só disco fotográfico com alpha circular, sem fundo do header/balão. Verificar bordas antialiasadas e informar pixels de matte sem reconstruir pele ou cabelo. A foto do header pode ter enquadramento diferente das pequenas; não substituir pessoas nem usar retratos de outras telas por aproximação.

Escritório: box inicial[16,165,150,209], global[1034,165,1168,209]. Extrair somente pixels fotográficos, excluir título/ícones/CTA e refinar limite inferior da foto. Manter cantos via CSS/alpha geométrico, não reconstruir canto inexistente. Não completar cenário, remover equipamento, gerar foto ou usar imagem de banco. Não há fotografia original maior comprovada. Documentar dimensões baixas e limites; upscaling não recupera detalhe. `ASSETS.md`, manifest e script devem registrar boxes finais, hash, identidade e prova RGB nos pixels opacos; alpha geométrico é a única alteração permitida.

SVGs locais para voltar, handset, opções, localização, calendário/duração, cachê, clipe, enviar, celular, Wi-Fi e bateria. Refinar os três pictogramas do card pela referência, sem emojis ou fontes de ícones. Desenhos vetoriais são aproximações documentadas. Nenhum rótulo/card/balão rasterizado.

## Cores, tipografia e adaptação

Arial, Helvetica, sans-serif nativas. Aproximações fonte: status6px, nome7px bold, online5,5px, mensagens7px com line-height10–11px, horas5px, título7px bold, metadados6,5px, CTA6,5px bold, placeholder6,5px. Em390, larguras usam sx=2,5: texto de mensagens≈17px, título≈17px, nome≈17px; ajustar visualmente para manter linhas/altura. Evitar multiplicar fonte cegamente por sy se prejudicar leitura.

Amostras RGB reais: fundo(75,50)=#f8f7f3; fundo(5,150)=#f9f8f4; balão recebido(30,80)=#f1f0eb; enviado(75,128)=#101010; CTA(75,280)=#e7e6e2. Texto principal≈#171715, secundário≈#82817b. A variação JPEG não justifica gradiente decorativo. Separador header e sombra card extremamente suaves; sem sombras fortes novas.

Base156×404 tem razão0,386, menor que viewports≈0,462. Âncoras horizontais W/156 e verticais H/404 definem UI fluida; nunca aplicar scaleX/scaleY à fotografia. Avatar circular com object-fit:cover e ratio1. Foto escritório mantém proporção intrínseca≈3,05:1; usar largura fluida e altura proporcional, ajustar respiro interno do card em vez de esticar foto. Registrar eventual pequeno corte adicional. Compositor preso à base com safe-area; corpo conversa flexível/rolável, header estável. Não comprimir ou ocultar texto em375.

| Âncora y | Fonte | 375×812 | 390×844 | 430×932 |
|---|---:|---:|---:|---:|
| Centro header |34|68|71|78|
| Primeiro balão topo |62|125|130|143|
| Balão enviado topo |111|223|232|256|
| Card topo |165|332|345|381|
| Card base aprox |300|603|627|692|
| Último balão topo |307|617|641|708|
| Compositor topo |374|752|781|863|

Tabela de card/base é alvo geométrico, não licença para distorcer a foto. Tipografia/caixas precisam acomodar a proporção nova; documentar ajuste da altura do conteúdo após foto proporcional. Não esticar imagem para acertar ambas as âncoras.

## Comportamento local e acessibilidade

- Voltar: link real `../MODEL_tela_05_V1/index.html`, sem alterar05.
- Telefone e opções: dialogs locais, sem iniciar chamada ou inventar contato. Explicar na abertura que é protótipo local. Sem menus novos no estado inicial.
- Ver detalhes: dialog com apenas título/local/duração/cachê visíveis no card. Não inventar briefing, datas ou anunciante. Foto do escritório abre dialog com o mesmo crop, sem conteúdo novo.
- Clipe: dialog local informando que anexos não são enviados; não iniciar upload externo. Se houver seleção local, limitar preview à memória e explicar comportamento; preferir dialog simples sem seleção desnecessária.
- Input aceita digitação; envio por botão/Enter adiciona bolha própria à conversa em estado de memória. Ignorar trim vazio, renderizar via textContent; não executar HTML. Hora de nova mensagem pode ser hora local explicitada no diálogo/informação do protótipo; não alterar10:24/10:25/10:29. Não gerar resposta automática, recibo ou fingir entrega. Recarregar restaura somente conteúdo original. Sem backend, fetch externo, persistência ou dados pessoais inventados.
- Novas mensagens tornam corpo rolável e permanecem acima do compositor, sem sobrepor card. Input deve manter foco após envio. Não inserir aviso visível no estado inicial que não conste da fonte; informação de protótipo pode constar nos dialogs e nome acessível de envio.
- Todos controles têm alvos>=44×44 CSSpx sem sobreposição, mesmo quando desenho pequeno; distribuir header para caber título. Foco visível, labels acessíveis e ordem lógica. Dialog com nome, botão fechar, Escape, foco contido/restaurado. Reduced-motion; fallback local para erro de foto/SVG sem glifo quebrado. Status é simulado. Sem publicação nesta etapa.

## Critérios para auditoria futura

Três capturas reais DPR1:375×812,390×844,430×932 da mesma versão; referência e screenshot390 lado a lado normalizados à mesma altura mantendo suas larguras proporcionais, nunca ambos156px por deformação. Abrir e inspecionar imagens, registrar navegador, dimensões, hashes, console/rede/overflow, alvos/foco/modais/envio/retorno05. Fotos/identidade/enquadramento35%, geometria25%, textos/ícones20%, cores10%, responsividade10%. Gate>9,0 e ausência de bloqueador material; meta9,5. Nota05 não se transfere. Tela07 aguarda decisão independente06.
