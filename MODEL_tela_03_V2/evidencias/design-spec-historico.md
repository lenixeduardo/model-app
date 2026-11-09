# Tela 03 — especificação V2

Contrato: docs/CODEX_TELA_03.md e handoff do usuário. Implementação nova, pois o repositório não contém a V2 anterior. Referência: MODEL_assets_v1/referencias/referencia-tela-03.png, 203 × 404 px.

- Retrato colorido original de Enzo, proporção intacta. A única extração limpa disponível tem 201 × 242 px, equivalente ao retângulo [421,28,622,270] do mockup. Não recuperar ou gerar corpo oculto. Exibir proporcionalmente e dissolver a borda inferior sobre preto. O fundo completo depende do original.
- Barra de status: hora 9:41, sinal, Wi-Fi e bateria brancos. Área simulada no navegador, ocultável na integração via data-native-status.
- Cinco segmentos: margem lateral aproximada 7% da largura, topo 5,8% da altura. Espessura aproximada 1,5 px no mockup (2 px na renderização).
- Controles voltar/opções com alvo >=44 px; topo abaixo dos segmentos. O painel 03 pequeno não mostra seus traços com clareza, mas o handoff os exige.
- Nome: Enzo, 26 com selo azul; cerca de 68% da altura, margem esquerda 7% da largura. Arial/sans-serif local como aproximação, pois não há fonte original.
- Localização exata: São Paulo, SP · 1,84 m. Categorias Fashion, Editorial, Comercial, borda cinza e fundo transparente.
- Três botões circulares, 21% da largura (limite 86 px), centros em aproximadamente 25%, 50%, 75%. Faixa inferior; coração vermelho, demais transparentes com borda cinza. Respeitar safe areas.
- Barra de gesto branca: base 8–10 px, largura 32%.
- Viewports de aceite: 375×812, 390×844, 430×932, DPR 1, sem overflow. Alvos de toque >=44 px, foco visível, SVGs independentes, redução de movimento.
- Favoritar/curtir: alternância acessível via aria-pressed. Ignorar: retira o único perfil em memória e oferece desfazer em um painel; não inventa outro modelo. Voltar, informações e opções: painéis locais explícitos, sem backend nem navegação à Tela 04.
- Não aprovar por inspeção do código. Evidências reais, comparação e rubrica obrigatórias. Meta >=9,0; limitações fotográficas não devem ser ocultadas pela nota.

## Ciclo 2
A área superior do céu usa um recorte sem interface [421,14,622,22] do mesmo mockup, expandido apenas no céu. A máscara do retrato faz a transição com esse céu e o fundo preto; o rosto e os ombros mantêm proporção natural. Não se recupera a parte inferior ausente.

## Ciclo3
A faixa de céu ampliada produziu banding; substituída por interpolação CSS das cinco amostras RGB da primeira linha do retrato (x0/50/100/150/200). Não há pessoa, corpo ou fotografia gerada. O recorte de céu permanece como evidência de origem, mas não é usado no runtime final.

## Ciclo7 — escopo da camada tipográfica
ForegroundsPNGseparados e decorativos, sem fundo retangular; namebox(11,272,66,21), locationbox(11,292,108,16), escalaaltura/404 e offset dafotografia. NativeH1/Pmantidos acessíveis e como fallback atômico para ambos oslabels. Somente textos fixos da referência são compatíveis; recusar visualraster noopt-out, erro deasset ou divergência textual. Manifesto documenta franja deantialiascontextual1px; não se trata deoriginalfontou restauração dafotografia.
