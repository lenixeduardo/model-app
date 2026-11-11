# Tela11 — Notificações — contrato visual V1

Planejamento autorizado pelo gate10 independente **9,28/10** (soma9,2825), em `../MODEL_tela_10_V1/AUDITORIA.md`. Original e referência abertos visualmente neste papel. Preservar integralmente03–10 e suas evidências. Entrega somente documental; sem assets, interface, capturas, nota ou publicação.

## Fonte, frame e limites

Original `MODEL_assets_v1/originais/mockup-geral.jpg`,1179×753. Referência `MODEL_assets_v1/referencias/11-notificacoes.png`,184×317. Crop global confirmado **[805,434,989,751]**, coordenadas direita/base exclusivas: comparação RGB Pillow/ImageChops bbox=None. A tela começa pela status bar e termina pela navbar; não cortar a base nem inserir moldura de aparelho. Razão fonte184/317≈0,58044; alvos móveis são mais estreitos proporcionalmente. Não esticar imagem ou fotografia para preencher essa diferença.

Há **seis linhas de notificação**, **cinco avatares fotográficos circulares** e **um círculo coral com pictograma**, quatro filtros e cinco destinos na navbar. Não há marcador colorido de não lida, contador, menu de três pontos, ilustração de empty state ou botão voltar no repouso. Linhas/separadores são discretíssimos; não inventar cartões, sombras ou bordas fortes.

## Geometria de referência

Medidas aproximadas em pixels da referência local184×317, a refinar pelo agente de assets sem alterar composição. Origem superior esquerda. Tolerância de leitura visual≈1–2px devido ao JPEG.

| Elemento | Box/âncora local aproximada |
|---|---|
| Status | hora9:41 em[13,7]; sinais/bateria em[139,7] até174 |
| Título | “Notificações”, x11,y26, altura12 |
| Adicionar | círculo preto centro[166,31], diâmetro17; mais branco |
| Filtros | y49–65; Todas x11–51; Castings54–91; Mensagens94–135; Sistema138–174; gap≈3 |
| Avatares | círculos≈24×24, x13–37, centros y88/123/159/194/229/265 |
| Coluna texto | x49, largura≈99; primeira baseline y85; segunda baseline y94; demais blocos a cada≈35–36 |
| Tempos | alinhamento à direita x169, centros y88/123/159/194/229/265 |
| Navbar | faixa inferior≈y287–317; ícones centros x19/55/91/127/163,y301; perfil preto ativo |

Primeira linha tem topo≈78; última termina≈273. Distribuição de seis linhas uniforme, sem sétima linha. Cabeçalho tem margem superior de status respeitada. Navbar tem casa outline, busca outline, mais, conversa outline, pessoa preenchida preta. Filtros são pills compactas: Todas preto/texto branco; demais claros/texto cinza. Não confundir Sistema com avatar de casting.

## Conteúdo nativo e quebras

Usar texto HTML nativo, Arial/Helvetica/sans-serif como aproximação da sans da miniatura; fonte exata não fornecida. Nada de rasterizar título, textos, tempos ou chips. Estimativas na referência: título11–12px bold; notificações6–6,5px normal, line-height≈9px; tempos≈5px cinza; chips≈5,5px; status≈6px semibold. Em390, título≈24px, mensagens≈13–14px, chips≈11–12px e tempos≈10–11px. Refinar visualmente sem reduzir legibilidade indevidamente.

Cada notificação tem **duas linhas** no estado inicial; quebras abaixo preservam composição. Não adicionar idade, agência nominal, prazo, cachê ou título de trabalho.

| Ordem | Linha1 | Linha2 | Tempo | Avatar/ícone |
|---|---|---|---|---|
| 1 | Nova mensagem | de Enzo | Agora | retrato masculino frontal, camiseta clara/cinza |
| 2 | Campanha Inverno 2025 | lhe enviou uma proposta. | 1h | homem de roupa escura, camisa clara |
| 3 | Seu perfil foi salvo | por uma agência. | 3h | retrato masculino escuro/frontal |
| 4 | Nova oportunidade | de casting. | 1d | círculo coral com pequeno pictograma claro |
| 5 | Matheus curtiu | seu perfil. | 2d | homem de roupa escura/camisa clara |
| 6 | Seu portfólio foi visualizado | 25 vezes esta semana. | 3d | retrato masculino frontal/camiseta clara |

Título e filtros: **Notificações**, **Todas**, **Castings**, **Mensagens**, **Sistema**. Hora **9:41**. Na linha6 a primeira linha é mais comprida; reservar largura suficiente antes do tempo, sem reticências. As identidades nominais dos avatares2/3/5/6 não são comprovadas pela foto: não assumir que foto semelhante pertence ao mesmo indivíduo, não importar Matheus10/Enzo03 para substituir pixels11. O texto chama Matheus na5, mas isso não autoriza reconstruir rosto. Pictograma coral parece oportunidade/casting, com traço fino; desenho exato é ambíguo no raster24px. Documentar SVG como aproximação, sem acrescentar logomarca ou letra inventada.

## Cor e assets

Papel quente≈#F9F8F4 (amostra margem dominante249,248,244), pequenas variações JPEG; área interna≈#F8F7F2. Preto≈#0C0C0C em filtro ativo e adicionar; texto principal≈#222; tempos/cinza≈#8C8C88 a conferir por amostra; pills inativos≈#EFEFEA. Coral do círculo deve ser amostrado diretamente pelo agente de assets; não converter em vermelho saturado. Fundo simples CSS sem textura JPEG de tela inteira. Não há gradiente decorativo.

