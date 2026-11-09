# MODEL

Aplicativo editorial para descoberta e contratação de modelos masculinos.

## Tela03 V2 — implementação disponível

[Protótipo e instruções](MODEL_tela_03_V2/README.md) · [Auditoria visual](MODEL_tela_03_V2/AUDITORIA.md) · [Comparação](MODEL_tela_03_V2/comparacao-390.png)

Da raiz:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Abrir http://127.0.0.1:8765/MODEL_tela_03_V2/.

HTML/CSS/JS e assets independentes. Capturas reais de375×812,390×844 e430×932, DPR1, Chromium156.0.8078.79. Testes de interações, teclado, carregamento e overflow em MODEL_tela_03_V2/render.py; relatório em relatorio-browser.json.

**Estado: Tela03 aprovada visualmente em9,13/10**, versão2.0.0-prototipo.7, ciclo7. Capturas e auditoria independentes documentadas. O torso foi recuperado de pixels existentes no mockup, sem gerar pessoa ou pele. Nome/localização usamUIforegrounds específicos do perfil, com H1/P acessíveis e fallback nativo para falha/novos dados; consulte limitações no README da tela.

Fila de agentes: [planejamento → assets → implementação → auditoria](docs/FILA_AGENTES.md). O gate>9,0 da Tela03 foi atingido e libera o planejamento da Tela04. As telas seguintes precisam de suas próprias capturas e notas.

## Estado das demais telas
- Tela01 — Login: referência disponível; autenticação não integrada.
- Tela02 — Descobrir: V3 mencionada no handoff, código ainda não recebido.
- Tela04 — Perfil do modelo: planejamento liberado e iniciado após aceite da03.
- Telas05–11: aguardam aprovação da tela anterior.

## Arquivos
- MODEL_tela_03_V2/: implementação, assets, screenshots, comparação, especificação, auditoria, changelog e scripts reproduzíveis.
- MODEL_assets_v1/: recortes e anexos originais enviados pelo usuário. Publicação dos originais autorizada em2026-11-09. As referências completas contêm interface incorporada; não são fotografias limpas nem capturas do app.
- docs/CODEX_TELA_03.md: contrato de fidelidade e validação.

Identidade editorial preto/branco/bege. Não substituir Enzo ou gerar partes ausentes para alegar fidelidade. Gate atual: nota superior a9,0/10; objetivo9,5/10. Dados e ações do protótipo ficam em memória; sem backend.
