# Tela 03 V2 — plano de revisão pela fila de agentes

Data: 2026-11-09. Papel: planejamento. Estado atual: implementação funcional e capturada, nota independente **7,74/10**, não aprovada. Critério atualizado do usuário: nota **superior a 9,0/10**; meta 9,5. Não iniciar conteúdo ou implementação da Tela 04 antes desse aceite.

## Diagnóstico com evidência visual

Foram lidos `DESIGN_SPEC.md`, `AUDITORIA.md`, `README.md` e `../docs/CODEX_TELA_03.md`. Foram abertas a referência oficial isolada (203×404) e a captura real de 390×844. Na referência, Enzo ocupa quase todo o fundo e seu torso permanece visível atrás de nome, localização e categorias. Na V2, o retrato limpo termina aproximadamente em 62% da altura, é dissolvido em preto e deixa o nome sobre uma área preta extensa. O rosto e os ombros conservam a proporção natural; isso não supre a área ausente.

A foto em runtime é `assets/enzo-swipe-referencia.png`, 201×242, originada do recorte limpo do mockup. A referência completa tem interface incorporada. O céu final é preenchimento CSS amostrado do retrato, não fotografia integral recuperada. Os testes técnicos passaram, mas esses resultados não resolvem a diferença de composição.

## 1. Entrega seguinte — agente de assets

Executar nesta ordem, sem alterar o código da tela:

1. Inventariar os arquivos fotográficos realmente disponíveis em `../MODEL_assets_v1/originais/`, `../MODEL_assets_v1/referencias/` e `assets/`; registrar caminho, dimensões, origem e o que contém interface incorporada. Abrir os arquivos relevantes, sem presumir que o anexo completo é o original limpo da fotografia.
2. Conferir se alguma fonte já fornecida contém **o mesmo retrato completo**, com o torso que a referência mostra. Recortes de outra pose, ainda que de Enzo, não atendem esse requisito. A foto de login não é substituta.
3. Se houver pixels suficientes em uma fonte limpa, exportar o asset preservando a proporção, documentar coordenadas e fornecer prévia. Não remover textos por geração/inpainting nem completar corpo oculto: isso fabricaria informação ausente, em conflito com o contrato atual.
4. Se não houver fonte suficiente, criar `ASSETS.md` registrando o bloqueio e a especificação do insumo faltante: foto original limpa do mesmo enquadramento, céu/ombros/torso completos, sem interface, idealmente resolução superior aos 430px da viewport (preferível >=860px de largura para DPR2). Resolução maior é desejável, não substitui o enquadramento correto.
5. Revisar os SVGs do X, selo e demais ações contra a referência. Entregar ajustes vetoriais permitidos como arquivos separados, com dimensões/espessuras propostas e indicação de que são aproximações. Não alegar vetor original.
6. Produzir `ASSETS.md` com três classes: original/extração fiel; aproximação vetorial/CSS identificada; insumo ausente. Entregar o inventário e a decisão sobre a fotografia ao implementador e ao auditor.

Se o torso não estiver disponível, essa etapa termina em **bloqueio fotográfico documentado**. Não criar uma fotografia alternativa para manter a fila andando.

## 2. Refinamentos de UI que podem ser implementados

Esses ajustes são independentes da obtenção do original e podem melhorar a V2, mas não asseguram nota >9:

- Comparar traço e escala interna do X/estrela/coração com a referência, preservando os alvos de toque >=44px e a geometria dos círculos.
- Calibrar o selo em relação ao nome; a auditoria observa selo um pouco pequeno.
- Calibrar altura, preenchimento, espaçamento e borda dos chips; a auditoria observa chips mais finos/compactos.
- Reavaliar a evidência dos controles superiores em relação ao painel oficial, preservando a presença de voltar/opções exigida no contrato.
- Manter textos, hierarquia, cinco segmentos e comportamento local; não adicionar novos modelos, rótulos ou navegação para a Tela 04.
- A fonte permanece aproximação até receber o arquivo ou identificação verificável da família original. Não alegar correspondência exata apenas por semelhança.

