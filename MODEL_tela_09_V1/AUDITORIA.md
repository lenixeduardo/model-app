# Auditoria independente09 — Salvos

**APROVADA VISUALMENTE: 9,27/10**, soma ponderada **9,265**. Versão congelada `1.0.0-prototipo.1`. Gate estrito >9,0 atendido, meta9,5 não atingida. Nenhum P1 material identificado no estado inicial e domínio375–430 das evidências. Auditor09 concluído; **planejador10 LIBERADO**. A decisão decorre da inspeção visual independente abaixo, não de asserts ou aprovação do implementador.

## Imagens efetivamente abertas

Abri via view_image a referência oficial `MODEL_assets_v1/referencias/09-salvos.png` (176×317), `CAPtura-375.png` (375×812), `CAPtura-390.png` (390×844), `CAPtura-430.png` (430×932) e `comparacao-390.png` (859×874). A capitalização real dos arquivos é **CAPtura**, não captura nem CAPturas/. Nenhum arquivo foi renomeado. A comparação usa referência469×844 e captura390×844, abaixo de cabeçalho30px; proporções individuais conservadas, sem esticar a referência para390. Conferência Pillow independente: região[469,30,859,874] é pixel a pixel idêntica à captura390.

## Rubrica visual

| Critério | Peso | Nota | Parcela | Fundamentação visual |
|---|---:|---:|---:|---|
| Fotografia, identidade, enquadramento |35%|9,70|3,395|Quatro retratos e enquadramentos originais preservados, inclusive ombros e bordas; resolução baixa fonte assumida. Controle opaco substitui parte encoberta, sem anatomia inventada.|
| Geometria |25%|8,80|2,200|Grid, âncoras, tabs e navbar corretos. Espaço entre fotos e nomes maior que a fonte, sobretudo na primeira linha.|
| Tipografia e ícones |20%|9,00|1,800|Hierarquia, nomes/cidades e seleção reproduzidos em texto nativo; Arial e pequenos vetores não igualam completamente desenho/peso da referência.|
| Cores, contraste, sobreposição |10%|8,80|0,880|Papel e preto coerentes; círculos de bookmark mais escuros/opacos e visualmente mais dominantes.|
| Responsividade e acabamento |10%|9,90|0,990|Três capturas mantêm quatro cards e nav inteiros sem overflow; fotos sem zoom, alongamento ou mudança de pessoa.|

Soma:3,395+2,200+1,800+0,880+0,990=**9,265**, arredondamento9,27. Nenhuma parcela foi dada automaticamente pelos testes.

Enzo26/São Paulo, SP; Gabriel28/Rio de Janeiro, RJ; Rafael29/São Paulo, SP; Theo24/Belo Horizonte, MG correspondem à fonte. Modelos está ativo, Castings cinza; header Salvos e cinco ícones casa/busca/mais/chat/perfil presentes. A roupa efetiva de Gabriel é a da fotografia original, conforme correção factual em ASSETS.md. UI no papel é HTML nativo; não há tela inteira como fundo raster.

## Verificação independente dos arquivos

Li DESIGN_SPEC.md, PLANO.md, ASSETS.md, README.md, EVIDENCIAS.json (equivalente do relatório-browser), FALLBACK.json, SHA256SUMS e implementação/scripts de verificação. Executei `sha256sum -c SHA256SUMS`:10/10 OK. Pillow confirmou referência RGB idêntica ao crop global[428,434,604,751] do JPEG. Fotos superiores74×63 e inferiores74×65:4366/4366/4514/4514 pixels visíveis, todos RGB iguais à fonte, nenhuma diferença; alpha oculto documentado. Não se afirma recuperação dos pixels sob UI.

Regressão07 verificada nos12 registros (4×3): diferença absoluta máxima entre ratio renderizado e intrínseco0,000108, compatível com arredondamento subpixel. CSS width100%/height auto e capturas corroboram frame integral, sem object-fit cover divergente. 100% do frame retangular original é apresentado proporcionalmente, exceto máscara de cantos/UI já declarada; não significa100% de pixels fotográficos recuperados sob bookmark.

