# Tela10 — plano executável V1

Autorizado após gate09 aprovado9,27/10. Contrato em [DESIGN_SPEC.md](DESIGN_SPEC.md). Preservar03–09;11 aguarda gate10. Este papel entrega somente planejamento e atualização da fila, sem assets, interface, capturas, nota ou publicação.

## 1 — Assets10

- Reabrir fonte185×317 e original1179×753; confirmar crop[612,434,797,751] RGB idêntico e hashes.
- Refinar um retrato circular de Matheus Silva da10, frame integral. Inventariar dimensões, ratio, box global/local e pixels encobertos pelo editar. Não extrair outra pessoa nem usar fotografia de outra tela.
- Extrair RGB genuíno com alpha geométrico exterior e footprint exato de UI; suporte opaco independente cobre lacuna permanentemente. Documentar matte, cobertura e limites sem inpaint. Provar RGB de pixels visíveis e proporção; insuficiência bloqueia, não autoriza substituto.
- SVGs locais de status/header/editar/selo/pin/menus/chevrons/nav, como aproximações declaradas. Texto fica HTML; não produzir raster de legendas. Colher cores e registrar origem de qualquer SVG reutilizado por hash.
- Entregar ASSETS.md, manifest, extração reproduzível e assets independentes utilizáveis. Não iniciar implementação sem esse handoff; sem nota.

## 2 — Implementador10

- Entregar HTML/CSS/JS separados, VERSION, README, CHANGELOG e verificação reproduzível; não editar aprovadas03–09 e não criar11.
- Construir hierarquia exata: status/back/Meu Perfil, avatar+editar, Matheus Silva24+selo preto/local, três tags, três medidas, **cinco** menus fonte e navbar5. Não há bio ou sexto menu na referência. Textos nativos Arial/Helvetica; foto integral sem deformação e sem UI embutida.
- Edit/dialogs somente em memória, cancelar/reload seguros; portfólio de Matheus sem atribuir fotos de Enzo. Disponibilidade/cachê/estatísticas/planos não inventam estado remoto, números, preços ou pagamento. Navegação03/06/07 e retorno09 verificáveis;08 apenas contexto rotulado quando pertinente. Mais/perfil ações locais honestas.
- Verificar 44px sem overlap, foco/aria-current/labels/dialog/Escape/restauração/reduced-motion/fallback, texto seguro, ausência de rede externa/overflow/erros. Conferir que suporte de editar não revela lacuna em qualquer estado. Geometria significativa:100% do frame circular fonte preservado e ratio intrínseco nos três tamanhos.

## 3 — Evidências finais

- Servir local e usar navegador real DPR1; abrir candidata390 e corrigir antes das finais. Documentar comandos e versão.
- Capturas default375×812,390×844,430×932. Abrir todas; comparação390/ref à altura844, proporções individuais preservadas. Não usar captura do editor como prova do app.
- Relatório técnico e hashes ligados à mesma versão, cobrindo ações/menus/edit/back/nav, teclado/foco/Escape/44px/falhas/console/rede/overflow/proporção. Capturas de dialogs separadas das finais default. Implementador não atribui nota.

## 4 — Auditor independente10

- Abrir fonte, três capturas e comparação; conferir identidade exclusiva da10, frame, RGB/máscaras/cobertura, texto, cinco menus e cinco nav, versão/hashes.
- Revisar testes distinguindo revisão de execução própria. Aplicar35foto/25geo/20tipoícones/10cores/10responsivo e documentar diferenças P1/P2. Gate>9,0, meta9,5, sem elevar nota para avançar.
- Falha corrigível volta ao papel responsável com nova versão/capturas/reauditoria. Insumo impossível gera bloqueio com prova e condição objetiva de retomada;11 segue aguardando.
- Entregar AUDITORIA.md e atualizar fila; apenas aprovação10 libera planejador11. Publicação autorizada do pacote completo cabe ao coordenador, sem declaração antecipada.

**Handoff:** planejador10 concluído; próximo papel **assets10 LIBERADO**.11 aguarda gate10 próprio;03–09 preservadas.
