# 🚀 Backend Logic Challenges (Python)

Este repositório foi desenvolvido com o objetivo de consolidar, treinar e demonstrar uma base sólida de lógica de programação, algoritmos e engenharia de software aplicados ao desenvolvimento Backend.

Ao invés de exercícios acadêmicos simples ou scripts isolados, o foco aqui é resolver **50 problemas do mundo real**. O grande diferencial deste projeto é que **cada desafio possui duas resoluções independentes**:

1. 🐍 **Abordagem Nativa (Pure Python):** Implementada do zero utilizando majoritariamente a *Standard Library*. Mostra o domínio dos conceitos fundamentais, lógica pura e estruturas de dados por baixo dos panos.
2. 📦 **Abordagem de Mercado (External Libraries):** Implementada utilizando os pacotes e frameworks mais consolidados do ecossistema moderno do Python (PIP). Focada em produtividade, performance industrial e boas práticas de mercado.

As soluções simulam regras de negócio complexas, arquitetura de sistemas, manipulação de dados em baixo nível e otimização de performance, refletindo os desafios enfrentados no dia a dia de sistemas corporativos em produção.

---

## 🛠️ Boas Práticas de Engenharia Aplicadas

Para garantir que o código atenda aos padrões exigidos pelo mercado de trabalho e por times de alta performance, todas as resoluções seguem rigorosamente as seguintes diretrizes:

* **PEP 8 & Padrões Estéticos:** Código limpo, legível, com nomenclatura semântica de variáveis/funções e formatação profissional.
* **Type Hinting Estrito:** Uso de tipagem estática nos argumentos e retornos de funções, garantindo segurança, documentação e fácil manutenção.
* **Tratamento de Exceções Resiliente:** Tratamento robusto de erros e cenários de falha (*edge cases*), antecipando inputs inesperados.
* **Estrutura de Pacotes Modular:** Organização limpa por pacotes e módulos Python, respeitando o princípio de responsabilidade única. Cada desafio possui sua própria **pasta**, dividida internamente entre as soluções `native.py` e `external.py`.

---

## 📂 Estrutura do Repositório e Índice de Desafios

O projeto está estruturado em 5 grandes blocos estratégicos. Cada subpasta representa um pacote Python contendo as duas variações de código:

### ⚙️ Bloco 1: Estruturas de Dados Puras e Algoritmos de Core Engine
*Comparação entre algoritmos manuais estruturados e pacotes de validação/parsing otimizados.*
1. **Validador de CPF/CNPJ Profissional:** Algoritmo de dígitos verificadores manual vs. `validate-docbr`.
2. **Gerador de Payload de Pagamento:** String Pix EMV Estático com CRC16 manual vs. `pix-qrcode-api` / bibliotecas de automação Pix.
3. **Conversor de Notação Polonesa Inversa:** RPN com estrutura de Pilha pura vs. uso de parsers abstratos.
4. **Filtro Avançado de Logs Gigantes:** Busca Binária manual por intervalo de milissegundos vs. indexação com `Pandas`/`Polars`.
5. **Algoritmo de Rate Limiting:** Implementação pura de Token Bucket por IP vs. `limits`.
6. **Diferença Profunda entre JSONs:** Algoritmo Recursivo de Deep Diff vs. `deepdiff`.
7. **Paginador de Resultados Manual:** Cálculo de offset, limites e metadados puro vs. paginação com `SQLAlchemy` / `Pydantic`.
8. **Validador de Expressões Sintáticas:** Checagem de símbolos balanceados via Pilha vs. parsers baseados em `Lark-parser`.
9. **Sistema de Permissões Corporativas:** Uso de Bitwise Masks puro vs. gerenciamento com bibliotecas de RBAC como `Casbin`.
10. **Gerador e Validador de Cupom de Desconto:** Hash Checksum antifraude nativo com `hashlib` vs. criptografia com `cryptography` / `PyJWT`.

### 💼 Bloco 2: Regras de Negócio e Engenharia de Software Backend
*Aplicações financeiras e operacionais cruas vs. ecossistema de bibliotecas de negócio.*

11. **Motor de Amortização Financeira:** Cálculo manual de Tabelas SAC e Price vs. uso de `numpy-financial`.
12. **Motor de Checkout com Descontos Cumulativos:** Lógica condicional pura vs. engines de regras como `business-rules`.
13. **Agendador de Consultas sem Sobreposição:** Manipulação manual de `datetime` vs. engines de intervalo como `croniter` ou `pydantic-extra-types`.
14. **Motor de Matchmaking de Vagas de Emprego:** Cálculo manual de Score de Compatibilidade vs. distância vetorial e similaridade com `scikit-learn`.
15. **Conversor de Moedas Multi-atendida:** Cache e cálculo de cotações manuais vs. integração via `requests` com a API `ExchangeRate`.
16. **Validador de Senhas Fortes:** Lógica posicional pura e RegEx vs. validações avançadas com `password-validator` / `zxcvbn`.
17. **Cálculo de Frete Logístico por Cubagem:** Fórmulas matemáticas manuais vs. geolocalização exata com `Geopy`.
18. **Pipeline de Sanitização de Cadastro:** Manipulação manual de strings vs. esquemas de validação estrita com `Pydantic`.
19. **Sistema de Pontuação de Fidelidade:** Máquina de cálculo com herança pura vs. frameworks de eventos e regras de fidelização.
20. **Gerenciador de Status de Pedido:** Máquina de estados estruturada (*State Pattern*) manual vs. `transitions`.

