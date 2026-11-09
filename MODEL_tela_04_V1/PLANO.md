# Tela04 V1 — plano de execução sequencial

Data:2026-11-09. Spec: `DESIGN_SPEC.md`. Pré-requisito concluído: Tela03 aprovada9,13 no ciclo7. **Tela04 ainda não implementada nem auditada.** Gate próprio>9,0, meta9,5. Sem iniciar planejamento/implementação da05.

## 1. Assets04 — próxima entrega

- Abrir painel04 e mockup geral; refinar os crops/boxes da especificação antes de exportar.
- Extrair foto principal monocromática e as três miniaturas completas + quarta parcial. Preservar identidade/pose/RGB, proporção e baixa resolução declarada; não substituir por Enzo03 colorido ou foto de login.
- Separar/remover UI da fotografia principal por máscaras alpha documentadas se necessário. Status/voltar/opções/contador são UI, não fotografia. Não inventar os pixels sob a pill1/8; a pill DOM deve se alinhar à região removida.
- Vetores locais de controles e selo, inventário de resolução/origem, manifesto de crop/máscara e hashes em `ASSETS.md`. Fontes e labels continuam HTML/CSS nativos sobre branco; não criar PNG de nome/bio/estatísticas.
- Sinalizar qualquer divergência ou lacuna real ao planejador antes da implementação. O contador1/8 não autoriza gerar mais quatro retratos.

## 2. Implementador04 — após handoff de assets

Criar `index.html`, `styles.css`, `app.js`, `README.md`, `CHANGELOG.md` e versão próprios em `MODEL_tela_04_V1/`, sem alterar a03 aprovada. Sem dependências de interface ou fonte externa obrigatória.

Ordem: foto/galeria e conteúdo claro → nome/local/categorias → dados físicos/bio → ações e acessibilidade. Aplicar o mapa192×404 da especificação; a pequena diferença de razão dos viewports deve ser absorvida por layout e crop proporcional, não estiramento da pessoa.

Interações locais mínimas, com estado inicial fiel ao mockup:

- Voltar: link à `../MODEL_tela_03_V2/`, preservando a versão aprovada.
- Miniaturas: abrir modal/visualização do recorte disponível ao toque/Enter, sem fabricar fotos não recebidas. Contador inicial1/8 continua como no mockup; não alegar que há oito arquivos completos no protótipo. As fotos recortadas não ganham detalhes por ampliação.
- Salvar: toggle local `aria-pressed`, com retorno acessível e sem persistência/backend implícitos.
- Compartilhar/opções/avião de papel: painéis locais explicando a ação disponível, sem envio automático de mensagem, dados de contato inventados ou links a telas ainda não liberadas.
- `Solicitar contato`: abre diálogo local com o mesmo título e estado explícito de protótipo; não afirmar solicitação enviada, aceitação ou contratação real. Fechar/Escape e retorno de foco precisam funcionar.
- Nenhum link de implementação à Tela05 antes do gate04. Não copiar seus dados/layout para esta etapa.

Rótulos acessíveis de ícones e texto explicativo de modais são permitidos para operação do protótipo; não são novos campos do perfil nem novos elementos do estado visual padrão. A tela principal conserva exclusivamente as informações do mockup.

## 3. Captura e verificação técnica

Criar script de renderização próprio ou adaptar o procedimento da03 sem alterar seus artefatos. Chromium/Playwright real, servidor local, DPR1; gerar `captura-375.png`, `captura-390.png`, `captura-430.png`, `relatorio-browser.json` e `comparacao-390.png`. Comparação com referência04, alturas normalizadas e proporções preservadas.

Verificar: foto e miniaturas/SVGs carregados, console/rede sem erros, ausência de overflow horizontal e corte indevido, imagem sem deformação, todos os controles exigidos respondendo a clique/toque/teclado, alvos>=44px, foco visível, ordem de leitura, labels/alt, dialogs/Escape/retorno de foco, redução de movimento e fallback de imagem. Conferir safe areas declaradas; não alegar teste físico de iPhone/VoiceOver a partir de Chromium. Se fonte ampliada exigir scroll, preservar acesso a todo conteúdo e ações.

## 4. Auditor04 independente e ciclo

O auditor abre painel04, três capturas finais e comparação, lê relatório/manifesto e atribui notas: fotografia/identidade/enquadramento35%, geometria25%, tipografia/ícones/chips20%, cores10%, responsividade/acabamento10%. Notas devem refletir as imagens, não a necessidade de avançar a fila.

Prioridades de inspeção: a foto monocromática correta e sua escala; relação foto156/miniaturas50/conteúdo198 na fonte; continuidade da faixa de thumbs com quarta parcial; nome/localização corretos; quatro categorias; dados1,84m/78kg/42; bio legível e CTA final no mesmo enquadramento; ausência de UI duplicada ou lacunas de máscara no header.

Se nota<=9,0 ou houver bloqueador material, devolver diferenças ao papel responsável, corrigir, recapturar e reauditar. Não reutilizar aprovação03. Somente nota>9,0, ausência de bloqueadores e pacote/evidências completos libera05.

## Handoff imediato

Planejamento entregue. Próximo papel: **assets04**. Entregar foto/miniaturas/SVGs e manifesto independente; depois implementador04; por último auditor04. Não gerar código, imagem sintética ou nota no estágio de planejamento.
