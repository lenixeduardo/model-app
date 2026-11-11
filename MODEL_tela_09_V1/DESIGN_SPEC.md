# Tela09 — Salvos — contrato visual V1

Planejamento de 2026-11-11. Gate08 aprovado 9,23/10, sem P1 material. Preservar03–08. Referência aberta: `MODEL_assets_v1/referencias/09-salvos.png`,176×317; original aberto: `MODEL_assets_v1/originais/mockup-geral.jpg`,1179×753. Crop global **[428,434,604,751]**, direita/inferior exclusivas, RGB idêntico confirmado por Pillow ImageChops, bbox=None. Medidas locais abaixo aproximadas pela resolução. Não iniciar10 antes do gate09 >9,0; meta9,5.

## Conteúdo e geometria

| Região | Coordenadas locais aproximadas | Conteúdo |
|---|---|---|
| Papel | [0,0,176,317], cantos≈12 | Branco quente, sem moldura adicional |
| Status | hora[16,7,30,13], sinais[138,7,165,14] | 9:41; celular, Wi-Fi, bateria pretos |
| Header | título[13,24,57,37], ação centro[159,31] | **Salvos**, bold; pequeno ícone de quatro braços/pontos, conforme fonte |
| Tabs | y47–63; Modelos[13,47,88,63], Castings centro[128,55] | **Modelos** ativo: pill preta; **Castings** cinza, sem pill escura |
| Foto01 | [12,72,86,135] | Enzo, peito nu, cabelo castanho, céu azul; pessoa e frame originais |
| Foto02 | [92,72,166,135] | Gabriel, cabelo escuro, camisa clara aberta, fundo cinza |
| Texto01 | x14,y142 e y153 | **Enzo, 26** / **São Paulo, SP** |
| Texto02 | x94,y142 e y153 | **Gabriel, 28** / **Rio de Janeiro, RJ** |
| Foto03 | [12,168,86,233] | Rafael, cabelo escuro, retrato de ombro e rosto em três quartos |
| Foto04 | [92,168,166,233] | Theo, cabelo escuro frontal, roupa escura, fundo cinza |
| Texto03 | x14,y240 e y251 | **Rafael, 29** / **São Paulo, SP** |
| Texto04 | x94,y240 e y251 | **Theo, 24** / **Belo Horizonte, MG** |
| Salvar | centros≈[77,126],[158,126],[77,224],[158,224] | Pequeno bookmark branco sobre área arredondada cinza translúcida; quatro ativos |
| Nav | divisor y285; centros x19/54/90/124/157,y299 | Casa preta preenchida; busca; mais; chat; perfil. Cinco ícones, preservar ordem e estado aparente da referência |

Margens laterais12/176≈6,82%; gutter6/176≈3,41%; colunas74/176≈42,05%. Não transformar o grid em lista ou acrescentar cards. Quatro identidades e metadados exclusivamente acima; não inferir novos nomes/dados do retrato. A foto04 é Theo conforme rótulo desta fonte, mesmo que outras telas tenham outra ordem de pessoas.

Textos nativos Arial/Helvetica/sans-serif sobre papel, sem PNG de labels. Título≈13px bold local; tabs≈7px; nomes≈8px bold; cidades≈6px; status≈6px. Em390, multiplicador horizontal2,216: título≈28,8px; nomes≈17,7px; cidades≈13,3px. Refinar por comparação, sem scaleX/scaleY de fonte. Ícones SVG locais aproximados, sem emoji/glifos substitutos.

Amostras RGB efetivamente colhidas do original por referência idêntica: papel faixa[5,35,170,44] dominante(249,248,244)=**#f9f8f4**,795 pixels; papel inferior[10,260,165,280] dominante(248,247,243)=**#f8f7f3**,836 pixels; interior tab ativa[20,50,80,58] dominante(12,12,12)=**#0c0c0c**,70 pixels. Variação JPEG não é gradiente decorativo obrigatório. Usar papel uniforme próximo #f9f8f4, preto próximo #101010, secundário cinza amostrado pelo papel de assets. Não inventar sombras.

## Contrato fotográfico e assets

Extrair quatro fotos independentes do mockup, registrando boxes refinados, global/local, dimensões, identidade, hashes e máscara. Boxes acima são guias; o agente de assets deve conferir borda/cantos exatos. Não usar referência completa como fundo, nem colar legenda/UI dentro de cada imagem. Cada fotografia deve conservar **todo o frame visível da fonte**, com largura fluida e altura intrínseca (`width:100%;height:auto` ou equivalente comprovado). Não usar object-fit:cover em caixa de ratio divergente:07 perdeu27–28% da largura e aumentou cabeça37–39%, P1 já corrigido. Cantos só nos limites originais; não recortar pessoa para preencher altura adicional.

