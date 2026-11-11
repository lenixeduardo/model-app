# Assets11 — handoff

Original1179×753 e referência184×317 abertos visualmente. Fonte: `../MODEL_assets_v1/originais/mockup-geral.jpg`; recorte global[805,434,989,751], direita/base exclusivas. Pillow confirma diferença RGB bbox=None contra `11-notificacoes.png`. Nenhum asset foi importado das telas03–10.

Cinco PNG RGBA independentes, próprios desta tela, todos28×28 e razão1:1:

|Arquivo|Linha|BBox local|BBox global|
|---|---|---|---|
|avatar-01.png|Nova mensagem|12,75,40,103|817,509,845,537|
|avatar-02.png|Campanha Inverno2025|12,110,40,138|817,544,845,572|
|avatar-03.png|Perfil salvo|12,145,40,173|817,579,845,607|
|avatar-05.png|Matheus curtiu|12,216,40,244|817,650,845,678|
|avatar-06.png|Portfólio visualizado|12,251,40,279|817,685,845,713|

Frames incluem disco fotográfico completo≈25–26px com pequena margem/matte JPEG genuína. Máscara binária: centro[13.5,13.5], raio13.7 no PNG; alpha255 dentro,0 fora. RGB transparente zerado; todo pixel visível coincide exatamente com o original. Sem interpolação, remoção de fundo interna, suavização facial, inpaint, criação de rosto ou partes. Preview ampliado dos cinco aberto para conferir cabelo/rosto/ombros. Identidades visuais não autorizam vincular avatares de outras telas. Não há UI aparentemente sobreposta nas fotos, nem reconstrução sob pixels indisponíveis. Detalhes fora do disco ou além da resolução original permanecem indisponíveis.

Implementar imagem com largura fluida e altura proporcional, sem cover/zoom. O suporte28px inclui matte: para manter o disco aparente≈25px na referência, usar largura28/184 da viewport, com posição esquerda12/184. Centros verticais são88.5/123.5/158.5/229.5/264.5. Não aplicar segundo crop circular mais estreito. A tolerância do limite é≈1px por JPEG; fotografias seguem naturalmente pixeladas quando ampliadas.

Dez SVGs locais novos: `plus-circle`, `home`, `search`, `plus`, `chat`, `profile`, `cellular`, `wifi`, `battery`, `casting`. Cada um independente, viewBox24×24; perfil preenchido ativo, outros destinos outline cinza, mais superior preto. São aproximações vetoriais declaradas da miniatura, sem correspondência pixel a pixel, sem bibliotecas ou reutilização. Símbolo casting é traçado fino abstrato aproximado, sem letra ou logomarca inventada; desenho exato não é recuperável no JPEG. Coral sólido#BD6C4F é amostra direta[19,187],RGB189,108,79; variação original quente do disco não é recuperada por esse vetor. Não confundir arquivo casting com fotografia.

Amostras exatas (demais no manifest): papel[45,280]=249,248,243; pill inativo[145,52]=240,239,235; preto[165,26]=11,11,11. RGB de amostra não representa cor uniforme de toda superfície JPEG. Título, hora, seis mensagens, tempos e quatro filtros devem permanecer HTML nativo; nenhuma tela integral ou texto raster foi entregue.

Reprodução: `python MODEL_tela_11_V1/assets/extract_assets.py` a partir da raiz (Pillow). Script verifica crop fonte, prova igualdade de todos pixels RGB visíveis, gera PNGs/SVGs e `assets/manifest.json`. Manifest registra hashes SHA256 fonte/ref/script/15assets, coordenadas, máscara, contagens alpha, amostras e proveniência. Execução concluída com todos asserts passando. Não constitui teste de renderização SVG em navegador, captura do app ou auditoria visual de implementação.

Assets11 concluído; implementador11 liberado.03–10 preservadas. Nenhum HTML/CSS/JS de interface, captura, nota ou publicação neste papel.
