# Tela08 — plano executável V1

Execução autorizada após gate07V2 de9,32/10. Contrato: [DESIGN_SPEC.md](DESIGN_SPEC.md). Este papel só entrega planejamento; preservar03–07.09–11 aguardam aprovação sequencial. Sem confirmação adicional.

## 1 — Assets08 (próximo papel)

Entregar `ASSETS.md`, `assets/manifest.json` e SVGs locais; script reproduzível se houver transformação.

- Reconfirmar referência200×317 e crop global[220,434,420,751] RGB idêntico ao original1179×753; registrar hashes.
- Conferir pictograma do campo, voltar, chevron e três status; reutilizar SVGs existentes somente com origem/hash e adequação visual documentados. Registrar aproximações, cores amostradas e incertezas do JPEG.
- Não extrair fotografia inexistente, nem rasterizar textos/chips/trilhos. Não gerar pessoas/corpos. Não usar referência integral como interface.
- Liberar implementador08 somente com assets utilizáveis e relatório, sem atribuir nota.

## 2 — Implementação08

Entregar `index.html`, `styles.css`, `app.js`, `VERSION`, `README.md`, `CHANGELOG.md` e verificação funcional reproduzível. Frontend nativo local; dependências necessárias autorizadas. Sem backend/API/persistência.

- Implementar estado inicial e composição exatos do contrato, textoArial nativo e SVGs locais; não acrescentar rótulos visíveis no default. Não editar07 para inserir navegação/estado.
- Implementar input cidade, distância, três faixas editáveis com dialog de extremos, categorias independentes, disponibilidade exclusiva, Limpar completo e Aplicar com resumo explicitamente local. Voltar aponta à07 aprovada; aplicar não afirma mudar castings.
- Verificações comportamentais: edição cidade/distância e extremos de cada faixa, teclado no slider, rejeição de mínimo>máximo, formatação pt-BR, multisseleção de categorias, exclusividade de disponibilidade, reset após edição de todos os campos, resumo fiel ao estado, reload restaurando default e navegação07.
- Garantir nomes acessíveis,44px sem sobreposição, foco, teclado, Escape, foco contido/restaurado em dialogs, safe areas e reduced-motion. Usar textContent para valores. Sem requests externos.

## 3 — Capturas e verificação real

Entregar renderização reproduzível, `relatorio-browser.json`, `screenshots/375x812.png`, `screenshots/390x844.png`, `screenshots/430x932.png`, `comparacao-390.png` e hashes ligados à versão.

- Servir raiz local, testar em navegador real DPR1. Conferir console/rede/recursos, overflow inicial, todos controles e navegação; separar cenários de dialog/erro/reduced-motion das capturas default.
- Capturar candidata390, abrir e corrigir diferenças justificadas. Capturar três finais limpas no estado inicial, sem foco/dialog aberto. Sem overflow default nas três dimensões.
- Gerar comparação390 à mesma altura da referência, preservando cada proporção. Abrir as três capturas e comparação. Registrar navegador, comandos, limitações, versão e hashes. Não atribuir nota própria.

## 4 — Auditor08 independente

Entregar `AUDITORIA.md` e atualizar `docs/FILA_AGENTES.md`.

- Abrir referência, três capturas finais e comparação; conferir dimensões/hashes/versão, geometria, textos, ícones, cores e adaptação. Rever testes; distinguir revisados dos repetidos.
- Fotografia N/A; normalizar os65% restantes conforme DESIGN_SPEC: (25G+20T+10C+10R)/65. Não dar10 gratuito por ausência de fotos, não alterar critérios/notas das telas anteriores.
- Registrar diferenças e bloqueadores. Gate>9,0, meta9,5, nenhum P1 material; nota exatamente9 não libera09.
- Reprovação corrigível retorna ao papel responsável, com nova versão/capturas/auditoria. Bloqueio incontornável exige evidência e condição de retomada;09 permanece aguardando.
- Só aprovação08 libera planejador09. Pacote completo e versão aprovada seguem para publicaçãoGitHub já autorizada pelo coordenador; este papel não publica.

**Handoff:** planejador08 concluído; próximo papel **assets08**. Sem assets novos, HTML/CSS/JS, capturas, nota ou publicação nesta etapa; sem planejamento09.
