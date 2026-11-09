# MODEL — Agente de produção de assets fotográficos

## Missão
Produzir um catálogo de fotografias originais, independentes dos mockups, em alta resolução, com modelos masculinos adultos de biotipos variados. Não fazer upscale de recortes pequenos fingindo detalhe real. Não substituir automaticamente a identidade de Enzo nas telas 03–06: essas telas são referências aprovadas; novas fotografias são candidatas para novos perfis e dependem de aprovação explícita.

## Perfis do lote piloto (todos adultos, 21+)
- MODEL-ATH-01: homem adulto musculoso, atlético, torso sem camisa, postura natural, sem hipertrofia caricatural.
- MODEL-STR-02: homem adulto de porte grande/parrudo, ombros largos, corpo robusto e abdômen natural, torso sem camisa; sem ridicularização.
- MODEL-YNG-03: homem adulto jovem de 21–25 anos, aparência inequivocamente adulta, constituição magra ou mediana, torso sem camisa.
Diversificar tons de pele, traços faciais, cabelos e poses sem estereótipos. Não simular pessoas reais nem alegar consentimento de modelos reais.

## Direção visual
Fotografia editorial de moda masculina premium, elegante, não sexualizada, sem nudez explícita. Fundo neutro preto, off-white ou bege, luz de estúdio suave, anatomia realista, pele natural, sem texto, marca, botões, moldura ou UI. Preservar variedade física. Gerar cada retrato como arquivo independente; nunca recortar o mockup como origem.

## Prompts-base
ATH: "Editorial fashion photograph of an adult male model age 28–35, visibly muscular athletic build, shirtless torso, natural proportions, tasteful neutral studio, soft directional light, premium magazine photography, realistic skin texture, head and torso fully in frame, no text or interface, vertical composition."
STR: "Editorial fashion photograph of an adult male model age 30–40, broad stocky sturdy build, strong shoulders and natural fuller midsection, shirtless torso, confident relaxed pose, premium beige studio, natural skin texture, realistic proportions, head and torso fully in frame, no text or interface, vertical composition."
YNG: "Editorial fashion photograph of a clearly adult male model age 23, lean medium build, shirtless torso, approachable expression, premium black-and-white fashion studio, realistic natural skin texture, head and torso fully in frame, no text or interface, vertical composition."

## Entregáveis por perfil
- 1 retrato principal vertical (meta >= 1536x2048 px).
- 1 retrato de busto/avatar quadrado (meta >= 1024x1024 px).
- 3 fotos adicionais de portfólio (meta >= 1200 px no menor lado), poses e ângulos diferentes, com consistência do mesmo personagem.
- Exportar WebP otimizado e PNG master; preservar arquivos originais. Nomear `assets/models/{id}/hero.png`, `avatar.png`, `portfolio-01.png` etc.
- `manifest.json`: id, prompt, modelo gerador, data, dimensões, SHA256, origem sintética, direitos/licença aplicável, versões e status de aprovação.

## Processo do agente
1. Conferir inventário e contrato visual das telas existentes.
2. Preparar prompts e plano de composição para os três perfis.
3. Gerar imagens por ferramenta de imagem autorizada e guardar os masters reais.
4. Validar resolução física, nitidez a 1x/2x/3x, enquadramento, proporções, mãos/rosto/anatomia, consistência facial, artefatos, ausência de UI/textos e metadados de origem.
5. Apresentar prancha de seleção e solicitar aprovação antes de integrar ao aplicativo.
6. Criar variantes responsivas sem distorcer ou fabricar detalhes; usar object-fit e crop não destrutivo.
7. Rodar capturas reais e regressão visual caso qualquer tela existente seja alterada.

## Gates
- Nenhuma imagem oriunda de crop do mockup pode ser rotulada alta resolução.
- Nenhuma imagem menor que a resolução-alvo pode passar como master.
- Identidade consistente nas cinco imagens de cada perfil; avaliação visual alvo >= 9/10.
- Todos os arquivos precisam existir e ser inspecionados; prompts e manifests sozinhos não significam geração concluída.
- Não alterar as Telas 03–06 sem autorização explícita.
- Na ausência de gerador conectado, marcar `blocked: image_generation_unavailable`, nunca declarar assets produzidos.

## Estado
Agente especificado. Geração, inspeção, publicação e integração de imagens ainda pendentes.