O implementador registra as mudanças em `CHANGELOG.md`. Se optar por entregar somente refinamentos com a foto parcial, preservar a versão anterior e marcar a nova como **não aprovada / limitação fotográfica mantida**.

## 3. Integração quando existir fotografia suficiente

1. Validar origem, identidade e proporção com o agente de assets.
2. Substituir somente o asset correspondente; usar `object-fit: cover`/`object-position` ou enquadramento proporcional equivalente, sem definir largura/altura independentes que deformem Enzo.
3. Recalibrar a escala/posição do rosto, cabeça, ombros e torso em cada viewport. Mostrar a fotografia por trás das informações como na referência; não usar preto para esconder uma área que o novo original contém.
4. Recalibrar a sobreposição escura para legibilidade sem apagar o torso; verificar o conjunto antes de mexer em tipografia/ícones.
5. Aplicar os refinamentos de UI e executar a verificação abaixo.

## 4. Verificação e auditoria da nova versão

Executar:

```sh
python MODEL_tela_03_V2/render.py --chromium /usr/bin/chromium
python MODEL_tela_03_V2/compare.py
```

Se o sandbox bloquear sockets/Chromium, registrar o erro e usar apenas a estratégia permitida pelo ambiente. Não substituir captura por montagem do mockup.

Entregar os três PNGs finais (375×812, 390×844, 430×932), `relatorio-browser.json`, comparação de390 com proporções preservadas, changelog e versão. Conferir imagens/SVGs, console/rede, overflow, estados de curtir/favoritar, ignorar/desfazer, teclado/foco, áreas de toque, redução de movimento e fallback de foto. Testes de Chromium não certificam VoiceOver ou safe areas reais de aparelho físico; documentar a limitação.

O auditor independente deve abrir referência e capturas finais e atribuir as cinco notas com pesos35/25/20/10/10. A nota atual não se transfere à nova versão. Nenhum bloqueador material, captura ausente ou deformação pode ser compensado pela média. Só nota **>9,0** e evidência completa libera a Tela04. Nota9,0 exata continua abaixo do gate atualizado.

## 5. Limite e condição de parada

A nota de fotografia atual é6,2/10, peso35%. Mesmo com todos os demais critérios hipoteticamente em10, a média seria8,67. Esse cálculo é apenas uma demonstração do peso do bloqueio; não é uma previsão de nova nota. A auditoria deve avaliar cada nova versão pelas imagens.

Enquanto faltar a fotografia suficiente, não existe fundamento para prometer >9 somente com CSS/ícones. O resultado correto é entregar o que foi implementado, registrar o bloqueio e manter a fila pausada na Tela03. Retomar após receber/verificar o insumo, ou após nova instrução explícita do usuário que altere o contrato de fidelidade.

## Checklist de handoff para assets

- [ ] Inventário com dimensões e origem de cada candidato fotográfico.
- [ ] Confirmação visual de identidade/pose do retrato oficial.
- [ ] Fonte limpa integral encontrada, ou declaração demonstrada de ausência.
- [ ] Asset fiel exportado com coordenadas, se possível; nenhuma fotografia fabricada.
- [ ] Propostas de ajustes dos SVGs independentes e identificadas como aproximações.
- [ ] `ASSETS.md` entregue e estado da fotografia comunicado ao implementador/auditor.

O arquivo `../docs/FILA_AGENTES.md` mantém a ordem das telas e os gates. O conteúdo da Tela04 permanece fora deste plano.

## Revisão de rota após o ciclo4 — aproveitar o torso já visível no mockup

