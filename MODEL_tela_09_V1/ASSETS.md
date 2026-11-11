# Assets09 — Salvos

Assets entregues para implementação, sem nota visual. Fonte única: `MODEL_assets_v1/originais/mockup-geral.jpg` (1179×753). Referência `MODEL_assets_v1/referencias/09-salvos.png` (176×317), crop global `[428,434,604,751]`, confirmado RGB idêntico por Pillow ImageChops. Referência e original abertos visualmente; referência também inspecionada ampliada. Hashes SHA256 completos no `assets/manifest.json`.

## Fotografias originais independentes

Boxes direita/inferior exclusivos, coordenadas locais da referência; global = local + [428,434]. Nenhuma foto reutilizada de outra tela, sintetizada ou completada. Gabriel usa a roupa efetivamente visível no original (regata/camiseta cinza sem mangas); a frase “camisa clara aberta” no planejamento é imprecisa e não autoriza trocar retrato.

| Arquivo | Identidade nativa | Cidade nativa | Box local | Dimensões | Centro controle relativo à foto |
|---|---|---|---|---|---|
| enzo.png | Enzo, 26 | São Paulo, SP | [12,72,86,135] | 74×63 | [65,54] |
| gabriel.png | Gabriel, 28 | Rio de Janeiro, RJ | [92,72,166,135] | 74×63 | [65,54] |
| rafael.png | Rafael, 29 | São Paulo, SP | [12,168,86,233] | 74×65 | [65,56] |
| theo.png | Theo, 24 | Belo Horizonte, MG | [92,168,166,233] | 74×65 | [65,56] |

Fotografias RGBA. Cada pixel de alpha>0 conserva exatamente RGB do JPEG fonte. Todo pixel alpha=0 tem RGB=(0,0,0). Não há raster de nome/cidade/UI nas fotos. O frame retangular integral é mantido; somente cantos externos e footprint do bookmark são transparentes. Contagens verificadas:4366 pixels visíveis por foto superior e4514 por inferior;296 ocultos por foto, incluindo cantos. Não inferir pixels sob a UI.

**Renderização obrigatória:** largura fluida, altura intrínseca (`width:100%;height:auto`); ratios74/63 e74/65. Em largura164px, alturas139,62px/144,05px. Não fixar altura por viewport e não usar `object-fit:cover` em caixa com razão divergente. A foto integral deve ficar presente nos três tamanhos. Resolução fonte pequena: ampliar proporcionalmente conserva composição, não cria detalhes.

## Máscara e controle independente

Máscara binária reproduzível: avaliar centro do pixel (x+.5,y+.5); remover disco de raio9,5 centrado conforme tabela e pixels fora do retângulo arredondado de raio5. Bbox do disco relativo: superiores[55.5,44.5,74.5,63.5], inferiores[55.5,46.5,74.5,65.5]; interseção com frame. Geometria aproximada ±1px fonte; não é segmentação anatômica. Matte/JPEG de borda pode persistir. Nenhum RGB opaco foi ajustado.

Oito SVGs `bookmark-{identidade}-{saved|unsaved}.svg`: viewBox[-10,-10,20,20], círculo **opaco** raio9,75, glifo branco preenchido/somente contorno. Cor opaca por foto vem da mediana de amostras no arco esquerdo do controle original; manifest registra RGB/hex. Essa aproximação substitui a transparência original, pois não há foto limpa sob o overlay. Não é possível restaurar pele/roupa verdadeira daquela área a partir deste insumo.

Co-registrar SVG20×20 unidades fonte, centro exato da tabela, escala igual à foto. Círculo opaco9,75 cobre o disco removido9,5 nos dois estados: margem radial0,25px fonte. **Recortar foto e controle juntos pelos mesmos cantos originais**; o SVG avança além da direita/inferior de propósito e deve ser clipped. Reservar alvo interativo44px independentemente do desenho; não ampliar a figura para44px. Em preview repetem-se escala/centro/cobertura; não mostrar PNG com a lacuna descoberta. Se remover card inteiro, nenhum buraco é apresentado. Na alternativa desmarcada, manter círculo e trocar somente glifo. Não usar `opacity` no botão/círculo: revelaria alpha vazio. Fallback de SVG deve conservar um círculo opaco com geometria equivalente.

## Ícones e texto

Nove ícones independentes: `nav-home.svg`, `search.svg`, `plus.svg`, `chat.svg`, `profile.svg` copiados byte a byte da07; `cellular.svg`, `wifi.svg`, `battery.svg` da06; `options.svg` novo aproximando os quatro braços/pontos pequenos do header. Proveniência/hashes individuais no manifest. Ícones são aproximações vetoriais do original pequeno, não assets oficiais. Cinco ícones nav em ordem casa/busca/mais/chat/perfil, casa preenchida; cores por currentColor. Bookmarks são específicos à09 e não reutilizam bookmark fino da07.

“Salvos”, “Modelos”, “Castings”, hora9:41 e oito labels de nomes/cidades devem ser texto nativo Arial/Helvetica/sans-serif; nenhuma fonte foi fornecida, sem escala horizontal artificial. Nenhuma data ou metadado adicional inferido.

## Cores amostradas

- Papel dominante[5,35,170,44]:#f9f8f4 (795 pixels); faixa inferior:#f8f7f3 (836). Variação JPEG não exige gradiente.
- Tab ativa interior:#0c0c0c (70 pixels).
- Núcleo real de texto secundário em[97,155]:RGB(131,129,130),#838182. Aproximação utilizável; antialias e compressão impedem descobrir a tinta tipográfica exata. Moda do retângulo de texto é papel, não cor do texto; manifest distingue essas amostras.
- Fundos opacos dos quatro controles são amostrados individualmente e constam do manifest; não representam marca.

## Reprodução e verificação

Na raiz `model-app`: `python MODEL_tela_09_V1/assets/extract_assets.py` (Python3/Pillow). O script extrai do JPEG original, valida painel idêntico, RGB visível, gera máscaras/SVGs, copia ícones e registra hashes/boxes/centros/cobertura em ambos estados. Manifest também inventaria hashes de cada PNG/SVG. Script não cria HTML/CSS/JS, capturas, notas ou publicação.

Assets09 concluído; implementador09 liberado.03–08 preservadas,10/11 aguardam gate09. Auditoria independente posterior deve verificar composição real, correspondência dos labels e cobertura dos controles em todos estados; esta entrega verifica geometria dos assets, sem atribuir nota à implementação futura.
