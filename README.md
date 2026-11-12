# MODEL

## Avanços da integração — publicação de trabalho em andamento

As onze telas estão implementadas nesta versão. Entrada e navegação foram conectadas; favoritos, salvos, filtros, mensagens, edição e leitura de notificações usam estado compartilhado com persistência local. **21 testes de navegação e estado passaram na última reexecução.** Autenticação e serviços reais continuam fora desta entrega.

**Acessibilidade e aceite integrado final permanecem pendentes.** Há alertas de contraste/ARIA/rótulos, sobreposições de toque e necessidade de novas capturas das telas modificadas. A revisão independente da última rodada de estado não foi concluída; os testes não substituem essa revisão. As notas abaixo são aprovações visuais históricas das versões indicadas nas respectivas auditorias, não aprovação automática do código integrado atual.

[Avaliação atual](docs/correcoes-123/AVALIACAO_ATUAL.md) · [Relatórios de implementação e revisão](docs/correcoes-123/revisoes/) · [Plano de correção](docs/superpowers/plans/2026-11-11-correcao-global-model.md).

Para testar: `npm ci` e `npm run test:e2e`. Para navegar: `python3 -m http.server 8765 --bind 127.0.0.1`, abrir `http://127.0.0.1:8765/`.


Aplicativo editorial para descoberta e contratação de modelos masculinos. Protótipos frontend locais; autenticação, persistência e backend não integrados.

## Validação do projeto como conjunto

**Pendente como aplicativo integrado.** A revisão global de11/11/2026 confirmou o carregamento dos nove protótipos e identificou navegação incompleta, estado isolado, pendências de acessibilidade e sobreposição de toque em Filtros. Aprovação visual individual não equivale a aprovação do produto completo. [Relatório e evidências](docs/VALIDACAO_GLOBAL.md). [To-do de correção](docs/superpowers/plans/2026-11-11-correcao-global-model.md).

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