Extrair cinco crops genuínos **desta tela11**, em proporção1:1; preservar cabelo, rosto, ombros e círculo completos. RGB deve coincidir com a fonte em pixels visíveis; apenas alpha geométrico exterior, sem suavizar/inventar rosto, inpaint, upscale generativo ou recuperar detalhe inexistente. Foto baixa resolução≈24px é limite explícito, não motivo para trocar pessoa. Assets deverá refinar boxes/centros e registrar fonte global/local, dimensões, hashes, máscaras/matte e todos os pixels indisponíveis. Círculo coral pode ser crop de pictograma ou vetor aproximado documentado; não conta como fotografia. Texto e controles ficam separados da foto. Referência integral não pode virar fundo da implementação. SVGs locais para status/mais/nav/casting; reutilização aprovada somente com origem/hash, pois ícones podem diferir.

## Ações locais honestas

Estado inicial idêntico à fonte: Todas ativo, seis itens, nenhuma indicação de leitura acrescentada. Estado apenas em memória; reload restaura. A referência não prova quais itens estão lidos nem o mapeamento taxonômico: regra local documentada para protótipo — Mensagens item1; Castings2/4; Sistema3/5/6; Todas seis. Não alegar classificação ou eventos recebidos do servidor. Filtros mudam a lista local e aria-pressed/estado selecionado; cabeçalho/nav fixam sua posição, itens restantes alinham ao topo com mesma geometria. Se busca alternativa causar vazio, explicar localmente; não criar conteúdo falso.

Cada item abre dialog acessível com seu próprio texto e aviso de demonstração local. Marcar como lida/não lida somente após ação explícita no dialog; estado fonte é “não informado” e não equivale a não lida. Sinal de alteração só aparece depois da ação, com legenda acessível; nenhum badge novo no repouso. Permitir desfazer em memória. Nenhum envio, curtida externa, proposta aceita, push ou atualização de contagem remota.

Item1: link explicitamente rotulado para conversa demonstrativa aprovada06 (`../MODEL_tela_06_V1/index.html`), sem alegar nova mensagem no backend. Item2: detalhe local com texto fonte; link opcional “Ver castings de demonstração” para07, pois referência07 mostra Campanha Inverno2025 mas não prova correspondência remota. Item4: mesmo destino07 explicitamente geral, sem inventar casting específico. Itens3/5/6: dialog somente informativo; link “Meu perfil” para10 sem inventar identidade da agência, lista de visualizadores ou analytics. Item6 não transforma25 em métrica viva. Mais superior: dialog de gerenciamento local, pode oferecer “Marcar todas como lidas” e restaurar estado inicial; não inventar formulário de criação/envio de notificação.

Navbar: casa→03 aprovada (`../MODEL_tela_03_V2/index.html`); busca→07; mais→dialog local sem publicação; conversa→06; perfil→10 (`../MODEL_tela_10_V1/index.html`). Perfil permanece visualmente ativo como fonte, embora esta tela seja Notificações; não trocar por sino. Não editar03–10 para inserir atalhos de11. Mesma aba, sem href vazio ou links mortos.

Alvos≥44×44 CSSpx sem interseção; filtros podem precisar aumentar altura invisível de clique mantendo separação do header/lista. Foco visível, nomes acessíveis, selected/pressed/current coerentes, ordem de tab e leitura. Dialog com título/fechar/Escape/contenção e restauração de foco, rolagem interna. Texto seguro via textContent, reduced-motion, fallback de foto mantém círculo e nome/descrição sem mostrar outra pessoa. Limites de demonstração aparecem ao agir, sem banner adicional no repouso.

## Adaptação e gate

Horizontais porW/184; âncoras verticais porH/317; fotografia mantém1:1 e tamanho por largura. Em390×844, título≈[23,69], adicionar centro≈[352,83]; filtros≈y130–173; centros das seis linhas≈234/327/423/517/610/706; avatar≈51×51; texto x104; tempos borda359; nav centro≈801. A diferença de razões cria mais respiro vertical: não alongar fotos nem inflar fonte por altura.375×812 e430×932 devem mostrar seis linhas/navbar integrais, sem overflow, colisões ou nav sobre último item. Refinar os respiros em comparação visual, preservando hierarquia.

Capturas reais **375×812/390×844/430×932,DPR1**, navegador/versão/comandos/hashes ligados à versão final. Abrir candidata390 antes das finais e abrir três finais. Comparação390 com referência normalizada à altura844, mantendo cada proporção (referência≈490×844, app390×844), sem stretch. Testar console/rede/assets/overflow/foto, filtros e contagens, readstates/desfazer/reload, dialogs/foco/Escape, links06/07/10 e nav03,44px/reduced-motion/fallback. Distinguir testes realizados de revisão.

Auditor independente: fotografia/identidade/enquadramento35%; geometria25%; tipografia/ícones/chips20%; cores/contraste/sobreposição10%; responsividade/acabamento10%. Soma **>9,0**, meta9,5, sem P1 material. Não inferir nota por código ou herdar9,28 da10. Versão alterada requer capturas e auditoria novas; nota exatamente9 não aprova. Falta de pixel genuíno bloqueia em vez de autorizar substituição. Gate11 encerra fila visual, não equivale a publicação automática neste papel.
