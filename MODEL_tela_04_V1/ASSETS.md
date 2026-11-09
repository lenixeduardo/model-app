# Tela04 — assets V1

Data:2026-11-09. Etapa sequencial de assets após planejamento. A Tela03 aprovada não foi alterada. **Esta entrega não aprova a Tela04.**

## Fonte e identidade

Fonte única dos recortes fotográficos: `../MODEL_assets_v1/originais/mockup-geral.jpg`,1179×753px, SHA-256`9120f379280879ca9c7695eeccba7288630b6956b39708eb94311080dbedf3dd`. Foram abertas a fonte geral e a referência04 isolada192×404; ampliadas as áreas de miniaturas, contador e controle superior direito para refinar bordas.

O painel04 é`[634,0,826,404)`. A fotografia principal é **o retrato monocromático da própria Tela04**, não o retrato colorido da03, o painel editorial ou o outro anexo de login. Não houve geração de pessoa, pose, pele ou novos detalhes. A foto original limpa em alta resolução não foi recebida; esta é extração da referência limitada.

## Recortes entregues

Coordenadasglobais`[esquerda,topo,direita,base)` com direita/base exclusivas. Máscaras de frame/controle estão no manifesto, com endpoints inclusivos segundo Pillow.

| Asset em `assets/` | Crop global | Crop local ao painel04 | Dimensões | Classificação |
|---|---|---|---:|---|
| `hero-enzo-perfil.png` | `[634,0,826,156)` | `[0,0,192,156)` | 192×156 | Hero correto monocromático, com UI retirada por alpha. |
| `thumb-01.png` | `[639,157,690,205)` | `[5,157,56,205)` | 51×48 | Primeira miniatura completa visível, colorida. |
| `thumb-02.png` | `[693,157,745,205)` | `[59,157,111,205)` | 52×48 | Segunda miniatura completa visível, monocromática. |
| `thumb-03.png` | `[748,157,800,205)` | `[114,157,166,205)` | 52×48 | Terceira miniatura completa visível, monocromática. |
| `thumb-04-parcial.png` | `[803,157,826,205)` | `[169,157,192,205)` | 23×48 | Somente a parte da quarta miniatura que aparece à direita. Não é foto completa. |

As miniaturas não contêm texto. As bordas e cantos são UI da galeria, retirados por alpha: trim1px e raio3 nas miniaturas1/3; trim2px e raio3 na2, cuja borda branca é mais marcada na fonte. A quarta tem somente o contorno esquerdo/cantos visíveis; a máscara se estende para além da direita para não inventar um canto arredondado onde a viewport corta a foto. Os pixels fotográficos preservados mantêm RGB exato.

A segunda miniatura tem uma borda clara de seleção visível na referência. Ela deve ser recriada como UI da galeria; sua presença não permite inferir oito arquivos completos. **1/8 é o texto do contador do mockup**, não inventário de oito fotografias disponíveis. O modal pode mostrar apenas o recorte fornecido, sem fabricar o lado oculto da quarta.

## Remoção da UI do hero

O hero tem **29.085pixels visíveis com RGB idêntico à fonte** e867pixels transparentes com RGB zero. Não há UI completa embutida como fundo, preenchimento dos buracos, inpainting, clonagem ou reamostragem.

| UI removida | Bounds locais de busca/removal | Método |
|---|---|---|
| Hora | `[12,2,36,16]` | Contornos claros,43sementes;116pixels após dilatação1px. |
| Sinal/Wi-Fi/bateria | `[141,2,186,16]` | Contornos claros,102sementes;208pixels após dilatação1px. |
| Chevron voltar | `[10,22,27,43]` | Contornos claros,12sementes;48pixels após dilatação1px. |
| Controle superior direito | `[164,21,186,43]` | Contornos claros,12sementes;55pixels após dilatação1px. |
| Pill contador1/8 | `[159,130,182,148]` | Retângulo arredondado inteiro, raio9. Não é preenchido com fotografia. |

