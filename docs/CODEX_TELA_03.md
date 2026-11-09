# Codex — MODEL, Tela 03 (Swipe / Descobrir)

## Objetivo
Continuar a implementação da Tela 03 a partir da V2 e comprovar fidelidade ao terceiro painel do mockup original. Não avançar para a Tela 04 antes da aprovação.

## Papéis de revisão
1. **Analista visual:** identificar layout, tipografia, enquadramento, gradientes, indicador de progresso, textos e controles no mockup.
2. **Implementador:** criar HTML/CSS responsivo com assets independentes, mantendo o retrato de Enzo e a identidade editorial.
3. **Auditor:** comparar capturas reais com a referência, pontuar critérios, apontar divergências e solicitar nova iteração se a nota for inferior a 9,0.

## Correções prioritárias
- Preservar o enquadramento e as proporções do retrato de Enzo.
- Ajustar posições e dimensões dos botões ignorar, favoritar e curtir.
- Ajustar nome, idade, localização, categorias e selo de verificação.
- Reproduzir o indicador superior de progresso com cinco segmentos.
- Respeitar safe areas, barra inferior e contraste.
- Evitar fotografias com textos embutidos; separar assets da interface.

## Validação obrigatória
- Executar o HTML em navegador real (Playwright/Chromium ou alternativa compatível).
- Gerar screenshots em 375×812, 390×844 e 430×932.
- Comparar lado a lado com a Tela 03 da referência, na mesma escala.
- Verificar carregamento de imagens e SVGs, overflow e alinhamento.
- Documentar pontuação fundamentada por critério e divergências restantes.
- Repetir o ciclo até **nota mínima 9,0/10**, buscando **9,5/10**.

## Regra de bloqueio
Se o navegador não produzir capturas verificáveis, marcar a versão como **não validada**, documentar o erro e tentar outra estratégia de renderização. Nunca atribuir nota de aprovação com base somente no código.

## Próximo passo
Adicionar ao repositório os arquivos locais da V2, a imagem de referência e os assets originais, preservando os direitos e a origem das fotografias.
