# Tela 03 — revisão de assets

Data: 2026-11-09. Papel: agente de assets, após planejamento. **Resultado: fotografia integral limpa não encontrada nas fontes locais verificadas.** Os arquivos atuais preservam Enzo, mas não permitem recuperar fielmente o torso atrás das informações. Gate atualizado da fila: nota **>9,0**, meta9,5.

## Fontes efetivamente verificadas

Inventário por `rg --files` em `/workspace`, anexos em `/tmp/codex-remote-attachments`, `shared` e `library-files`; dimensões lidas com Pillow. Foram abertas visualmente as duas fontes originais, referência isolada, recorte parcial, descoberta, painel editorial e captura390. O mockup geral foi inspecionado integralmente para conferir também os pequenos retratos de perfil/portfólio/salvos.

Os dois anexos remotos são cópias byte a byte dos arquivos em `MODEL_assets_v1/originais/`; as duplicatas em `/workspace/MODEL_assets_v1/` também não representam novas fontes. Não há arquivo fotográfico independente com o enquadramento integral exigido.

| Arquivo relativo à raiz | Dimensões | Origem e uso permitido |
|---|---:|---|
| `MODEL_assets_v1/originais/mockup-geral.jpg` | 1179×753 | Anexo `2-Foto-2.jpg`. Mockup raster completo; textos, ícones e sobreposição fazem parte dos pixels. Fonte de comparação e recortes documentados, não fotografia limpa. |
| `MODEL_assets_v1/originais/login-referencia.jpg` | 430×932 | Anexo `1-Foto-1.jpg`. Fotografia/pose diferentes, monocromática, com UI de login incorporada. Não substitui o retrato colorido oficial. |
| `MODEL_assets_v1/referencias/referencia-tela-03.png` e `03-swipe.png` | 203×404 | Mesmo recorte `[420,0,623,404]` do mockup; interface incorporada. Referência oficial, não fundo independente. |
| `MODEL_assets_v1/assets/enzo-retrato-parcial.png` | 201×242 | Extração fiel `[421,28,622,270]`, única área grande limpa da foto oficial. Sem textos; termina no peito antes da área de nome/localização/chips. |
| `MODEL_tela_03_V2/assets/enzo-swipe-referencia.png` | 201×242 | Cópia exata do recorte acima; asset de runtime. Não é fotografia integral nem imagem em alta resolução. |
| `MODEL_tela_03_V2/assets/enzo-ceu-topo.png` | 201×8 | Faixa limpa `[421,14,622,22]` do mesmo mockup. Evidência de extração; não usada no runtime final porque sua ampliação produziu banding. |
| `MODEL_assets_v1/referencias/02-descoberta.png` | 199×404 | Cartão de Enzo com a mesma pose, em área fotográfica menor e também com texto incorporado. Não contém o torso integral limpo nem aumenta o detalhe da fonte. |
| `MODEL_assets_v1/referencias/04-perfil-modelo.png` | 192×404 | Retrato principal/miniaturas com outros recortes/poses; não recupera a camada original da foto03. |
| `MODEL_assets_v1/referencias/05-portfolio.png` | 172×404 | Mosaico de fotos/poses diferentes, resolução menor; não substitui o mesmo enquadramento03. |
| `MODEL_assets_v1/referencias/09-salvos.png` | 176×317 | Miniatura da mesma pose, menor e com cartão/UI incorporados. Não acrescenta a área de torso ausente. |
| `MODEL_assets_v1/referencias/painel-editorial.png` | 176×317 | Homem olhando para outro ângulo, com composição/pose diferentes. Não usar como substituição. |

Demais recortes do mesmo mockup: `01-splash.png`188×404, `06-chat.png`156×404, `07-castings.png`201×317, `08-filtros.png`200×317, `10-meu-perfil.png`185×317 e `11-notificacoes.png`184×317. São telas com UI incorporada; não contêm o arquivo limpo do retrato03. Coordenadas de todos os recortes constam de `MODEL_assets_v1/manifest.json`.

### Identidade das fontes

SHA-256:

