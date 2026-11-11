# Tela07 — Castings — contrato visual V1

Planejamento de 2026-11-09. Fonte oficial aberta: `MODEL_assets_v1/referencias/07-castings.png` (201×317); original `MODEL_assets_v1/originais/mockup-geral.jpg` (1179×753). Crop global **[11,434,212,751]**, bordas direita/inferior exclusivas, confirmado RGB idêntico (Pillow ImageChops bbox=None). Coordenadas abaixo são locais ao painel.03/04/05/06 aprovadas permanecem intactas. Próximo papel: assets07;08 bloqueada até auditoria07>9,0, meta9,5.

## Conteúdo e geometria

| Região | Box/âncora fonte aproximada | Conteúdo |
|---|---|---|
| Painel | [0,0,201,317] | Papel branco quente, cantos≈12px; nenhuma moldura de telefone adicional |
| Status | hora[15,6,30,13], sinais[156,6,186,14] | **9:41**, celular, Wi-Fi, bateria pretos |
| Header | título x12,y22; plus centro[181,28] | **Castings**, bold≈13px; círculo preto≈18px com mais branco |
| Filtros | y43–58 | **Todos** [12,43,55,58] ativo preto/branco; **Moda** [59,43,97,58]; **Comercial** [100,43,144,58]; **Editorial** [147,43,189,58], fundos cinza muito claro |
| Foto01 | [12,65,74,124] | Homem de cabelo escuro, casaco preto aberto; fundo cinza; manter identidade e enquadramento |
| Card01 | x82,y69–129 | **Campanha Inverno 2025**; **São Paulo, SP**; **18 de mar de 2025**; chips **Moda**, **Editorial**; **Cachê sob consulta** |
| Salvar01 | centro[181,74] | Bookmark contorno preto |
| Foto02 | [12,141,74,204] | Homem de óculos escuros e regata escura; fundo cinza quente; não substituir por foto01 |
| Card02 | x82,y146–205 | **Marca Esportiva**; **Rio de Janeiro, RJ**; **25 de mar de 2025**; chips **Fitness**, **Comercial**; **R$ 1.200 - R$ 2.000** |
| Salvar02 | centro[181,149] | Bookmark contorno |
| Foto03 | [12,219,74,283] | Homem de cabelo escuro, camisa clara aberta, fundo escuro; crop distinto original |
| Card03 | x82,y225–283 | **Editorial Masculino**; **São Paulo, SP**; **30 de mar de 2025**; chips **Editorial**, **Lifestyle**; **R$ 800 - R$ 1.500** |
| Salvar03 | centro[181,227] | Bookmark contorno |
| Tabbar | y289–317; centros x22,61,100,139,179; y301 | Casa preenchida preta ativa, lupa, mais, balão, pessoa de contorno fino cinza |

Metadados por card: localização≈y84/162/239; data≈97/175/252; chips≈110/188/265; cachê≈124/202/279. Títulos≈7px bold fonte, metadados≈6px, chips≈5,5px; Arial/Helvetica/sans-serif nativa. Texto principal preto/quase preto, secundário cinza conforme fonte. Todos textos sobre papel permanecem nativos; não rasterizar título, chips, datas ou valores. Datas são conteúdo estático do mockup, não oportunidades atuais. Quebras pequenas permitidas para caber sem mudar redação. Não adicionar CTA, descrição, marca, duração, badge, contador, aba ou rótulo visível ausente da fonte.

## Assets exigidos

Três fotografias independentes extraídas do original. Boxes globais iniciais:01[23,499,85,558],02[23,575,85,638],03[23,653,85,717]. Refinar cantos/limites pelo JPEG; registrar boxes finais e RGBA geométrico. Nenhuma fotografia pode carregar título, bookmark ou metadados incorporados. Preservar RGB de todos pixels com alpha>0; sem reconstruir corpo, cabelo, fundo ou pixels ocultos, sem imagem gerada/stock, sem reutilizar retrato parecido de outra tela. Upscaling não recupera detalhes. Registrar resolução baixa, identidade/enquadramento e eventual matte JPEG. Se recorte suficiente faltar, bloquear assets, sem substituição.

