# Assets10 — Matheus Silva

Entrega exclusiva de assets, sem interface, captura de app ou nota. Referência10 e original geral abertos visualmente. `assets/extract_assets.py` confirma igualdade RGB do crop global[612,434,797,751] com referência185×317 e gera novamente foto, SVGs e manifest. Executar `python MODEL_tela_10_V1/assets/extract_assets.py` a partir da raiz model-app; requer Pillow.

## Fotografia e máscara

`assets/matheus-avatar.png`:77×77 RGBA, razão1:1, recorte local[53,39,130,116], global[665,473,742,550]. Identidade exclusivamente da tela10, Matheus Silva24. Nenhuma foto de Enzo/Rafael foi reutilizada. Círculo de centro[38.5,38.5], raio38.5 no crop; máscara por centro do pixel, alpha binário. Conservar o círculo integral em proporção; altura automática, sem object-fit:cover ou estiramento. Borda contém antialias/matte do JPEG original; não recolorida. A foto não recupera detalhe ao ampliar.

Editar ocupa o círculo de centro[64.5,64], raio12.5 no crop, equivalente a[117.5,103] local/[729.5,537] global. Todo pixel nessa área indisponível recebe alpha0/RGB0, assim como exterior.4386 pixels visíveis preservam exatamente RGB fonte;283 pixels dentro do círculo fotográfico são removidos pelo footprint de UI. Sem inpaint, anatomia gerada ou foto sob o suporte. Máscara/crop/hash/dimensões constam no manifest; o script verifica cada pixel visível. O avatar ampliado com alpha foi aberto para inspeção.

`edit-overlay.svg` usa o MESMO viewBox77×77, centro[64.5,64], suporte opaco #f8f7f3 de raio13.5 e lápis preto. A margem geométrica de1px cobre o buraco integralmente; não contém foto embutida. Sobrepor absoluto inset0, largura/altura100% do avatar; o suporte permanece em todos estados, incluindo dialog, erro de ícone e edição. Clipping conjunto opcional na borda circular: nunca clipar foto e suporte com transforms diferentes. A área de toque44px deve envolver o desenho como hitbox transparente, sem aumentar separadamente seu desenho ou raspar o frame. `edit.svg` é versão standalone, mas `edit-overlay.svg` é a versão recomendada para co-registro exato. Renderização SVG isolada não foi executada: CairoSVG indisponível; verificar no navegador durante implementação.

## Vetores e cores

Status celular/Wi-Fi/bateria, search/chat/plus/location reutilizados de07 sem alteração por adequação visual; caminhos e hashes iguais registrados. Os demais SVGs são aproximações novas de10: back/chevron, home contorno, perfil ativo preenchido, selo PRETO com check BRANCO, editar, portfólio/disponibilidade/cachê/estatísticas/planos. Não reutilizar home preenchido ativo07 nem selo azul03. Todos locais, sem textos rasterizados ou fontes externas. Os cinco menus e cinco itens nav continuam elementos nativos da implementação; nenhum sexto item/bio é fornecido.

Papel #f8f7f3, chips #efeeea, primário #111111; secundário aproximado #70706c. Papel/chips baseados nas amostras fonte documentadas no DESIGN_SPEC; não há identificação forense de fonte. Textos serão Arial/Helvetica nativos. SVGs currentColor requerem cor explícita do elemento/contexto; em img externo currentColor tende a preto, portanto opacidade/cor secundária deve vir do contêiner ou variante local, sem filtros na fotografia.

## Handoff

Manifest inclui hashes SHA256 de todos os21 arquivos de produção/extração, hashes das duas fontes, proveniência dos sete reusos e limitações. Script reproduzível gerou os assets e confirmou igualdade fonte/RGB.03–09 preservadas. Implementador10 liberado;11 aguarda gate10 próprio>9,0. Nenhuma nota ou publicação atribuída neste papel.
