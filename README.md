# MODEL

Aplicativo editorial para descoberta e contratação de modelos masculinos. Protótipos frontend locais; autenticação, persistência e backend não integrados.

## Estado validado

| Tela | Estado | Nota /10 | Evidência |
|---|---|---:|---|
| 03 — Swipe / Descobrir | Aprovada visualmente | 9,13 | [Auditoria](MODEL_tela_03_V2/AUDITORIA.md) |
| 04 — Perfil do modelo | Aprovada visualmente | 9,30 | [Auditoria](MODEL_tela_04_V1/AUDITORIA.md) |
| 05 — Portfólio | Aprovada visualmente | 9,34 | [Auditoria](MODEL_tela_05_V1/AUDITORIA.md) |
| 06 — Chat / Negociação | Aprovada visualmente | 9,28 | [Auditoria](MODEL_tela_06_V1/AUDITORIA.md) |
| 07 — Castings | Aprovada visualmente | 9,32 | [Auditoria](MODEL_tela_07_V1/AUDITORIA.md) |
| 08 — Filtros | Aprovada visualmente | 9,23 | [Auditoria](MODEL_tela_08_V1/AUDITORIA.md) |
| 09 — Salvos | Aprovada visualmente | 9,27 | [Auditoria](MODEL_tela_09_V1/AUDITORIA.md) |
| 10 — Meu perfil | Aprovada visualmente | 9,28 | [Auditoria](MODEL_tela_10_V1/AUDITORIA.md) |
| 11 — Notificações | Aprovada visualmente | 9,27 | [Auditoria](MODEL_tela_11_V1/AUDITORIA.md) |

Telas01/02 têm referências, mas seu código original não foi recebido neste workspace. A aprovação é visual, fundamentada nas três capturas reais e auditoria de cada tela, não em testes técnicos apenas. Meta9,5; gate de avanço>9,0. Tela03 usa legendas gráficas específicas do perfil de Enzo com H1/P acessíveis e fallback nativo; veja seus limites de integração no README próprio.

## Abrir

Na raiz: `python3 -m http.server 8765 --bind 127.0.0.1`. Abrir a pasta de cada tela, por exemplo http://127.0.0.1:8765/MODEL_tela_03_V2/. Servir a raiz preserva os links entre telas aprovadas.

Cada pasta contém HTML/CSS/JS, assets independentes, especificação, changelog, scripts de navegador e comparação, capturas e auditoria. As fotografias vêm dos mockups fornecidos; não foram geradas pessoas ou partes de corpo. Ações do protótipo ficam em memória.

[Fila de agentes](docs/FILA_AGENTES.md) · [Plano das últimas quatro telas](docs/PLANO_ULTIMAS_QUATRO.md). Os papéis são planejamento → assets → implementação → auditoria independente. Nenhuma nota é transferida para outra tela.