SVGs locais aproximados da fonte: celular, Wi-Fi, bateria, mais, bookmark, localização, calendário, cachê/moeda, casa, lupa, balão e pessoa. Confirmar pictogramas pequenos no original; documentar incerteza. Sem glifos Unicode, emoji ou fonte de ícones. Manifest, script de extração e ASSETS.md com proveniência, coordenadas e hashes. Referência completa não serve de fundo da interface.

## Adaptação aos viewports

Fonte201×317 possui razão diferente das telas375×812,390×844,430×932. UI fluida: âncoras horizontais W/201, verticais H/317 como ponto de partida; jamais scaleX/scaleY de pessoas. Fotos usam proporção intrínseca individual, object-fit proporcional, sem esticar para preencher altura dos cards. Ajustar espaço entre cards e respiro dos metadados, mantendo todas três linhas de oportunidade e tabbar visíveis em estado inicial. Não ampliar pessoas por eixo diferente. Branco quente≈#f9f8f4, texto≈#141414, chips claros; colher amostras reais na implementação e evitar sombra/gradiente decorativos.

| Âncora y | Fonte | 375×812 | 390×844 | 430×932 |
|---|---:|---:|---:|---:|
| Header centro |28|72|75|82|
| Filtros topo |43|110|114|126|
| Foto01 topo |65|166|173|191|
| Foto02 topo |141|361|375|415|
| Foto03 topo |219|561|583|644|
| Tabbar centro |301|771|801|885|

Valores verticais são alvos da composição, não licença para esticar fotos. Header/filtros estáveis, lista com espaço fluido, tabbar fixa ao rodapé considerando safe-area; overflow vertical permitido apenas se necessário em tamanhos menores que os alvos. Texto não pode colidir com bookmark. Alvos de44×44px CSS, sem áreas sobrepostas; desenhos visuais pequenos dentro dos alvos.

## Interações locais

- Filtros reais em memória: Todos mostra03, Moda mostra01, Comercial mostra02, Editorial mostra01/03, segundo chips visíveis. Seleção aria-pressed e estilo ativo; preservar ordem. Nenhuma busca/backend. Reload restaura Todos e bookmarks vazios.
- Bookmarks alternam estado salvo por card em memória, com label/aria-pressed; não mudar card ao salvar. Clique no bookmark não abre detalhes.
- Clique/teclado no card ou foto abre dialog com a mesma foto e os dados visíveis, informando que é demonstração local. Não inventar briefing, contato ou candidatura. Sem CTA de candidatura/envio.
- Mais do header e da tabbar abre dialog honesto de protótipo: criação indisponível localmente; botão fechar. Não simular anúncio publicado nem adicionar card inventado.
- Tabbar mantém exatamente cinco ícones. Casa pode levar ao Descobrir03 aprovado (`../MODEL_tela_03_V2/index.html`), pois02 original não tem código aprovado neste escopo. Lupa abre painel/dialog local de navegação demonstrativa sem implementar08. Balão leva06 aprovado (`../MODEL_tela_06_V1/index.html`), oferecendo retorno à sequência06 por controle já visível. Pessoa abre painel local explicando indisponibilidade da área de perfil; não iniciar10. Não criar back-arrow no header nem abas extras. Destinos aprovados04/05 podem ser apresentados somente em painéis locais quando contextualizados; não criar02/08/09/10/11. Não alterar06 para inserir backlink.
- Dialogs com título, fechar, Escape, foco contido e restaurado. Foco visível em todos controles, nomes acessíveis, ordem lógica, conteúdo seguro via textContent. Preferir card como botão sem controles interativos aninhados: bookmark irmão separado.
- Foto com erro tem fallback local honesto e mantém geometria, sem substituir pessoa; SVG ausente não vira glifo quebrado. Reduced-motion, teclado e44px verificados. Nenhuma rede externa/backend/persistência/publicação.

## Auditoria e gate

Capturas reais finais375×812,390×844,430×932 DPR1; navegador/procedimento/versão/hashes documentados. Comparação390 e referência à mesma altura, cada proporção preservada. Abrir todas imagens e comparação. Auditor independente atribui fotografia/identidade/enquadramento35%, geometria25%, tipografia/ícones/chips20%, cores10%, responsividade/acabamento10%; gate **>9,0**, meta9,5, sem bloqueador material. Notas anteriores não se transferem. Console/rede/assets/overflow/foco/44px/dialogs/Escape/filtros/save/retorno06/falha de fotos/reduced-motion entram no relatório. Só aprovação07 libera planejamento08.
