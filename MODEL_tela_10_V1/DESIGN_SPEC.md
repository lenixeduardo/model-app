# Tela10 — Meu Perfil — contrato visual V1

Planejamento de 2026-11-11, liberado pelo gate09 aprovado9,27/10 (soma9,265), sem P1 material.08 aprovada9,23. Preservar03–09 e suas evidências. Referência aberta: `MODEL_assets_v1/referencias/10-meu-perfil.png`,185×317. Original aberto: `MODEL_assets_v1/originais/mockup-geral.jpg`,1179×753. Crop global **[612,434,797,751]**, direita/inferior exclusivas, RGB idêntico confirmado com Pillow ImageChops (bbox=None). Coordenadas locais abaixo aproximadas; assets deve refiná-las. Não iniciar11 antes do gate10 próprio>9,0; meta9,5.

## Hierarquia e conteúdo original

| Região | Box/âncora local aproximada | Conteúdo verificável |
|---|---|---|
| Papel | [0,0,185,317], cantos≈12 | Branco quente, sem moldura extra |
| Status | hora[15,7,29,13]; sinais[143,7,173,14] | 9:41, sinal celular, Wi-Fi, bateria pretos |
| Header | voltar centro[15,28]; título[68,22,115,31] | **Meu Perfil**, centralizado; chevron simples à esquerda |
| Avatar | círculo bbox[53,39,129,116] | Retrato masculino original desta10, cabelo escuro, fundo cinza; frame circular integral |
| Editar | centro[118,103], suporte≈[107,93,129,115] | Pequeno lápis/editar preto em suporte claro circular sobre borda inferior direita |
| Identidade | centro x92,y126 | **Matheus Silva, 24**, bold, selo preto de verificação à direita |
| Localização | centro x92,y142 | Ícone pin e **São Paulo, SP** |
| Tags | centros x45/91/138,y159 | **Fashion**, **Editorial**, **Comercial** em três pills claras |
| Medidas | centros x36/92/148,y182 e194 | **1,85 m** / **80 kg** / **42**; legendas **Altura** / **Peso** / **Manequim** |
| Linha01 | ícone x22, texto x39,y217; chevron x165 | **Meu portfólio** |
| Linha02 | mesmos x,y233 | **Disponibilidade** |
| Linha03 | mesmos x,y249 | **Cachê** |
| Linha04 | mesmos x,y265 | **Estatísticas** |
| Linha05 | mesmos x,y280 | **Planos e assinaturas** |
| Navbar | divisor≈y290; centros x21/56/91/126/163,y301 | Casa contorno, busca, mais, chat contorno, perfil preto preenchido ativo |

A fonte mostra **cinco** entradas de menu, não seis. Não há bio, botão sair, notificações, plano atual, preço ou sexto item legível. Não acrescentar para completar uma expectativa de quantidade. Ícones das linhas: portfólio/calendário-quadro, disponibilidade/relógio-calendário, cachê/bolsa, estatísticas/barras, planos/usuário; detalhes minúsculos são aproximações SVG a validar visualmente, sem afirmar semântica extra. O selo é preto, não o azul de Enzo. Matheus Silva é o nome da10; não renomear para Enzo nem trocar seu retrato por outro rosto semelhante presente em outras telas.

Texto HTML nativo `Arial, Helvetica, sans-serif`, sem legendas raster e sem fonte remota. A fonte tipográfica original não pode ser comprovada pelo JPEG: Arial é a escolha técnica explícita, não identificação forense. Título≈10px bold local; nome≈9px bold; cidade≈6,5px; tags≈6px; valores≈8px bold; legendas≈6px; menu≈7,5px; hora≈6px. Na390, multiplicador horizontal390/185≈2,108: título≈21,1px, nome≈19px, menus≈15,8px. Ajustar por comparação sem scaleX/scaleY da fonte. Fonte primária dos dados é exclusivamente a referência10 confirmada ao original; telas03/06/07/08/09 fornecem contexto de navegação, não identidade substituta.

Amostras RGB reais da referência idêntica ao original: papel[10,200,175,207] dominante(248,247,243),196pixels, seguido(249,248,244),163; papel inferior[10,284,175,289] dominante(248,247,243),152; chip[29,155,60,162] dominante(239,238,234),13. Usar papel próximo **#f8f7f3/#f9f8f4**, chips≈#efeeea, preto≈#101010, secundário cinza a amostrar pelo agente de assets. Variação JPEG não exige gradiente decorativo. Sem sombra adicional.

## Contrato de assets e identidade

Um avatar independente, extraído exclusivamente dos pixels RGB do retrato10. Crop preliminar global[665,473,741,550]; refinar caixa circular conservando todo o frame fonte visível e proporção, sem cortar cabeça/ombro para preencher outra caixa. A largura/altura final deve conservar ratio intrínseco; o círculo é máscara geométrica, não deformação. Mesmo que a borda raster sugira diferença de1px nas dimensões, conferir círculo e registrar escolha. Não aplicar object-fit:cover em caixa incompatível, esticar verticalmente, trocar por Enzo ou outro homem, inventar anatomia, fundo, textura ou pixels ocultos. Ampliação não recupera detalhe.

