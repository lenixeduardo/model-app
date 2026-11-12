**Integração em andamento:** o runtime desta pasta foi alterado após a auditoria visual histórica. `AUDITORIA.md`, capturas antigas e seus manifests descrevem a versão pré-integração, recuperável no commit `b49b77d`; não certificam os arquivos atuais. Novas evidências e aceite final permanecem pendentes. Ver [estado da integração](../docs/correcoes-123/AVALIACAO_ATUAL.md).

**Estado vigente: APROVADA VISUALMENTE — 9,23/10**, versão 1.0.0-prototipo.1. Auditoria independente e hashes em AUDITORIA.md / EVIDENCIAS_RELEASE.json. Gate >9,0 atingido; a aprovação não certifica backend ou dispositivo físico.

# Tela08 — Filtros

Versão 1.0.0-prototipo.1. Implementação HTML/CSS/JS nativa, sem backend, persistência, fontes remotas ou fotografias. Originais e pacotes03–07 preservados. Fotografia N/A; auditoria independente concluída em9,23/10 com critérios aplicáveis normalizados.

Servir **a raiz do repositório**: `python -m http.server 8000`, abrir `/MODEL_tela_08_V1/index.html`. Executar `python MODEL_tela_08_V1/tests/test_browser.py` e `python MODEL_tela_08_V1/tests/verify.py`. Python Playwright, Pillow e `/usr/bin/chromium` são utilizados. Teste inicial registrou falha real por index.html ausente antes da implementação.

Os valores e opções iniciais seguem DESIGN_SPEC. Limpar restaura todos os valores da fonte. Cidade é campo local livre; distância oferece10/25/50/100km. Categorias independentes e disponibilidade exclusiva. Aplicar apresenta somente resumo local e link explícito à07, sem alegar busca remota.

Cada faixa tem um thumb nativo que modifica o limite inferior e botão de valores para editar ambos os extremos em dialog. Domínios visuais locais: idade0–88, altura1,30–2,86 e cachê0–670, estendidos quando necessário para incluir valores editados; não representam domínio de mercado. A posição é calculada a partir do valor nativo e do domínio, nunca um thumb decorativo desconectado. O input é limitado ao intervalo selecionado e ao mínimo técnico ao interagir. Dialogs validam idade18–100, altura1–2,50, cachê0–100000/50, e rejeitam inferior>superior. Domínio técnico oculto e domínio visual são decisões locais para preservar o único thumb e as âncoras da fonte. Os valores anunciados via aria-valuetext são os intervalos completos.

Alvos44px, foco visível, dialogs nativos com Escape e retorno de foco, teclado/setas nas faixas e nas opções de disponibilidade. Trilhos têm desenho deslocado dentro dos alvos para separar botão de edição e área de faixa. Texto secundário #777570 foi escurecido frente à estimativa antialias #9d9c9a. SVGs externos locais conservam preto (currentColor em documento externo); localização usa lupa. UI e textos não são imagens.

Evidências: `relatorio-browser.json` contém versão do Chromium, dimensões/DPR1, entradas nativas, alvos, fluxos, console/rede e SHA256. Capturas sem foco ou dialog: `screenshots/captura-{375,390,430}.png`. `comparacao-390.png` redimensiona a referência para844px de altura preservando proporções e mantém a captura390×844 sem distorção. Candidata390 foi aberta e comparada antes do congelamento; três finais e comparação foram inspecionadas. Baixa resolução JPEG e proporções de viewport distintas limitam comparação pixel a pixel. A pontuação9,23/10 foi atribuída pelo auditor independente, após abrir as capturas reais.

As capturas captura-375.png / captura-390.png / captura-430.png são os raw finais ou cópias idênticas dos raw em screenshots/, sem edição. Candidatos e versões anteriores são históricos, não prova da versão aprovada.


## Integração

Navegação integrada à demonstração local. Dados e ações permanecem locais; não há backend.