Bookmark encobre pixels reais. Separar fotografia com alpha apenas no footprint exato do controle/UI, e SVG/botão co-registrado opaco na área que não possui fotografia genuína. Não reconstruir pele/roupa/céu sob o controle, não inpaint, não gerar corpo, não substituir pessoas. Registrar matte JPEG residual. Se o overlay original for translúcido e não permitir recuperar pixels sem inventá-los, preservar a lacuna e cobri-la por controle independente com geometria fiel; demonstrar que a lacuna nunca fica exposta, inclusive ao mudar salvo. Não confundir pixels de fotografia escura com UI na máscara. Sem inventar alta resolução a partir do recorte pequeno. Fotos podem ser ampliadas proporcionalmente com limite de nitidez explicitado.

## Comportamentos locais

- Estado inicial: tab Modelos ativa; quatro modelos salvos. Estado somente em memória; reload restaura referência. Sem backend, login, API ou persistência alegada.
- Modelos/Castings são tabs acessíveis com painel associado e seleção anunciada. Castings pode mostrar dados já existentes e identificados da07 ou vazio honesto com texto de demonstração; não criar campanhas, valores, salvos remotos ou metadados novos. Retornar Modelos preserva estado em memória. Captura inicial sempre Modelos.
- Bookmark é botão independente da foto, com nome “Remover [nome] dos salvos”, aria-pressed e alvo44px. Remoção pode retirar card e oferecer desfazer em aviso acessível; ordem restaurada é original. Alternativa permitida: manter card e indicar estado desmarcado nesta demonstração. Nesse caso a área opaca necessária para cobrir lacuna fotográfica permanece, apenas glifo/estado muda. Não remover overlay e revelar alpha vazio. Não propagar clique do bookmark à foto.
- Foto/card pode abrir preview local acessível com nome/cidade/foto genuína, sem inventar biografia. Somente Enzo pode oferecer “Ver perfil de Enzo (demonstração)” para04 aprovada. Não encaminhar Gabriel/Rafael/Theo ao perfil04 como se fosse deles; informar ausência de perfil completo local ou apenas preview. Não ampliar máscara com crop anatômico.
- Ícone superior abre opções locais honestas (por exemplo resumo de salvos ou ajuda) em dialog; não inventar sincronização/ordenação remota. Não adicionar decoração no estado inicial.
- Nav original: casa→03 aprovada (`../MODEL_tela_03_V2/index.html`); busca→07 aprovada (`../MODEL_tela_07_V1/index.html`); chat→06 aprovada (`../MODEL_tela_06_V1/index.html`). Mais abre ação local explícita de demonstração; perfil informa tela ainda indisponível em dialog, sem criar10 nem link morto. Navegação mesma aba. Não alterar03–08 para inserir links novos.
- Alvos44×44px sem sobreposição entre foto/bookmark/tabs/nav. Foco visível, teclado, labels, aria-live de saves/desfazer. Dialog com título, fechar, Escape, contenção e restauração de foco; reduced-motion e fallback de imagem/ícone sem símbolo quebrado. Se foto falhar, área textual com identidade e aviso; não usar outra pessoa. Texto via textContent.

## Responsividade e avaliação

Âncoras horizontais porW/176, verticais porH/317; o alongamento da viewport é distribuído em respiros, não em anatomia ou foto. Em390×844: margens≈26,6px, gutter≈13,3px, largura foto≈164px e altura natural≈140/144px; y fotos≈192/447, textos≈378/639 conforme âncoras, ajustar respiro sem cortar frames. Não fixar foto em altura proporcionalH se isso mudar ratio. Na375×812 e430×932, todos os quatro cards e navbar devem aparecer sem overflow lateral; safe area incluída e nav não cobre conteúdo. Fotos mantêm largura/altura intrínsecas nos três tamanhos.

Evidências reais375×812,390×844,430×932,DPR1; comparação da390 com referência normalizada à **altura844**, preservando proporção individual, sem stretch. Registrar versão/navegador/procedimento/hashes; abrir três capturas e comparação. Testar console/rede/assets/overflow, quatro bookmarks e isolamento/desfazer/reload, tabs, previews, destinos03/04/06/07, nav local, foco/Escape/teclado44px/reduced-motion/fallback.

Rubrica: fotografia/identidade/enquadramento35%; geometria25%; tipografia/ícones20%; cores/contraste/sobreposição10%; responsividade/acabamento10%. Nota soma ponderada **>9,0**, meta9,5 e nenhum P1 material. Só auditor independente libera10; média não supera bloqueio de identidade/crop/pixels inventados.