Reabertas visualmente a referência completa03, a captura390 do ciclo4 e o mockup integral. A nota atual no arquivo de auditoria é7,84; este plano não altera essa nota. A constatação relevante é mais precisa que «não existe torso»: **o mockup contém muitos pixels do torso fora dos overlays; o recorte201×242 deixou esses pixels de fora**. Não há fonte integral limpa, mas há uma próxima tentativa sem sintetizar anatomia.

### Próxima ação prioritária: extração com lacunas transparentes

O agente de assets deve produzir uma variante experimental separada, sem substituir o asset atual:

1. Partir do painel03 completo `[420,0,623,404]`, preservando dimensões203×404 e a proporção natural. O arquivo é a fonte raster, não uma fotografia limpa.
2. Remover a interface incorporada por **transparência**, sem preencher os pixels removidos, clonar pele ou gerar corpo. Remover status, segmentos, nome/selo, localização, chips, informação, três círculos e gesto inferior; também retirar eventual franja/bege externa à área da tela. Não exportar a captura intacta como fundo.
3. Conservar literalmente os pixels fotográficos visíveis fora dessas regiões, em especial rosto, cabelo, pescoço, ombros e torso ao redor/entre as legendas. O fato de haver torso preservável precisa ser usado na tentativa; não limitar novamente a exportação à faixa limpa superior.
4. Registrar as regiões/máscaras em `assets/mask-manifest.json` e salvar a variante como `assets/enzo-mockup-foto-com-lacunas.png`. Nome e `ASSETS.md` devem identificá-la como **extração parcial com lacunas**, não original recuperado nem fotografia integral limpa. A sobreposição escura já incorporada ao mockup permanece nos pixels visíveis; isso também deve ser declarado.
5. Comprovar que os pixels com alpha255 fora das máscaras são os da fonte, sem troca do rosto/pose. Abrir a variante sobre fundo quadriculado e sobre preto para verificar resíduos de letras, ícones ou bordas. Máscaras devem ser tão pequenas quanto o conteúdo real permitir, sem deixar UI reconhecível; as caixas abaixo são pontos iniciais conservadores, não coordenadas de precisão aprovadas.

Coordenadas locais iniciais para inspeção manual (x1,y1,x2,y2), em203×404:

| Overlay | Região inicial aproximada |
|---|---|
| Hora / status | `(12,2,38,17)` e `(156,2,198,17)` |
| Progresso | `(12,20,190,27)` |
| Nome e selo | `(12,272,92,292)` |
| Localização | `(12,292,116,308)` |
| Informação | `(172,282,193,305)` |
| Chips | `(12,310,170,333)`, refinando separadamente cada chip |
| Ignorar / favoritar / curtir | `(26,339,75,389)`, `(77,339,126,389)`, `(128,339,178,389)` |
| Gesto | `(67,392,137,403)` |

O agente deve conferir os limites visualmente na fonte. Não usar essas caixas cegamente nem remover grandes áreas de torso por conveniência. Não preencher os buracos com tons de pele: transparência significa dado ausente, não dado recuperado.

### Teste de integração permitido, com versão reversível

O implementador pode criar um ciclo experimental usando a variante sobre o fundo preto existente, com o DOM de toda a interface independente. Deve manter o asset/capturas atuais preservados. Ajustar o enquadramento proporcional da nova imagem: o painel completo tem razão203/404, diferente da viewport390/844; `cover` ou imagem natural dimensionada proporcionalmente deve ser calibrado e não deformado para encaixar.

Primeiro capturar390 e abrir lado a lado com a referência. O teste é útil se o torso reaparece onde hoje há a grande faixa preta, sem letras/ícones duplicados. Não basta esconder a referência intacta atrás do DOM. As lacunas terão preto por baixo e podem aparecer como remendos; se isso ocorrer, registrar o que foi preservado e o que segue ausente. O deslocamento entre máscaras da fonte e controles do DOM precisa ser avaliado, pois alinhamento imperfeito pode tornar os remendos evidentes.

