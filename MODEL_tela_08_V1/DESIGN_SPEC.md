# Tela08 — Filtros — contrato visual V1

Planejamento de2026-11-11 (America/Sao_Paulo). Gate07 aprovado9,32/10, versão1.0.0-prototipo.2; preservar03–07. Fontes abertas com view_image: `MODEL_assets_v1/referencias/08-filtros.png`200×317 e `MODEL_assets_v1/originais/mockup-geral.jpg`1179×753. Crop global **[220,434,420,751]**, direita/inferior exclusivas, confirmado RGB idêntico por Pillow ImageChops, bbox=None. Coordenadas abaixo são locais à referência e aproximadas pela resolução disponível. Próximo papel: assets08.09–11 aguardam seus gates.

## Geometria e conteúdo exato

| Região | Box/âncora local aproximada | Conteúdo/estado inicial |
|---|---|---|
| Papel | [0,0,200,317], cantos≈12 | Branco quente; sem moldura adicional |
| Status | hora[17,6,30,13], sinais[157,7,186,13] | **9:41**, celular, Wi-Fi e bateria pretos |
| Header | seta centro[17,27], título centro[96,27], ação x163,y27 | **Filtros** bold; **Limpar** cinza; voltar contorno fino |
| Localização | título[14,45], campos y56–74 | **Localização**; campo[14,56,127,74] com lupa/localização pequena e **São Paulo, SP**; seletor[134,56,186,74] **50 km** e chevron |
| Idade | título[14,88], valor alinhado à direita x185,y91 | **Idade**; **18 - 35 anos**; trilho[14,102,186,105], segmento preto até thumb centro[49,104], círculo≈12px |
| Altura | título[14,120], valor direito x185,y123 | **Altura**; **1,70 m - 1,95 m**; trilho[14,134,186,137], segmento preto até thumb centro[61,136], círculo≈12px |
| Cachê | título[14,152], valor direito x185,y155 | **Cachê (por dia)**; **R$ 300 - R$ 5.000**; trilho[14,165,186,169], segmento preto até thumb centro[91,167], círculo≈12px |
| Categorias | título[14,179] | **Categorias** |
| Chips linha1 | y190–207, x14–55/59–97/101–145/149–188 | **Fashion** ativo preto/branco; **Fitness**, **Comercial**, **Editorial** claros |
| Chips linha2 | y209–225, x14–55/59–99 | **Lifestyle**, **Passarela**, claros |
| Disponibilidade | título[14,234] | **Disponibilidade** |
| Opções | y247–265, x14–59/63–139/143–184 | **Imediata** ativa preto/branco; **Próximas semanas**; **Flexível** claras |
| CTA | [14,278,188,302], raio≈11 | **Aplicar filtros** branco central, fundo preto |

Não há fotos, tabbar, contador ou rótulo de demonstração visível no estado inicial. Nenhuma marca, texto extra ou imagem de interface como fundo. Campos/títulos/chips/valores devem ser texto nativo Arial/Helvetica/sans-serif. Referência: título≈10px bold; labels≈7px bold; valores/campo/chips≈6–6,5px; CTA≈7px. Fonte final proporcional à largura, respeitando hierarquia e sem fontes remotas. Cor principal≈#101010, papel≈#faf9f5, chips/campos≈#efeeeb, trilho≈#d9d8d4, secundário≈#777570; colher amostras do original no papel de assets, registrar aproximações JPEG. Evitar sombras decorativas; thumb branco com borda cinza e sombra mínima compatível com fonte.

## Contrato de controles locais

A fonte revela os valores iniciais e um thumb por faixa; não revela limites externos, opções ocultas ou comportamento. As regras abaixo são decisões funcionais locais, não conteúdo inferido do mockup. Manter a aparência inicial dos três thumbs nas âncoras acima. Usar controles acessíveis de faixa com seleção de intervalo; representação visual inicial de um thumb conforme fonte. O valor textual de cada faixa é um botão discreto sem decoração extra que abre dialog para editar **ambos os limites**, com labels explícitos nesse dialog. Não desenhar um segundo thumb ausente da referência. O thumb visível ajusta o limite inferior; o limite superior é editável pelo dialog. Usar aria-valuetext para anunciar o intervalo completo e explicar o ajuste no nome/descrição acessível. O domínio local do slider pode ser o intervalo entre mínimo e máximo selecionados, mas sua posição deve ser recalculada coerentemente após edição; não usar geometria inicial como desculpa para valor anunciado falso. Se necessário, implementar slider de intervalo com thumb único que desloca a faixa inteira, documentando a decisão no README e mantendo edição precisa dos extremos no dialog.