- Mockup geral: `9120f379280879ca9c7695eeccba7288630b6956b39708eb94311080dbedf3dd`.
- Login: `2a61473dc4535c17185fe431f5fddc1a6c3c03684e5db3d0bf560ce755e91238`.
- Retrato parcial e sua cópia de runtime: `0eba9a3a98add154419e5599836079909e6f15167a368566ef5e7685bcb1fb86`.
- Referência03 e `03-swipe.png`: `20078867f604b6771214ec52a7a55d12c3843c822721ceda1fd4561aab6dc409`.

## Classificação para implementação

**Extração fiel utilizável:** o retrato parcial preserva os pixels e a proporção naturais do rosto/ombros. Pode continuar no protótipo identificado como parcial. Não se deve esticar ou ampliar sua altura para aparentar o torso ausente. O céu extraído também é fiel, mas não supre o fundo integral.

**Aproximações identificadas:** sete SVGs locais (`voltar`, `opcoes`, `fechar`, `estrela`, `coracao`, `informacao`, `verificado`) foram reconstruídos, não exportados dos vetores originais. O preenchimento CSS do céu interpola cinco cores da fotografia; não é uma recuperação de textura fotográfica original. Não há arquivo de fonte tipográfica original fornecido.

**Insumo ausente:** imagem limpa do **mesmo retrato de Enzo**, com céu, cabeça, ombros e torso visíveis por trás do nome, localização e chips, sem textos, botões ou gradiente já incorporados. Preferível largura>=860px para DPR2; largura>=430px já melhora a entrega DPR1. Resolução maior não compensa pose ou enquadramento diferentes.

## Refinamento vetorial entregue

Criado `assets/icons/fechar-acao.svg`, variante independente proposta para a ação ignorar. `viewBox="0 0 24 24"`, traço1,8, diagonais entre4 e20. O X atual ocupa apenas12/24 da caixa; a referência mostra maior ocupação interna em relação ao círculo. A variante pode ser usada em uma caixa de40×40px dentro do círculo, ocupando aproximadamente26,7px de largura, sem mudar o alvo de toque. Ela **não foi conectada ao HTML** nesta etapa. O implementador deve compará-la na captura antes de decidir e não substituir o X de fechar diálogo indiscriminadamente.

Propostas adicionais ao implementador: ampliar o selo de cerca de23 para25px na viewport390 e calibrar chips com maior preenchimento vertical/borda. São aproximações verificáveis somente por nova captura. Nenhum vetor foi alterado in-place; estrela/coração/informação permanecem estáveis. Não há fundamento para retrabalhar todos os assets quando o bloqueio dominante é a fotografia.

## Bloqueio e decisão

Nenhuma fonte local resolve a ausência do torso integral limpo. Remover UI por geração/inpainting ou completar pixels do corpo criaria informação nova; não foi feito. Usar a captura inteira do mockup como fundo esconderia a dependência entre fotografia e interface; não foi feito. Também não foi substituída a pose pelo painel editorial ou login.

A nota fotográfica da auditoria atual é6,2 com peso35%. Mantida essa nota, mesmo supondo todos os demais critérios em10, a média seria `6,2×0,35 + 10×0,65 = 8,67`. Isso é um teto **ilustrativo sob essa hipótese**, não uma pontuação nova nem uma previsão de auditoria. Demonstra por que polir ícones sozinho não sustenta a promessa de>9.

Entrega de assets concluída como revisão e variante vetorial. **A obtenção do asset fotográfico suficiente está bloqueada.** O implementador pode avaliar o refinamento vetorial como protótipo não aprovado, mas não deve iniciar ciclos infinitos ou liberar a Tela04. Retomar o enquadramento final quando chegar a foto original limpa do mesmo retrato, ou se o usuário alterar explicitamente o contrato que proíbe fabricar a fotografia ausente.

Nenhuma captura, CSS/JS, auditoria visual ou publicação foi alterada por este agente.

## Publicação
O inventário acima descreve os arquivos locais. O recorte histórico de céu enzo-ceu-topo.png não é usado no runtime final e fica somente no pacote local. A cópia de runtime enzo-swipe-referencia.png reutiliza exatamente o blob já público de enzo-retrato-parcial.png, sem novos pixels.