Se houver melhora real, recapturar375/390/430, verificar interações/carregamento/overflow e enviar ao auditor independente. Se as lacunas e a sobreposição incorporada forem visualmente materiais, **rejeitar a variante para aceite**, manter a evidência experimental e passar à condição abaixo. Essa opção não garante nota>9 e não altera a rubrica.

### Alternativa ImageGen: derivação aproximada exige autorização específica

A hipótese de remover a UI por ImageGen pode produzir uma composição mais próxima, porque a maior parte da pessoa/pose já está visível e a remoção seria localizada. Entretanto os pixels de pele/céu atrás de texto, chips e controles são desconhecidos: a ferramenta os estima. Isso é reconstrução generativa de um asset derivado, não extração fiel ou recuperação do original. Também há risco de alterar rosto/pose ou a textura já visível; o resultado deve ser rejeitado se isso ocorrer.

O contrato inicial manda solicitar o original quando o recorte for insuficiente e não fabricar fidelidade. A autorização geral de gerar assets/publicar arquivos não deve ser interpretada, sozinha, como autorização para substituir esse requisito por pele reconstruída. **Antes de testar essa alternativa, é necessária uma autorização explícita do usuário para a reconstrução aproximada das regiões encobertas do mesmo retrato**, sem substituir Enzo ou usar outra foto. Formulação concreta para obter essa decisão:

> Autoriza remover por IA os textos, ícones e controles da fotografia do painel03 do mockup, reconstruindo apenas os pixels encobertos como aproximação, sem trocar Enzo, rosto, pose ou enquadramento, e usar esse asset derivado na implementação e na auditoria, identificado como reconstrução e sem garantia de nota?

Se autorizada, o agente de assets registra essa decisão e mantém fonte/derivado separados; solicita somente remoção dos overlays dentro do quadro existente, sem outpainting, nova pose, corpo novo ou «melhoria» estética. Rosto/cabelo/ombros visíveis são áreas protegidas. O auditor compara a identidade/pose, anatomia, textura e posição com o mockup e pode rejeitar o asset, mesmo que os controles estejam corretos. A auditoria deve explicitar o que foi reconstruído e **não atribuir fidelidade ao arquivo original inexistente**. Aprovação continua dependente das capturas finais e do gate>9; não é consequência da autorização de geração.

Sem essa autorização específica, a rota generativa não é executada. A tentativa com transparência acima pode ser feita agora por aproveitar somente pixels existentes e documentar lacunas; se ela não sustentar o aceite, o próximo insumo continua sendo a foto original limpa ou a decisão explícita sobre reconstrução derivada.

### Calibração geométrica inicial da variante203×404

Os três viewports exigidos têm razão próxima de0,462, contra203/404≈0,502 do painel. Exibir a nova imagem somente com `width:100%; height:auto` põe os overlays mascarados cerca de40px acima do DOM no caso390×844 e tende a expor os buracos. A primeira hipótese a testar é `object-fit:cover`, quadro100%×100dvh e escala proporcional pela altura:

- Em390×844, escala844/404≈2,089; largura fotográfica≈424px, excesso horizontal≈34px.
- `object-position-x` próximo de8% recorta cerca de2,7px no lado esquerdo. O x14 da referência passa a aproximadamente26,5px na viewport, perto da margem7% do DOM (27,3px).
- O y275 da referência passa a574,5px, perto do nome atual em torno de570px. Ajustar somente após a captura, sem deformar a fotografia nem prometer alinhamento de todas as máscaras.

O teste de antiestiramento existente compara a razão da caixa `<img>` à razão natural. Essa asserção pode dar um falso erro quando a caixa usa `object-fit:cover`: a caixa é estreita, mas o conteúdo continua proporcional e é recortado. O implementador precisa conferir a escala efetiva do conteúdo (`max(larguraCaixa/larguraNatural, alturaCaixa/alturaNatural)`), dimensões cobertas e corte por `object-position`; não remover a verificação de proporção para «passar o teste». Outra implementação válida é posicionar uma imagem com dimensões naturais escaladas pela altura em um contêiner com overflow oculto, se preservar essa mesma geometria. O auditor deve julgar a captura e as lacunas visíveis, não somente o valor do teste.