Editar está sobreposto ao retrato: separar alpha somente no footprint real de UI. Cobrir integralmente lacuna com suporte opaco independente e SVG co-registrado, documentando qualquer matte JPEG residual. Não tentar recuperar pixels sob área translúcida/inpaint. O suporte persiste em todos estados, inclusive dialog aberto, edição local e falha do ícone, para não revelar buraco. RGB de todo pixel visível preservado contra fonte; exterior circular e lacuna ficam transparentes. Manifest deve registrar coordenadas globais/locais, máscara, hashes, dimensões e prova RGB. Se o insumo não permitir retrato suficiente fiel, registrar bloqueio, sem substituto. Não usar screenshot integral nem menu rasterizado como fundo.

SVGs locais para status/back/editar/selo/pin, cinco menus/chevrons e cinco nav. Reconstruções são aproximações declaradas, com viewBox e traços refinados na fonte. Reuso de aprovadas por hash e adequação é permitido; não importar legendas ou pessoa de outro pacote.

## Ações locais honestas

- Estado inicial reproduz a fonte. Estado apenas em memória; reload restaura. Sem backend, upload/envio externo, pagamento, login ou persistência alegada. Não acrescentar banners de demonstração ao repouso; explicar limites nos dialogs ao agir.
- Voltar: histórico local válido ou fallback09 aprovada. Editar abre dialog acessível de edição local dos dados fonte; mudanças somente em memória, cancelar descarta. Foto não é trocada por pessoa inventada; controle pode informar que não há upload nesta demonstração. Nome/idade/medidas editados deixam de ser estado inicial de comparação e não herdam selo automaticamente como verificação real. Texto seguro via textContent.
- Meu portfólio: dialog de Matheus, informando que não há portfólio próprio disponível no pacote. Não abrir05/04 como se o portfólio de Enzo fosse de Matheus. Não inventar fotos/trabalhos; o avatar genuíno pode ser mostrado como retrato, sem chamá-lo trabalho comercial.
- Disponibilidade: dialog com seleção local opcional e estado inicial não informado, sem inferir disponibilidade atual. Cachê: dialog informa ausência de valor definido na fonte; nenhuma tarifa ou proposta é inventada/enviada. Estatísticas: sem métricas no mockup; informar indisponíveis nesta demonstração. Planos e assinaturas: sem planos/preços na fonte; dialog explicativo, sem compra/checkout/cobrança.
- Navbar: casa→`../MODEL_tela_03_V2/index.html`; busca→`../MODEL_tela_07_V1/index.html`; mais→dialog local de demonstração; chat→`../MODEL_tela_06_V1/index.html`; perfil→estado atual10 (anúncio local se necessário). Destinos mesma aba, sem links mortos.09 é fallback de retorno;08 pode ser link contextual de filtros em ação local explicitamente rotulada, sem trocar navegação original. Não editar03–09 para inserir links e não criar11.
- Alvos44×44px, foco visível, nomes acessíveis, aria-current da nav, ordem de leitura e tab coerentes. Os cinco itens precisam caixas≈44px sem overlap; ampliar respiro em telas-alvo em vez de sobrepor hitboxes. Dialog com título, fechar, Escape, contenção/restauração de foco e rolagem interna se necessário. Reduced-motion; fallback de avatar mantém geometria e nome/aviso, nunca outra pessoa. SVG com fallback legível, sem glifo quebrado. Ações não podem alegar confirmação externa.

## Proporção, evidências e gate

Horizontais W/185; verticais porH/317 como âncoras, sem alongar o avatar. Em390×844, avatar≈160×162px pela dimensão intrínseca, centro≈[192,206]; header y≈71; nome y≈335; tags y≈423; valores y≈485; menus y≈578/620/663/706/746; nav y≈802. O avatar começa≈104 e termina≈266 por escala horizontal, deixando respiro até identidade. Refinar com comparação preservando integralmente frame e hierarquia. Margens menus≈35–42px em390; nomes/valores não colidem com ícones.375×812 e430×932 mantêm todos os cinco menus e navbar visíveis, sem overflow horizontal, com safe area incluída e nav sem cobrir última linha. Não escalar altura de fotos porH.

Implementador deve abrir candidata390 antes das finais; screenshots reais default375×812,390×844,430×932,DPR1, com navegador/versão/procedimento/hashes. Abrir três capturas e comparação390/ref normalizada à **altura844**, cada imagem proporcional sem stretch. Não aceitar recorte do editor/mockup como captura do app. Verificar console/rede/assets/overflow, ratio/cobertura do avatar, menus/edit/cancelar/reload/back/nav, teclado/foco/Escape/44px/reduced-motion/fallback. Registrar testes realmente feitos e limites.

Auditor independente aplica fotografia/identidade/enquadramento35%, geometria25%, tipografia/ícones/chips20%, cores/contraste/sobreposição10%, responsividade/acabamento10%. Soma>9,0, meta9,5; exatamente9 não libera. Nenhum P1 material, especialmente identidade errada, frame perdido ou pixels inventados, mesmo com média alta. Nota não é transferida da09 nem forçada a10. Só gate10 libera planejamento11.
