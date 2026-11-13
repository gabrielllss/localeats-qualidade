# Guia de estudo — Defesa Técnica 1 (Gabriel Lopes Soares)

## Atividade 1 — Fundamentos e características da qualidade

- **Necessidade explícita x implícita (meus exemplos):**
  - Explícita: criar conta e entrar com e-mail e senha; pesquisar e filtrar por especialidade ou localização.
  - Implícita: dados de login protegidos com sessão segura; busca rápida e compreensível mesmo sem resultados.
  - Consequência: sem explícita não acessa / não acha; sem implícita há vazamento, perda de confiança, percepção de sistema quebrado.

- **Funcionalidade explorada e evidência:**
  - Explorar restaurantes (busca + filtro). Logado na tela Explorar: digitei `Italiana` e cliquei Buscar, depois cliquei no filtro Italiana. Nos dois casos apareceu `Nenhum restaurante encontrado`, embora a listagem inicial tivesse italianos. Descoberta: busca filtra por localização, não por culinária.
  - Evidência: `atividades/atividade-01/evidencias/gabriel-explorar-filtro-italiana-sem-resultado.jpg`

- **Requisito de qualidade formulado:**
  - "Ao buscar ou filtrar por especialidade existente (ex.: Italiana), exibir apenas restaurantes daquela especialidade, e quando não houver resultados exibir mensagem orientativa."

- **Característica escolhida:**
  - Adequação Funcional — Correção Funcional (ISO/IEC 25010). Justificativa: retorna conjunto errado (zero em vez dos italianos), é falha de correção, não de estética ou rapidez.

- **Como avaliar:**
  - Observar e contar: para especialidades existentes, registrar quantas retornam conjunto correto; verificar se mensagem sem resultados informa especialidade e sugere alternativa.

- **Pergunta clássica:** sistema com tudo explícito pode ter baixa qualidade? Sim — se implícitas falham (lento, mensagem genérica sem orientação), funcionalidade existe mas experiência é ruim.

## Atividade 2 — Papéis e responsabilidades

- **Papéis analisados (6, todos por mim por ser individual):** PO, Analista de sistemas/negócio, Desenvolvedor, QA, DevOps, Liderança técnica.
- **Responsabilidade x competência:** responsabilidade = obrigação de entregar / prestar contas; competência = capacidade (conhecimento + habilidade + atitude). Ex.: QA tem responsabilidade de planejar testes do sistema, precisa de competência técnica em partição/valores-limite e comportamental em ceticismo produtivo e comunicação sem tom acusatório.
- **Técnicas x comportamentais (exemplos meus):** Dev — técnica: testes unitários/integração, Git, revisão; comportamental: responsabilidade pelo próprio trabalho, humildade para revisão. PO — técnica: critérios de aceitação, priorização por valor/risco; comportamental: dizer não com justificativa.
- **Por que qualidade é compartilhada:** nasce em produto, requisito, código e esteira. Só QA no fim vira gargalo, acha tarde quando custa caro. Cada papel responde por parte; QA também facilita práticas.
- **Matriz RACI (9 linhas, 1 A por linha):**
  - Ex.: Definir critérios = A PO, R Analista. Implementar = R Dev, A Liderança. Planejar/testes sistema = R QA, A Liderança. Registrar defeitos = R QA, A Liderança. Aprovar versão = R QA + R DevOps, A Liderança.
- **Lacuna:** Registrar defeitos só tem R no QA (se QA falta, perde-se histórico); Aprovar versão concentra A na Liderança que também é A de implementação/revisão (conflito — aprova próprio trabalho). Correção: Dev também R pelo defeito que corrige, PO como C na aprovação.
- **Práticas propostas:** 1) DoD acordada e checada (aceitação validado, unitários, revisão, sistema sem bloqueantes, evidência). 2) Triagem com registro único, severidade, evidência e reunião curta de prioridade.

## Atividade 3 — Estratégia e projeto de testes

- **Minha funcionalidade:** Pesquisar restaurantes por especialidade ou localização. Fora de escopo: Fazer pedido (transacional, outro ciclo).
- **Decisões do plano:** Nível sistema, tipo funcional, caixa-preta. Técnicas: particionamento + tabela de decisão. Ambiente: app no ar, Chrome 1280x720, conta de teste, catálogo com Italiana e Centro.
- **Riscos:**
  - R01 Alta/Alta/Alta: termo de especialidade aplicado ao filtro de localização → busca Italiana retorna vazia. Visto na Atividade 1.
  - R02 Média/Média/Média: mesma mensagem genérica para vazio e falha → usuário não distingue. Mensagem era só "Nenhum restaurante encontrado."
- **Técnicas e aplicação:**
  - Particionamento (R01): V1 vazio `""` → lista tudo; V2 `Italiana` → só italianos; V3 `Centro` → só Centro; V4 `XYZabc` → vazio com mensagem citando termo; I1 `"   "` → tratar como vazio. Deriva CT01 e CT02.
  - Tabela decisão (R02): combina termo informado? requisição concluída? há resultados? Regras 1 lista tudo, 2 lista compatíveis, 3 mensagem de ausência citando termo + limpar busca, 4 mensagem de erro distinta + tentar novamente. Deriva CT03.
- **Casos:**
  - CT01: buscar `Italiana` → só cartões Italiana.
  - CT02: buscar `Centro` → só cartões Centro.
  - CT03: buscar `XYZabc` → mensagem de ausência citando termo; bloquear API e buscar `Italiana` → mensagem de erro distinta com tentar novamente.
- **Rastreabilidade:** R01 → partição → CT01, CT02. R02 → decisão → CT03.
- **Critérios:** Entrada: app no ar, logado, catálogo com especialidades/localizações distintas. Saída: todos casos executados com evidência, R01 e R02 com ao menos 1 caso. Suspensão: app fora do ar, catálogo vazio, 5xx generalizado.

## Pequenas alterações — respostas prontas com meu trabalho

- **Limite/regra mudou (ex.: buscar também por nome do prato):** reviso classes V2/V3, adiciono classe e CT novo, atualizo CT01/CT02 e requisito de Correção Funcional.
- **Sem QA:** Dev assume R de execução e registro do que corrige, PO assume A de aceite/priorização, Liderança mantém A técnico mas com C do PO na liberação; aplico DoD e triagem para não perder histórico. Priorizo R01/CT01.
- **Correto mas lento:** reviso característica: de Correção Funcional para Eficiência de Desempenho / Comportamento Temporal, crio requisito <2s e teste de carga, mantendo funcionais.
- **Tempo cortado:** executo R01/CT01 e CT02 primeiro, depois R02/CT03; I1 fica como cobertura futura (já previsto).

## Uso de IA (declarar se perguntarem)

Muse Spark para redação/organização e ISO/RACI. Rejeitei valor-limite como principal na Atividade 3 porque busca é textual sem limites numéricos. Verifiquei com exploração manual, conferência de RACI (1 A por linha) e rastreabilidade risco→técnica→caso.