### 🗄️ Bloco 3: Arquivos, Parsers e Persistência de Dados (I/O)
*Desafios clássicos de manipulação de disco puristas vs. ferramentas industriais de dados.*

21. **Parser Manual de Arquivos CSV:** Conversão para dicionários sem `import csv` vs. uso de `Pandas` / `csvkit`.
22. **Banco de Dados Key-Value Baseado em Arquivo:** Persistência em arquivo texto manual vs. `diskcache` / `TinyDB`.
23. **Parser de XML de Nota Fiscal Eletrônica (NF-e):** Parsing via `xml.etree` nativo vs. conversão direta com `xmltodict`.
24. **Sistema de Migrations Manual para JSON:** Controle de versão estruturado em disco vs. simuladores de migração inspirados em `Alembic`.
25. **Compactador e Descompactador de Texto:** Algoritmo Run-Length Encoding (RLE) puro vs. compactação via `bramses` / `zstandard`.
26. **Gerenciador de Configurações `.env` Customizado:** Leitor e injetor manual em `os.environ` vs. `python-dotenv`.
27. **Exportador de Relatórios em Markdown:** Criação de strings estruturadas pura vs. geração via templates com `Jinja2`.
28. **Sistema de Auditoria de Arquivos:** Geração de logs manual vs. monitoramento de eventos em tempo real com `watchdog`.
29. **Validador de Schema de JSON Manual:** Checagem de tipos pura via código vs. validação com `jsonschema`.
30. **Rotacionador Automático de Arquivos de Log:** Monitoramento e quebra de arquivos manual vs. `loguru`.

### 🌐 Bloco 4: Concorrência, Assincronismo e Redes
*Gerenciamento primitivo de rede e threads vs. clients assíncronos modernos de produção.*

31. **Pooling de Conexões com Timeout:** Estrutura de fila manual com threads vs. `DBUtils` / Pools nativos do `Psycopg2`.
32. **Fila de Mensagens Assíncronas Em Memória:** Padrão Produtor-Consumidor via `queue.Queue` vs. mensageria com `Celery` / `Kombu`.
33. **Simulador de Requisições com Exponential Backoff:** Loop manual com `time.sleep` vs. retentativas profissionais com `tenacity`.
34. **Agrupador de Requisições para Processamento em Lote:** Lógica de buffer temporal nativa vs. processamento em lote via `RxPy` (ReactiveX).
35. **Implementação de Circuit Breaker Pattern:** Flag e contadores de falha manuais vs. `pycircuitbreaker`.
36. **Parser Manual de Query Strings de URL:** Destruturação manual de strings vs. `yarl`.
37. **Simulador de Upload de Arquivos em Pedaços:** Divisão lógica de buffers de bytes vs. multipart chunking do `boto3` (AWS S3 style).
38. **Cache In-Memory com TTL:** Dicionário com timestamps manual vs. `cachetools`.
39. **Validador de Cabeçalhos HTTP de Segurança:** Dicionários de checagem manuais vs. validações automáticas com `Secure` (OWASP integration).
40. **Processador Paralelo Multicore de Tarefas:** `concurrent.futures` nativo vs. processamento distribuído com `Ray`.

### 📐 Bloco 5: Desafios Avançados de Arquitetura e Engenharia Reversa
*Lógica algorítmica profunda em Python puro vs. motores de computação de ponta.*

41. **Motor de Busca Textual Simples com Índice Invertido:** Algoritmo manual de tokenização e busca vs. indexação com `Whoosh`.
42. **Interpretador Genérico de Máquina de Estado para Workflows:** Engine orientada a dicionários vs. workflows robustos com `Temporalio` / `Airflow`.
43. **Gerenciador de Dependências de Tarefas:** Ordenação Topológica manual (Grafos/DAG) vs. resolução de dependências com `networkx`.
44. **Algoritmo de Criptografia Manual:** Cifra de chave alternada pura (XOR/Vigenère) vs. criptografia simétrica real com `PyNaCl`.
45. **Simulador de Estrutura de Blockchain:** Encadeamento manual por Hash SHA-256 vs. abstrações criptográficas industriais.
46. **Alocador Dinâmico de Recursos (Mochila Adaptado):** Programação Dinâmica manual vs. otimização linear com `scipy.optimize` / `PuLP`.
47. **Sintetizador de Histórico de Saldo Bancário Retroativo:** Algoritmo de reconstrução linear vs. manipulação de séries temporais com `Pandas`.
48. **Engine de Validação Dinâmica de Regras Textuais:** Avaliador baseado no `eval` seguro/AST nativo vs. `PyParsing`.
49. **Sistema de Desfazer e Refazer Operações (Undo/Redo):** Pilhas emparelhadas manuais (`Command Pattern`) vs. arquitetura de Event Sourcing com `eventsourcing`.
50. **Sistema de Rotas e Matcher de URL Dinâmico:** Core engine baseada em Regex estruturado vs. roteamento do `Werkzeug` (motor do Flask).

---

## 🚀 Como Executar e Testar os Desafios

Cada desafio foi desenvolvido como um módulo isolado. Na base de cada arquivo, há uma seção `if __name__ == "__main__":` contendo asserções (`assert`) e casos de teste que validam o comportamento de ambas as abordagens.

Para rodar e comparar os scripts, navegue até a raiz do projeto e passe o caminho do arquivo desejado para o interpretador do Python (requer Python 3.10 ou superior):

```bash
# Executando a versão purista (Apenas Python Nativo)
python -m bloco_01_core_engine.desafio01_validador_cpf.native

# Executando a versão de mercado (Utilizando as Bibliotecas Externas)
python -m bloco_01_core_engine.desafio01_validador_cpf.external