## Ciclo6 — co-registro de UI independente e acabamento sem síntese

Referência, captura390 do ciclo5, CSS, `ASSETS.md` e nova auditoria8,72 foram abertos/lidos. O gap dominante agora não é falta total de torso: são silhuetas de UI removida que o DOM não recobre, especialmente nome/localização/status e discos de ação. Esta revisão substitui a condição antiga de parar apenas por ausência do original: há uma tentativa adicional concreta e reversível usando as camadas já extraídas.

### Decisão de geometria

Manter `object-position:8% 50%` neste ciclo. Nome/localização e suas máscaras seguem o mesmo mapa da fotografia: unidade`u=altura/404`, largura fotografada`203u`, deslocamento horizontal`(larguraViewport−203u)×0,08`. Não trocar para50% enquanto se corrige a tipografia: isso deslocaria o nome para perto de12px de margem em390 e introduziria outra divergência. Também não projetar os círculos para deixar o conjunto aproximadamente13px fora do centro da viewport só para recobrir as máscaras.

Para os círculos, testar uma solução de camada: base verdadeiramente preta e **fade do alpha da fotografia aproximadamente de82% a85% da altura** (fontey≈331..343; em844px,≈692..718px), depois dos chips e antes dos vazios das ações. Isso retira visualmente os discos deslocados, sem gerar pele ou mover os três botões centrados. A referência já se aproxima do preto nessa área inferior. O teste deve preservar o torso e a textura atrás das informações/chips; não repetir o grande preto que apagava o corpo nas primeiras versões. O alfa é multiplicado pela máscara existente; os RGB preservados do asset não são reescritos. Se a transição ficar como faixa artificial ou apagar torso que a referência mostra, o auditor deve apontar a regressão.

### Próxima ação antes da implementação: candidato tipográfico do agente de assets

Produzir variantes separadas de `name-type.svg` e `location-type.svg` com **somente os contornos dos glifos visíveis** do nome e da localização. Isso é uma camada visual de UI independente, admissível como aproximação tipográfica; não é nova fotografia nem descoberta da fonte original. Não extrair o retângulo fotográfico com as letras dentro.

Requisitos da extração:

- Cada SVG contém apenas paths/contornos vetoriais dos glifos, com preenchimento uniforme branco/claro e fundo transparente. Não usar `<image>`, raster embutido, caixa com RGB fotográfico, retalho de pele/céu ou pixels ao redor como «halo». Não reproduzir RGB por pixel da fonte: nas bordas antialias esses valores já estão misturados com pele/céu e podem carregar fotografia para a camada de UI.
- O manifesto registra a caixa local `(x,y,w,h)` na fonte203×404, e o `viewBox` mantém exatamente essa geometria. O implementador projeta a caixa pelo mesmo`u`/offset da foto, sem calcular uma nova baseline com Arial.
- Máscara de remoção e pintura visual devem usar uma geometria comum verificável. Caso o corte seja maior que o glifo pintado, persistirá o halo negro. A dilatação de1px atual gera699pixels removidos para317sementes no nome; pintar essa expansão inteira de branco pode engrossar demais o nome. Comparar o contorno reconstruído e o peso com a referência antes de entregar; não tratar «buraco coberto» como fidelidade automática.
- Se for necessário aproximar antialias, usar apenas cobertura/alpha geométrico do glifo, não cores da fotografia. Documentar a aproximação. O asset fotográfico precisa continuar sem UI reconhecível; não resolver o problema deixando letras raster no fundo.
- Manter o selo como SVG independente; sua posição/dimensão deve cobrir a máscara correspondente sem um segundo contorno negro. Não incluir o selo azul na seleção de glifos neutros do nome.
- Entregar prévia de cada SVG sobre fundo neutro e composição somente para inspeção com a fotografia mascarada, além dos SVGs/manifesto independentes. Composição de inspeção não substitui captura nem vira fundo de runtime.

