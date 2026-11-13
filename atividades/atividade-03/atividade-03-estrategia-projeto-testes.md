# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Turma:** ADS5N26-2C
**Equipe:** Individual (1 integrante)
**Data:** 12/11/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Gabriel Lopes Soares | @gabrielllss |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se a pesquisa de restaurantes retorna exatamente os estabelecimentos compatíveis com o termo informado — por especialidade (ex.: "Italiana") ou por localização (ex.: "Centro") — e se os estados de "nenhum resultado" e de "falha de carregamento" são comunicados de forma clara, distinta e acionável ao usuário, de modo que ele saiba se deve corrigir o termo ou tentar novamente mais tarde.

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Gabriel Lopes Soares | Pesquisar restaurantes por especialidade ou localização | Se o termo digitado é aplicado ao campo correto (especialidade ou localização), se o conjunto retornado corresponde ao termo e se a ausência de resultados é informada de forma orientativa. |

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Fazer pedido | Envolve fluxo transacional (carrinho, itens, confirmação e persistência do pedido) e depende de dados de cardápio; fica fora do recorte de busca definido para este ciclo de testes e será tratada em um ciclo específico. |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Sistema | O comportamento a verificar é o resultado apresentado ao usuário na tela Explorar, do preenchimento do termo até a listagem final; testes unitários não alcançam a integração entre formulário, filtros e API. |
| Tipos de teste | Funcional | O foco é a regra de negócio da busca (termo → conjunto de restaurantes) e a mensagem exibida em cada estado, não atributos como desempenho ou segurança. |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | Os casos serão derivados do que o usuário informa e do que a interface exibe, sem acesso ao código; a evidência da Atividade 1 mostra que o problema é observável pela interface, o que torna a caixa-preta suficiente para este recorte. |
| Técnicas de teste | Particionamento de equivalência e tabela de decisão | A busca recebe um texto livre, com classes de entrada bem distintas (especialidade válida, localização válida, termo inexistente, termo vazio) — cenário típico de particionamento. A comunicação de estados depende da combinação entre termo informado e existência de resultados, o que é melhor representado por tabela de decisão. |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Aplicação em <https://local-eats-unisenac.vercel.app/>, navegador Chrome atualizado em desktop (1280x720), conexão estável de internet, uma conta de teste criada exclusivamente para a atividade (sem dados pessoais reais) e catálogo contendo ao menos uma especialidade e uma localização conhecidas (ex.: "Italiana" e "Centro"). |
| Responsáveis pelo planejamento | Gabriel Lopes Soares |
| Responsáveis pela especificação dos casos | Gabriel Lopes Soares |
| Responsáveis pela futura execução | Gabriel Lopes Soares |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | Aplicação disponível e acessível, conta de teste autenticada, catálogo carregado com restaurantes de especialidades e localizações distintas e termos de busca conhecidos definidos (ex.: "Italiana", "Centro", "XYZabc"). |
| Saída | Todos os casos planejados executados, resultado de cada um registrado como aprovado ou reprovado com evidência, e cada risco (R01 e R02) com pelo menos um caso executado e conclusão registrada. |
| Suspensão | Aplicação fora do ar, catálogo vazio, ausência de restaurantes para as especialidades/localizações de referência ou API retornando erro generalizado (5xx) que impeça distinguir falha do sistema de ausência de resultados. |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | Gabriel Lopes Soares | Pesquisar restaurantes por especialidade ou localização | O termo digitado é aplicado ao filtro de localização, e não ao de especialidade, fazendo uma busca por especialidade existente retornar lista vazia. | O usuário conclui que não há restaurantes daquela especialidade, desiste da busca e a aplicação perde o propósito principal de descoberta. | Alta | Alto | Alta | O comportamento foi observado na exploração da Atividade 1: buscar "Italiana" retornou "Nenhum restaurante encontrado" mesmo havendo restaurantes italianos na listagem inicial. Afeta diretamente a descoberta de restaurantes. |
| R02 | Gabriel Lopes Soares | Pesquisar restaurantes por especialidade ou localização | A interface usa a mesma mensagem genérica para "nenhum resultado" e para falha de carregamento, sem indicar o termo buscado nem oferecer ação de recuperação. | O usuário não distingue erro do sistema de busca sem correspondência, não sabe como corrigir e perde a confiança na aplicação. | Média | Médio | Média | A mensagem observada era apenas "Nenhum restaurante encontrado.", sem o termo nem orientação; a consequência é relevante, mas reversível e não bloqueia o uso de outras áreas. |

