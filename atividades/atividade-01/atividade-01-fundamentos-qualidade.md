# Atividade 1 — Fundamentos e Caracteristicas da Qualidade no LocalEats

## 1. Identificacao

**Unidade Curricular:** Qualidade de Software
**Metodologia:** Problem-Based Learning (PBL)
**Projeto:** LocalEats
**Modalidade:** Individual
**Data:** 12/11/2026

### Integrantes
## Tarefa 1: Fundamentos da qualidade

| Tipo | Necessidade | Interessado | Consequencia se nao for atendida |
|------|-------------|-------------|----------------------------------|
| Explicita | Criar conta e entrar no sistema com e-mail e senha. | Usuario que deseja usar o LocalEats | O usuario nao consegue acessar as areas autenticadas (explorar, favoritar, pedir). |
| Explicita | Pesquisar e filtrar restaurantes por especialidade (ex.: Italiana, Japonesa) ou localizacao. | Usuario que busca um restaurante | O usuario nao encontra o que procura e abandona a aplicacao. |
| Implicita | Os dados de login e da conta devem estar protegidos e a sessao deve ser mantida com seguranca. | Usuario / Negocio | Vazamento de credenciais, acesso indevido a conta e perda de confianca no sistema. |
| Implicita | A busca e os filtros devem responde## Tarefa 2: Exploracao da aplicacao

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidencia |
|------------|----------------|---------------------|---------------------|-----------|
| Gabriel | Explorar restaurantes (busca + filtro## Tarefa 3: Requisitos e caracteristicas de qualidade

| Integrante | Requisito de Qualidade | Caracteristica | Justificativa | Como avaliar |
|------------|------------------------|----------------|---------------|--------------|
| Gabriel | Ao buscar ou filtrar por uma especialidade existente (ex.: Italiana), o LocalEats deve exibir apenas restaurantes daquela especialidade, e quando nao houver resultados deve exibir mensagem orientativa. | Adequacao Funcional — Correcao Funcional (ISO/IEC 25010) | A busca/filtro deve retornar o conjunto correto de restaurantes. Buscar Italiana retornou zero resultados mesmo havendo restaurantes italianos: falha de correcao, nao apenas de estetica ou rapidez. | Observar e contar: para especialidades existentes, registrar quantas retornam o conjunto correto; verificar se a mensagem sem resultados informa a especialidade e sugere alternativa. |

---

## Uso de inteligencia artificial

**Ferramenta utilizada:** Muse Spark (Sider) como apoio a redacao e organizacao.

**Como foi utilizada:** Apoio para estruturar o documento conforme o modelo, relacionar o observado a ISO/IEC 25010 e gerar os arquivos.

**Como as respostas foram verificadas:** Exploracao manual do LocalEats (conta de teste, busca e filtro por especialidade) e revisao do texto antes da entrega. Sem dados pessoais.
 por especialidade) | Uso esperado: acessei a tela Explorar logado e observei a listagem. Uso alternativo: digitei Italiana no campo de busca e cliquei em Buscar; depois cliquei no filtro Italiana. | Com a busca por Italiana e com o filtro Italiana, a grade exibiu a mensagem Nenhum restaurante encontrado, embora a listagem inicial apresentasse restaurantes dessa especialidade. O campo de busca filtra por localizacao, nao por culinaria, o que confunde o usuario. | [ver evidencia](./evidencias/gabriel-explorar-filtro-italiana-sem-resultado.jpg) |

---

r de forma rapida e compreensivel, mesmo quando nao houver resultados. | Usuario | Frustracao e percepcao de sistema quebrado (ex.: mensagem generica sem orientacao do que fazer). |

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade?**

Sim. Mesmo com login, busca e filtros implementados, a qualidade e baixa se necessidades implicitas nao forem atendidas. Por exemplo, se a busca demorar ou exibir apenas Nenhum restaurante encontrado sem orientar o usuario, a funcionalidade existe, mas a experiencia e ruim e o usuario considera o sistema inadequado.

---


| Nome | Usuario no GitHub |
|------|-------------------|
| Gabriel | @gabrielllss |

**Elemento de Competencia:** Compreender os fundamentos de qualidade de software e sua aplicacao no desenvolvimento de sistemas.

**Aplicacao:** https://local-eats-unisenac.vercel.app/

---