Critério dos contornos:`minRGB>=90 && maxRGB-minRGB<=35`, restrito aos bounds listados e revisado visualmente; dilatação1px para retirar antialiasing. Esses bounds estão sobre fundo predominantemente escuro, afastados do rosto. A máscara externa usa cantos superiores de raio12 e forma estendida abaixo do recorte para retirar o bege dos cantos sem arredondar artificialmente a base do hero.

Prévias sobre preto e máscaras alpha estão em`assets/previews/`; abertas na inspeção. Não foram observados rótulos ou ícones brancos reconhecíveis sobrevivendo nas regiões retiradas. Os buracos existem e devem ser recobertos pela UI nativa co-registrada. O implementador deve conferir halos em captura real, especialmente no contador; alinhar a pill à caixa removida, não inventar pixels sob ela.

## Vetores locais independentes

| SVG em `assets/icons/` | Origem/certeza |
|---|---|
| `voltar.svg` | Cópia byte a byte do vetor03; chevron corresponde à função/desenho simples. |
| `verificado.svg` | Cópia byte a byte do selo03; aproximação vetorial conhecida, não vetor original. |
| `opcoes.svg` | Aproximação do pequeno símbolo superior direito04. No zoom ele parece um retículo/cruz de quatro pontas com centro, não três pontos. A fonte é pequena demais para identificar o glifo exato. Usar rótulo acessível funcional «Mais opções», sem novo rótulo visível ou alegação de ícone original. |
| `compartilhar.svg` | Aproximação vetorial local de seta/compartilhamento. |
| `salvar.svg` | Bookmark de contorno local. |
| `aviao.svg` | Avião de papel vetorial local. |

SVGs têm fundo transparente e usam`currentColor`; as fotografias não estão embutidas nos ícones. Para controles brancos sobre o hero, a integração deve aplicar cor/filtro apropriado ao SVG externo; os controles inferiores ficam escuros sobre claro. Não reutilizar inadvertidamente filtro invertido no selo azul.

## Texto e integração

Nome, localização, quatro categorias, números/legendas e bio devem ser HTML/CSS nativos, com fonte inicial Arial/Helvetica/sans-serif. Não há necessidade de foreground tipográfico raster aqui: o fundo é claro e uniforme, sem lacunas fotográficas atrás das legendas. Não copiar os PNGs de texto da03.

Posições/crops são específicos da geometria192×404. Projetar a foto proporcionalmente na caixa planejada com`object-fit:cover`/`object-position` ou equivalente; jamais esticar largura e altura da pessoa separadamente. O quarto recorte é parcial e deve continuar parcial, sem ser alargado horizontalmente para fingir imagem inteira.

O hero não deve conter status ou contador raster restaurados no fundo: reconstruir controles como UI independente. Todos os dados exibidos permanecem os da especificação; não adicionar nome, disponibilidade, contato ou oito arquivos inexistentes.

## Reproduzir e verificar

Da raiz do repositório:

```sh
python MODEL_tela_04_V1/assets/extract_assets.py
```

Dependência de desenvolvimento: Pillow já disponível no ambiente. O script exporta os crops, aplica máscaras, zera RGB invisível e percorre todos os pixels preservados para comprovar igualdade com a fonte. Também valida XML dos novos SVGs, registra hashes de todos os arquivos e confirma cópias vetoriais por identidade de bytes. Manifesto completo:`assets/manifest.json`.

Hashes das fotos finais:

- Hero:`d080e0c08db39731b621d34d9ca8486a951ea15d388bcf326d2f406ceb5b94d3`.
- Thumb1:`dbe616c1ed2aa7df28e3addb83966aff9804ad115c591407c0705ed79ea91e3a`.
- Thumb2:`c67a1166c63ea2f33bfbb84db6ede43af4720bbb9660550a5af6002e9876bcee`.
- Thumb3:`da65542e37b6bae3ae3e5d254bceaf861ed0ef7fa4192c9f54578e9cbb71dc61`.
- Thumb4parcial:`f7b9841fcfc56184519dd06313569099ef68df9139138cd377e5e51c3a7fe3a0`.

Próximo papel: implementador04. Nenhum HTML/CSS04, captura, auditoria, arquivo da03 aprovada ou publicação foi alterado por este agente. A Tela05 continua aguardando gate04.