### 3.2 Aplicação das técnicas

#### Análise do integrante 1 — Técnica 1: particionamento de equivalência

**Integrante:** Gabriel Lopes Soares
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização
**Risco relacionado:** R01
**Técnica escolhida:** Particionamento de equivalência

**Por que a técnica foi escolhida:**
O campo de busca aceita texto livre, com infinitas possibilidades de entrada, mas o comportamento esperado depende apenas da classe a que o termo pertence — especialidade existente, localização existente, termo sem correspondência ou campo vazio. Como todas as entradas de uma mesma classe devem produzir o mesmo tipo de resultado, o particionamento permite cobrir o risco R01 com poucos casos representativos, em vez de testar termos um a um.

**Aplicação da técnica:**

| Classe | Situação | Valor representativo | Resultado esperado |
|---|---|---|---|
| V1 | Campo vazio (sem termo) | `""` | Listar todos os restaurantes, sem filtro aplicado |
| V2 | Especialidade existente no catálogo | `Italiana` | Listar somente restaurantes com especialidade Italiana |
| V3 | Localização existente no catálogo | `Centro` | Listar somente restaurantes localizados no Centro |
| V4 | Termo sem correspondência | `XYZabc` | Nenhum item e mensagem informando que não há resultados para o termo |
| I1 | Termo composto apenas por espaços | `"   "` | Tratar como campo vazio (listar todos), sem erro na tela |

**Casos derivados:** CT01 e CT02.

As classes V1 e V4 são exercitadas indiretamente: a listagem inicial observada no passo 1 do CT01 corresponde à classe V1 e o cenário sem resultados do CT03 corresponde à classe V4. A classe I1 (termo composto apenas por espaços) fica registrada como cobertura futura, por ter risco menor que as demais.

#### Análise do integrante 1 — Técnica 2: tabela de decisão

**Integrante:** Gabriel Lopes Soares
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização
**Risco relacionado:** R02
**Técnica escolhida:** Tabela de decisão

**Por que a técnica foi escolhida:**
O risco R02 trata da comunicação do estado da tela, que não depende do valor do termo, mas da combinação entre "há termo informado", "existem resultados" e "a requisição falhou". São condições combinatórias, e a tabela de decisão explicita todas as combinações relevantes, evidenciando que os estados de vazio e de erro precisam de mensagens diferentes.

**Aplicação da técnica:**

| Regra | Termo informado? | Requisição concluída? | Existem resultados? | Resultado esperado |
|---|:---:|:---:|:---:|---|
| 1 | Não | Sim | Sim | Listar todos os restaurantes |
| 2 | Sim | Sim | Sim | Listar apenas os compatíveis com o termo |
| 3 | Sim | Sim | Não | Mensagem de ausência de resultados citando o termo e oferecendo limpar a busca |
| 4 | Sim ou Não | Não | — | Mensagem de erro de carregamento, distinta da mensagem de ausência de resultados, com opção de tentar novamente |

**Casos derivados:** CT03.

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

### CT01: Busca por especialidade existente retorna apenas restaurantes daquela especialidade

**Integrante responsável:** Gabriel Lopes Soares
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização
**Risco ou requisito relacionado:** R01
**Técnica utilizada:** Particionamento de equivalência (classe V2)

**Pré-condição:**
Usuário autenticado na tela Explorar, catálogo carregado e com pelo menos um restaurante de especialidade Italiana e pelo menos um de outra especialidade.

**Dados de entrada:**
Termo de busca: `Italiana`

**Passos:**

