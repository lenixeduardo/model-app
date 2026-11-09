# Tela04 — Perfil de Enzo

Versão `1.0.0-prototipo.1`. **Aprovada visualmente em9,30/10**, auditoria independente semP1 material. Gate>9,0 atingido; meta9,5 permanece. Consulte AUDITORIA.md para pesos, hashes eP2.

Frontend estático independente com HTML, CSS e JS nativos. Servir a raiz do repositório (`python -m http.server 8000`) e abrir `/MODEL_tela_04_V1/`; isso preserva o link real à Tela03 aprovada. Nenhuma dependência externa em produção.

`python MODEL_tela_04_V1/render.py` usa Playwright e Chromium `/usr/bin/chromium`, servidor da raiz, DPR1, capturas reais375×812,390×844 e430×932 antes de interagir. `--candidate` gera somente o candidato390. `python MODEL_tela_04_V1/compare.py` compara referência e390 com altura844 e proporções preservadas. O teste foi criado e executado primeiro com falha esperada por HTML ausente.

Verificações automatizadas: imagens/SVGs carregados, ausência de erros de console/rede e overflow, controles>=44px, salvar, quatro recortes em diálogo, contato/compartilhar/opções/mensagem, Escape, retorno de foco, foco visível e link real03. Relatório: `relatorio-browser.json`. Fotos usam `object-fit:cover`, sem transformações ou distorção; a quarta continua parcial. CSS declara safe-area por viewport-fit; ações ficam afastadas da borda e conteúdo reduzido em altura pode rolar. Redução de movimento declarada sem animações; fallback conserva alt e fundo neutro. Esses últimos itens são revisão de código; não equivalem a teste físico de dispositivo/VoiceOver.

O contador1/8 pertence ao mockup; há somente quatro recortes fornecidos. Salvar vale só nesta sessão. Diálogos informam o caráter demonstrativo e não enviam solicitações ou mensagens. Baixa resolução e ícones aproximados estão documentados em ASSETS.md. Nenhuma fotografia foi gerada, substituída ou reconstruída. Tela03 não foi alterada. Tela05 foi liberada para planejamento após esta auditoria04>9,0; sua nota e suas capturas serão próprias.
