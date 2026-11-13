# Atividade 2 — Organização da Qualidade no LocalEats

## 1. Identificação

**Unidade Curricular:** Qualidade de Software
**Turma:** ADS5N26-2C
**Metodologia:** Problem-Based Learning (PBL)
**Projeto:** LocalEats
**Modalidade:** Individual
**Equipe:** Individual (1 integrante)
**Data:** 12/11/2026

### Integrantes

| Nome | Usuário no GitHub |
|------|-------------------|
| Gabriel Lopes Soares | @gabrielllss |

**Elemento de Competência (EC2):** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

**Aplicação:** https://local-eats-unisenac.vercel.app/

---

## Tarefa 1: Diagnóstico da situação

| Problema identificado | Possível consequência para o produto ou para a equipe |
|-----------------------|--------------------------------------------------------|
| Não existe um critério de "pronto" acordado: cada pessoa entende de um jeito quando uma funcionalidade está concluída. | Funcionalidades são consideradas entregues apenas por "funcionarem na máquina do desenvolvedor", chegando ao usuário com defeitos e gerando retrabalho e perda de confiança. |
| A crença de que "somente o QA deve testar" concentra a verificação em uma única pessoa. | O QA vira gargalo do processo, os defeitos são descobertos tarde (quando o custo de correção já é alto) e o desenvolvedor não se sente responsável pela qualidade do que produz. |
| Defeitos são encontrados, mas nem sempre registrados e acompanhados, e não há clareza sobre quem aprova a liberação de uma versão. | Defeitos se perdem ou são reencontrados repetidamente, o histórico de qualidade não existe e versões podem ser publicadas sem avaliação, aumentando o risco de incidentes em produção. |

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

Não. O QA tem papel central de verificação e de organização das práticas, mas a qualidade nasce nas decisões de produto, na escrita dos requisitos, no código e na esteira de entrega — logo, é responsabilidade compartilhada. Se apenas o QA testa, ele se torna um gargalo e atua como "fiscal" no fim da linha, quando corrigir já custa caro. Por isso, cada papel precisa responder por parte da qualidade, e o QA deve atuar também como facilitador de práticas, e não como único dono do resultado.

---

## Tarefa 2: Papéis e competências

> Como a atividade é individual, todas as análises de papel foram realizadas pelo mesmo integrante, que também justifica a inclusão de cada papel na estrutura do LocalEats.

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|------------|-----------------|--------------------------------------------|-----------------------|------------------------------|
| Gabriel Lopes Soares | Responsável pelo produto (Product Owner) | Definir o que é valor para o usuário; escrever critérios de aceitação claros junto ao time; decidir prioridade de correção de defeitos; aceitar ou recusar a entrega com base nos critérios acordados. | Escrita de critérios de aceitação (formato de histórias), priorização por valor e risco, leitura de métricas de uso e de defeitos. | Comunicação clara, escuta do usuário, capacidade de negociação e de dizer "não" com justificativa, foco no problema e não na solução. |
| Gabriel Lopes Soares | Analista de sistemas / de negócio | Traduzir necessidades em requisitos verificáveis; revisar requisitos com o time antes do desenvolvimento; identificar necessidades implícitas (ex.: mensagens de erro e estados vazios). | Modelagem de requisitos, análise de fluxos alternativos e de exceção, noções de usabilidade e de regras de negócio. | Atenção a detalhes, pensamento crítico, colaboração com produto e desenvolvimento, clareza na escrita. |
| Gabriel Lopes Soares | Desenvolvedor | Implementar a funcionalidade já com testes unitários; revisar o código dos colegas; cobrir casos inválidos e de borda; corrigir defeitos com prioridade acordada; não "empurrar" o problema para o QA. | Linguagens e frameworks do LocalEats (front-end e API), testes unitários e de integração, versionamento com Git, revisão de código, depuração. | Responsabilidade pelo próprio trabalho, humildade para receber revisão, colaboração, comunicação técnica objetiva. |
| Gabriel Lopes Soares | QA / Analista de qualidade | Planejar e executar testes de sistema e de aceitação; manter o registro e o acompanhamento de defeitos; verificar se os critérios de "pronto" foram cumpridos; apoiar o time na definição de critérios e de práticas de teste. | Técnicas de teste (partição de equivalência, valores-limite, testes exploratórios), escrita de casos de teste, registro de defeitos com passos e evidências, automação básica de testes. | Ceticismo produtivo, organização, comunicação sem tom acusatório, pensamento crítico e foco no risco. |
| Gabriel Lopes Soares | DevOps | Garantir que a esteira de integração e entrega execute verificações automáticas antes da publicação; manter ambientes e dados de teste; tornar a publicação reversível e rastreável. | Pipelines de CI/CD, automação de build e testes, versionamento de artefatos, observabilidade e rollback. | Colaboração com desenvolvimento e QA, atenção a riscos operacionais, transparência sobre falhas na esteira. |
| Gabriel Lopes Soares | Liderança técnica | Definir os padrões técnicos do projeto (padrão de código, estratégia de testes, uso de branches); revisar decisões de arquitetura com foco em qualidade; aprovar a disponibilização de uma versão junto ao produto; remover impedimentos do time. | Arquitetura de software, revisão de código, estimativa de risco técnico, configuração de padrões e de ferramentas de análise estática. | Tomada de decisão, mentoria, mediação de conflitos, visão sistêmica e coerência entre discurso e prática. |