O controle usa SVG próprio saved/unsaved, círculo opaco raio9,75 sobre máscara9,5, posição e escala relativas à foto pelo container. Foto e controle compartilham clipping; visualmente nenhuma lacuna/seam exposta nas três capturas. Alvo44px fica no canto inferior dentro do frame e separado da faixa de preview, que termina44px antes da base. O desenho excede parcialmente o frame por projeto e é recortado, sem reduzir o botão44×44. Preview usa mesma geometria. Máscara é aproximada, não segmentação anatômica exata; isso integra os limites de fidelidade abaixo.

## Evidência de comportamento revisada

EVIDENCIAS.json registra Chromium156.0.8078.79/DPR1, errors=[], networkFailures=[], responses=[], carregamento completo e overflow=false nos três tamanhos. Todos alvos listados têm mínimo44px. Script verifica saves individuais sem abrir preview, desfazer, reload restaurando4, tabs e teclado, previews das4 identidades, Escape/restauração de foco, dialogs locais e navegação real03/07/06/04. Código restringe perfil04 a Enzo; outros previews informam indisponibilidade. Estado é memória local, sem backend ou persistência alegada. Texto usa textContent; fonte local de sistema Arial/Helvetica, sem download.

FALLBACK.json registra foto indisponível com identidade, SVG alternativo carregado, foco dentro do dialog e restaurado; script revisado usa falhas deliberadas. Reduced-motion registrado e CSS sem animações relevantes. Dialog nativo showModal fornece contenção e Escape. São evidências do implementador revisadas, **não uma segunda execução independente de browser pelo auditor**. O auditor executou somente conferências locais de hashes/RGB/dimensões/colagem, e abriu as imagens finais. Não se afirma auditoria completa de leitor de tela, todos navegadores ou dispositivos físicos.

## P2 e limites aceitos

- Na390, foto superior y≈192–331 e nome y≈380: cerca49px de intervalo; na referência o intervalo é muito menor. Inferiores y≈447–591 e nome≈643 têm efeito parecido. Âncoras verticais por altura e fotos naturais por largura explicam a redistribuição, prevista no contrato. O resultado conserva anatomia e legibilidade, mas reduz compacidade visual.
- Bookmarks na390 têm desenho≈44px e círculos opacos por foto mais escuros que os pequenos controles translúcidos da fonte. Não vazam máscara, mas são dominantes (centros aproximados171/348,y311 e573); refinamento futuro exige preservar cobertura dos pixels não disponíveis. Nenhum preenchimento de pele/roupa/céu autorizado.
- Hora/status, pictograma superior, nav e Arial diferem no traço/peso da fonte. A comparação à mesma altura também evidencia escala horizontal menor do viewport estreito. Não é distorção dos frames.
- JPEG pequeno74×63/65, matte e máscara aproximada limitam nitidez/cantos. Círculo opaco é substituição honesta da UI, não fotografia reconstruída. Sem dados remotos, perfil completo para três modelos, sincronização, backend ou validação de produção. Alturas fora das três evidências, safe areas de aparelhos reais e zoom tipográfico exigem validação adicional.

## Hashes das imagens avaliadas

```text
2ef31f40f70ae50d3f5317ea79d9162e57d547cbdde5cdf46c3ceebc1966c508  MODEL_assets_v1/referencias/09-salvos.png
e1809aa2a2b5b56f96196677dde033ccdd4bf85227a964c23526dec9ccd3884d  CAPtura-375.png
578cf21dcd71464050d49f072d69b8462b063cab46dbdc07a22e0d729a4a8ad4  CAPtura-390.png
d35863cd90463ea07da15bc7d8ae31e002d4e7ae768af4d44939cf90fd2588f7  CAPtura-430.png
6829b22fdc024089446b4179125105e7f6809572562eae4bed6edd98d014ee13  comparacao-390.png
cff7c0c33eeaa0a033386e87799c377a21d9218c547371ca8dd3751eb27b056c  EVIDENCIAS.json
6b231fd289a5a7df905372869921173c2aaa86a3532d9b6c4539d6845e07f6f9  FALLBACK.json
```

Somente AUDITORIA.md e fila alteradas nesta auditoria.03–08 preservadas (08=9,23); código/assets/capturas09 intactos. Nenhuma publicação ou início10 realizado. Aprovação09 libera somente o próximo papel sequencial, planejador10;11 depende do gate próprio10.