- Estado inicial em memória: cidade `São Paulo, SP`, distância50km; idade[18,35], altura[1.70,1.95]m, cachê[300,5000]R$/dia; categorias somenteFashion; disponibilidadeImediata. Reload restaura esses valores. Não usar localStorage, cookies, backend, geolocalização ou API simulada.
- Localização é input editável, não busca remota. Distância é seletor acessível com valores locais10/25/50/100km, inicialmente50. Não inventar sugestões de cidades ou resultados reais. Fechar seletor com Escape, mantendo foco.
- Faixas aceitam edição numérica dos dois extremos no dialog: idade inteira18–100, altura1,00–2,50m em0,01, cachê0–100000 em50. Esses limites são validação técnica local, não informação da referência; não aparecem no estado inicial. Validar mínimo≤máximo com erro textual acessível no dialog, sem trocar silenciosamente números. Formatação pt-BR exata no estado inicial.
- Categorias são multisseleção independente, aria-pressed; os seis rótulos são os da tabela. Disponibilidade é seleção exclusiva entre as três opções visíveis, com semântica de grupo/radio. Mudanças afetam somente esta tela e seu resumo local.
- **Limpar** restaura o estado inicial completo acima, inclusiveFashion/Imediata e cidade/distância; não interpretar como campos vazios sem referência. Deve funcionar após qualquer edição.
- **Aplicar filtros** abre dialog acessível com resumo dos valores atuais e aviso de aplicação somente nesta demonstração local, sem afirmar que os castings foram filtrados. Fechar mantém valores. Pode oferecer retorno explícito à07 aprovada em `../MODEL_tela_07_V1/index.html`; o voltar do header navega para esse mesmo destino. Não alterar07, seus arquivos, runtime ou filtros, nem passar estado fingindo integração.
- Alvos44×44px CSS, sem sobreposição; ampliar área interativa sem ampliar o desenho dos chips/ícones indevidamente. Foco visível, teclado/setas para sliders, labels vinculados, valores e erros anunciados. Dialog com título, fechar, Escape, foco contido/restaurado; reduced-motion. Texto de usuário via textContent, sem HTML injetado.

## Assets e adaptação

Sem fotografia nem labels PNG. Assets08 entrega SVGs locais de voltar, ícone pequeno do campo (lupa conforme desenho aparente; registrar incerteza), chevron e status celular/Wi-Fi/bateria, com proveniência e hashes; reutilização por hash de assets aprovados é permitida, sem modificar originais. UI nativa para trilhos, thumbs e chips. Sem glifos Unicode/emoji como substituto.

Usar composição fluida: x porW/200 e y porH/317 como âncoras iniciais, sem transformar texto por scaleX/scaleY. Preservar duas linhas de categorias e uma de disponibilidade, todos controles e CTA visíveis sem overflow no estado inicial em375×812,390×844,430×932. A altura maior que a proporção fonte é distribuída nos espaços verticais, mantendo hierarquia. Exemplos de topoCTA y278:712/740/817; centroheader y27:69/72/79. Insets horizontais14:26/27/30. Safe areas incluídas sem cortar CTA. Na390, a fonte visual aproximada do título é19,5px; labels13,7px, texto comum12–13px; ajustar pela comparação real. Dialogs podem rolar internamente se necessário, sem overflow lateral.

## Evidências e rubrica08

Três screenshots reais375×812,390×844,430×932,DPR1; procedimento/navegador/versão/hashes documentados. Comparação390 e referência à mesma altura, proporções preservadas. Abrir capturas e comparação. Registrar console/rede/ausência de assets/overflow default, edição dos campos/faixas, validação, chips, disponibilidade, reset, aplicar, voltar07, teclado/foco/Escape/44px e reduced-motion.

**Fotografia/identidade/enquadramento: N/A**, porque não há fotografia. Não atribuir10 gratuito nem alterar notas anteriores. Normalizar os65% restantes: nota08=(25×geometria+20×tipografia/ícones/chips+10×cores/contraste+10×responsividade/acabamento)/65. Pesos equivalentes38,4615%/30,7692%/15,3846%/15,3846%. Auditor independente documenta essa adaptação honesta, diferenças concretas e bloqueadores. Gate**>9,0**, meta9,5, nenhum P1 material. Só aprovação08 libera planejador09.