**Justificativa dos papéis escolhidos:** os seis papéis cobrem o caminho completo de uma funcionalidade no LocalEats — decisão de produto, requisito, código, verificação, entrega e padrão técnico. Sem o responsável pelo produto e o analista, os critérios de aceitação não existem; sem o DevOps e a liderança técnica, ninguém responde pela esteira e pela aprovação da versão, que são justamente os pontos frágeis relatados.

---

## Tarefa 3: Matriz de responsabilidades (RACI)

**Legenda:** R = Responsável pela execução · A = Aprovador (decisão final, único por atividade) · C = Consultado · I = Informado

| Atividade de qualidade | Produto (PO) | Analista | Desenvolvedor | QA | DevOps | Liderança técnica |
|------------------------|--------------|----------|---------------|----|--------|-------------------|
| Definir critérios de aceitação | A | R | C | C | I | C |
| Revisar requisitos | A | R | C | C | I | C |
| Implementar a funcionalidade | I | C | R | I | I | A |
| Revisar o código | I | I | R | C | I | A |
| Criar testes unitários | I | I | R | C | I | A |
| Planejar e executar testes do sistema | I | C | C | R | I | A |
| Registrar e acompanhar defeitos | C | I | C | R | I | A |
| Priorizar a correção dos defeitos | A | I | C | C | I | R |
| Aprovar a disponibilização da versão | C | I | I | R | R | A |

**Lacuna ou conflito encontrado:**

A atividade **"Registrar e acompanhar defeitos"** fica concentrada em um único papel: o QA é o único **R**, e ninguém mais tem responsabilidade real sobre o ciclo de vida do defeito. Ao mesmo tempo, **"Aprovar a disponibilização da versão"** concentra a decisão na liderança técnica, que também é **A** da implementação e da revisão de código — ou seja, o mesmo papel aprova o próprio trabalho.

**Consequência:**

Na primeira lacuna, se o QA estiver ausente, sobrecarregado ou de férias, os defeitos deixam de ser registrados e acompanhados, e o problema volta exatamente ao que foi relatado pela direção. Na segunda, existe conflito de interesse: a liderança técnica pode liberar uma versão com base na sua própria avaliação, sem uma verificação independente, o que enfraquece o controle e aumenta o risco de defeitos chegarem ao usuário. Uma correção simples é tornar o desenvolvedor **R** também pelo registro do defeito que corrige e incluir o produto como **C** na aprovação da versão, mantendo o QA como **R** da verificação final.

---

## Práticas recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---------------------|-------------------------------|-------------------|
| **Definition of Done (DoD) acordada e checada antes da entrega**, com itens objetivos: critérios de aceitação validados, testes unitários escritos, revisão de código aprovada, testes de sistema executados sem defeitos bloqueantes e evidência registrada. Revisão do DoD a cada sprint. | Critérios de "pronto" pouco claros e funcionalidades chegando com defeitos ao usuário; também reduz a ideia de que só o QA verifica, pois cada item do DoD tem dono. | Produto, Analista, Desenvolvedor, QA e Liderança técnica. |
| **Triagem de defeitos com registro único e prazo de decisão** (defect triage): todo defeito entra em um único local, com passos de reprodução, severidade e evidência; reunião curta semanal define prioridade e prazo, e o andamento é visível para todos. | Defeitos identificados mas não registrados ou acompanhados, e ausência de clareza sobre quem prioriza a correção. | QA (registra e organiza), Produto (prioriza), Liderança técnica (decide esforço), Desenvolvedor (corrige), DevOps (acompanha a esteira). |

---

## Uso de inteligência artificial

**Ferramenta utilizada:**
Muse Spark (Sider) como apoio à redação, à organização das tabelas e à revisão da coerência da matriz RACI.

**Como foi utilizada:**
Apoio para estruturar o documento conforme o modelo oficial da atividade, sugerir a distribuição inicial de responsabilidades na matriz RACI e redigir as descrições de papéis, competências e práticas. As decisões sobre quais papéis existem no LocalEats e qual é a lacuna principal foram definidas a partir das situações relatadas no contexto da atividade.

**Como as respostas foram verificadas:**
Conferência das regras da matriz (todo papel com pelo menos um R, um único A por atividade), leitura das situações relatadas pela direção para garantir que cada problema e cada prática estivessem ligados a um relato concreto, e revisão do texto quanto à coerência entre papéis, competências e responsabilidades. O conteúdo foi lido e é passível de explicação e defesa oral.
