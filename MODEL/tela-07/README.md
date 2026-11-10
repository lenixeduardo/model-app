# MODEL — Tela 07 / Castings e Oportunidades

Implementação inicial independente, em HTML/CSS/JavaScript, sem build. Abra `index.html` em um servidor HTTP, com os SVGs compartilhados em `../assets/icons/`.

## Estado

- Cabeçalho, busca, chips, filtros, grid assimétrico, detalhes e navegação inferior implementados.
- Os quatro registros são **fictícios e demonstrativos**, identificados na interface. Nenhuma candidatura é enviada.
- Sem integração com Supabase, autenticação, pagamentos ou geocodificação. O campo de raio é coletado mas **não filtra por distância** até existir uma fonte geográfica confiável.
- Fotos de castings reais não foram fornecidas; os visuais são tipográficos e CSS, não representações de anúncios reais.
- Tela 02 permanece incompleta quanto aos PNGs de modelos. Esta tela não resolve a pendência.

## Validação pendente

1. Testar no Playwright/Chromium em 375×812, 390×844 e 430×932.
2. Comparar com o mockup original e revisar diferenças antes de atribuir nota.
3. Conectar dados reais do Supabase com políticas RLS, autenticação e autorização de candidatura.
4. Conectar a navegação ao roteador real do projeto, sem links demonstrativos.

**Não realizar merge na main sem a auditoria.**