1. Acessar a tela Explorar e registrar a quantidade de restaurantes exibidos na listagem inicial.
2. Digitar `Italiana` no campo "Buscar por culinária ou localização...".
3. Acionar o botão "Buscar".

**Resultado esperado:**
A listagem exibe somente restaurantes cuja especialidade é Italiana, sem itens de outras especialidades; cada cartão exibido apresenta a especialidade Italiana.

---

### CT02: Busca por localização existente retorna apenas restaurantes daquela localização

**Integrante responsável:** Gabriel Lopes Soares
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização
**Risco ou requisito relacionado:** R01
**Técnica utilizada:** Particionamento de equivalência (classe V3)

**Pré-condição:**
Usuário autenticado na tela Explorar e catálogo com restaurantes em mais de uma localização.

**Dados de entrada:**
Termo de busca: `Centro`

**Passos:**

1. Digitar `Centro` no campo de busca.
2. Acionar o botão "Buscar".
3. Comparar a localização exibida em cada cartão com o termo informado.

**Resultado esperado:**
A listagem exibe apenas restaurantes cuja localização é Centro; nenhum cartão de outra localização é apresentado e a quantidade é menor ou igual à da listagem inicial.

---

### CT03: Ausência de resultados e falha de carregamento são comunicadas de forma distinta

**Integrante responsável:** Gabriel Lopes Soares
**Funcionalidade:** Pesquisar restaurantes por especialidade ou localização
**Risco ou requisito relacionado:** R02
**Técnica utilizada:** Tabela de decisão (regras 3 e 4)

**Pré-condição:**
Usuário autenticado na tela Explorar, catálogo carregado e acesso às ferramentas de desenvolvedor do navegador para simular indisponibilidade da API (modo offline ou bloqueio da requisição da listagem).

**Dados de entrada:**
Termo de busca: `XYZabc` no cenário sem resultados e `Italiana` no cenário com a API bloqueada.

**Passos:**

1. Com a conexão normal, digitar `XYZabc` no campo de busca, acionar "Buscar" e observar a mensagem exibida na área da listagem.
2. Ativar o modo offline (ou bloquear a requisição da listagem) e repetir a busca pelo termo `Italiana`.
3. Comparar a mensagem do passo 1 com a mensagem do passo 2.

**Resultado esperado:**
No passo 1, a tela informa que não há resultados para o termo pesquisado, citando o termo e sem mensagem de erro técnico. No passo 2, a tela informa falha de carregamento, com possibilidade de tentar novamente. As duas mensagens são diferentes entre si.

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Gabriel Lopes Soares | Pesquisar restaurantes por especialidade ou localização | R01: termo de especialidade aplicado ao filtro de localização | Particionamento de equivalência | CT01 e CT02 |
| Gabriel Lopes Soares | Pesquisar restaurantes por especialidade ou localização | R02: mensagem única para ausência de resultados e falha de carregamento | Tabela de decisão | CT03 |

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
Muse Spark (Sider) como apoio à redação e à organização do documento.

**Como foi utilizada:**
Apoio para estruturar o plano conforme o modelo oficial da atividade, organizar as tabelas de riscos, classes de equivalência e tabela de decisão, e revisar a rastreabilidade entre riscos, técnicas e casos de teste. A escolha da funcionalidade e a identificação do comportamento da busca partiram da exploração real da aplicação registrada na Atividade 1.

**Uma sugestão que precisou ser alterada ou rejeitada:**
Foi sugerido aplicar análise de valor limite como técnica principal da busca, mas a sugestão foi rejeitada: o campo de busca é textual e não possui limites numéricos, o que tornaria os casos artificiais. A técnica foi substituída por tabela de decisão, adequada ao risco R02, que trata da combinação entre termo informado, conclusão da requisição e existência de resultados.

**Como as respostas foram verificadas:**
Conferência da rastreabilidade (todo risco com casos associados), revisão das classes de equivalência contra o comportamento observado na aplicação e verificação de que os resultados esperados descrevem apenas o que é observável pela interface, sem suposições sobre código ou banco de dados. O conteúdo foi lido e é passível de defesa oral.
