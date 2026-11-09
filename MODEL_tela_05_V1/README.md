# Portfólio — tela05

Versão `1.0.0-prototipo.1`. **Aprovada visualmente em9,34/10**, auditoria independente semP1 material; gate>9,0 atingido. HTML/CSS/JS nativos e sete recortes oficiais locais. Servir a raiz do repositório: `python -m http.server 8000` em `model-app`; abrir `/MODEL_tela_05_V1/`. Link Voltar aponta à04 aprovada;03/04 não foram alteradas.

Estado inicial: status simulado9:41, Portfólio, Fotos/Vídeos/Trabalhos e sete fotografias. Abas vazias informam honestamente a ausência de arquivos. Lupa abre busca por descrição local, sem servidor. Fotos abrem exatamente o crop disponível em dialog; Escape/botão fecham e restauram foco. Dialog modal nativo contém foco; abas respondem a setas/Home/End. Alvos44px e foco visível. Nenhuma chamada externa, upload, publicação ou backend.

Reprodução: `python MODEL_tela_05_V1/render.py` gera capturas raw DPR1 e relatório; `--candidate` gera somente candidato390. `python MODEL_tela_05_V1/compare.py` gera referência e captura390 com altura844 e proporção preservada. Requer Pillow, Playwright e Chromium em `/usr/bin/chromium`.

TDD: primeiro render.py foi executado antes do HTML e falhou com `Expected implemented index.html; HTML absent (TDD red)`. Após implementação, testes reais passaram nos três tamanhos. Relatório inclui browser, console/rede, dimensões, imagens, alvos, ações e hashes.

Limites: fonte172×404 de baixa resolução. Fotos06/07 são parciais e permanecem assim. Tiles têm largura proporcional à viewport e alturas proporcionais ao painel; `object-fit:cover` preserva proporção natural e ajusta o enquadramento vertical aproximadamente8% em relação à fonte, sem estirar corpos/pixels. Nos parciais o crop é o limite absoluto de informação. Não há reconstrução ou geração. Fontes nativas e ícones vetoriais são aproximações. Pill Fotos usa44px mínimos para acessibilidade, ligeiramente maior que o escalonamento literal na menor altura.

Candidato390 inspecionado contra a fonte: corrigidos ícones pretos de SVG externo com inversão CSS e fechamento Escape do campo search. Capturas finais obtidas antes de interações. Auditoria independente concluída em9,34/10; planejamento06 liberado. A nota não é transferida à tela seguinte. Consulte AUDITORIA.md para rubrica, hashes eP2.
