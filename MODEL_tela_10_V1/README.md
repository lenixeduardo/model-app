**Estado vigente: APROVADA VISUALMENTE — 9,28/10**, versão 1.0.0-prototipo.1. Auditoria independente e hashes em AUDITORIA.md / EVIDENCIAS_RELEASE.json. Gate >9,0 atingido; a aprovação não certifica backend ou dispositivo físico.

# Meu Perfil — tela10

Versão `1.0.0-prototipo.1`, 11 de novembro de 2026 (America/Sao_Paulo). HTML/CSS/JS nativos. Retrato genuíno de Matheus Silva,24, três tags, três medidas, cinco menus e navbar5. Dados estáticos da referência; idade não calculada pelo relógio.

Da raiz do repositório: `sh MODEL_tela_10_V1/serve.sh`; abrir `http://127.0.0.1:8099/MODEL_tela_10_V1/`. Servir a raiz preserva navegação para aprovadas03/06/07/09. Nenhum arquivo03–09 foi alterado.Na entrega da implementação,11 aguardava o gate10; seu estado atual consta no README da raiz.

Teste inicial executado antes do HTML: `python MODEL_tela_10_V1/test_initial.py` falhou com “HTML da tela10 ausente”; após implementação passa. `node MODEL_tela_10_V1/candidate.cjs` gera candidata390, aberta antes das finais. `node MODEL_tela_10_V1/verify.cjs` gera finais e EVIDENCIAS.json; `node MODEL_tela_10_V1/verify-extra.cjs` verifica interseções de alvos e teclado. Dependências disponíveis: Playwright, Chromium `/usr/bin/chromium`, Pillow. Executado Chromium156, DPR1; versão completa consta no JSON.

Capturas de repouso foram feitas antes das interações em375×812,390×844,430×932 e todas abertas. Comparação390 aberta: referência redimensionada proporcionalmente para493×844, app390×844 sem esticar. Diferença de largura é intencional: referência185×317 e viewport390×844 têm razões distintas. Avatar sempre escalado apenas pela largura, ratio1:1 e frame circular integral; não se alonga pela altura. Overlay usa o mesmo viewBox77, suporte r13.5 cobre lacuna r12.5; suporte CSS independente permanece se o SVG não aparece. Nenhum pixel de pele inventado. Ver ASSETS.md para prova RGB e matte JPEG.

Executados: cinco menus e Adicionar com Escape/retorno de foco; disponibilidade salva em memória e reset por reload; editar/cancelar/salvar seguro com string HTML via textContent e retirada do selo após edição; reload restaura Matheus; Tab/Shift+Tab contidos no dialog; navegação03/07/06 e fallback09; perfil atual anunciado; reduced-motion; fallback de foto mantendo nome e suporte. Alvos >=44px sem interseções nos três tamanhos. Assets carregados, documento sem overflow e zero erros de console/página/rede nas ações principais. Fallback simula evento de erro, não requisição404 real. Capturas de dialog/fallback são evidências separadas.

Ações são locais e temporárias; nenhum backend, upload, pagamento, login ou envio. Portfólio de outra pessoa não é atribuído a Matheus. Limites visuais: Arial é aproximação, vetores são reconstruções, JPEG pequeno limita detalhe; o suporte de editar preserva cobertura e pode parecer dominante. Auditoria independente concluída:9,28/10, gate>9,0 atingido; diferenças residuais em AUDITORIA.md.

As capturas captura-375.png / captura-390.png / captura-430.png são os raw finais ou cópias idênticas dos raw em screenshots/, sem edição. Candidatos e versões anteriores são históricos, não prova da versão aprovada.