Este é o candidato prioritário porque uma fonte aproximada diferente não tem os mesmos contornos das lacunas. Arial alinhada por baseline pode continuar como fallback, mas não garante o recobrimento de cada silhueta removida.

### Status: evidência antes de alterar o threshold

A inspeção do agente de assets constatou que a máscara anterior do status atinge glifos/halosJPEG nas caixas locais, não uma região arbitrária de nuvens: hora58sementes/135pixels após dilatação, boundsx17..34,y5..13; ícones118sementes/229pixels, boundsx159..193,y5..12. A hipótese inicial de simplesmente estreitar a neutralidade para range<=25 é insuficiente: sinal celular contémRGB221,240,255(range34), e esse limite deixaria resíduos.

O agente pode testar minRGB125/140 com range<=36, mas somente se a inspeção mostrar remoção integral da UI e preservação do céu. Registrar a comparação com a máscara anterior; não anunciar que estreitar o threshold resolveu o status sem ver a composição. Co-registrar posição/escala da hora e dos ícones nativos à geometria da fonte. Se o contorno/fonte da hora continuar expondo lacunas, uma variante de UI tipográfica vetorial da própria hora, seguindo os mesmos requisitos sem RGB fotográfico, é uma possibilidade restrita; não adicionar uma faixa decorativa opaca para esconder o erro.

### Integração pelo implementador

1. Preservar assets/capturas do ciclo5. Receber os SVGs e manifesto, conferir que não contêm imagem ou fotografia embutida e que o alinhamento está especificado.
2. Manter o`h1` real com «Enzo,26» e o`p` real com «São Paulo,SP ·1,84m» no DOM acessível, com a grafia/espaçamento original corretos. A camada visual de paths é decorativa (`alt=""`/`aria-hidden="true"`). Quando a visualização vetorial estiver ativa, aplicar a técnica sr-only aos textos nativos; não usar`display:none`/`aria-hidden` nos textos semânticos. O leitor de tela não deve receber duas cópias.
3. Posicionar cada visual tipográfico pela caixa fonte projetada. A geometria da caixa, a máscara e a foto precisam permanecer co-registradas em375/390/430; não usar nudges absolutos independentes por viewport para esconder erros locais.
4. Ajustar selo/status na mesma projeção onde necessário. Preservar o alvo>=44px da informação e a semântica/interação das ações; a imagem tipográfica não intercepta clique/toque (`pointer-events:none`).
5. Aplicar o fade inferior de alpha e basepreta mantendo as ações centradas. Não mudar simultaneamente o enquadramento da foto, a cor da pele ou a anatomia.
6. Capturar390 primeiro e inspecionar em escala real e zoom: halos negros, peso do nome, localização, selo, status e contorno dos círculos. Se houver melhora concreta, gerar os três tamanhos e repetir testes completos. Se os SVGs produzirem letras muito grossas, resíduos ou aparência pixelada discrepante, rejeitar essa candidata e registrar; não forçar a nota.

### Revalidação

`AUDITORIA.md` do ciclo5 permanece intacta até a nova captura. O auditor deve abrir a referência e os três PNGs finais do ciclo6 e fazer nova rubrica, sem receber instrução de aprovar. Critérios específicos: torso mantido, nenhum texto/ícone duplicado ou halo fotográfico em asset UI, ausência de discos deslocados, legibilidade e peso tipográfico próximos da referência, geometria natural de Enzo e ausência de regressões técnicas. O gate segue>9,0, meta9,5; estas mudanças são uma hipótese de melhoria, não uma nota predeterminada.
