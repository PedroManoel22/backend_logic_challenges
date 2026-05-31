# 🚀 Backend Logic Challenges (Python)

Este repositório foi desenvolvido com o objetivo de consolidar, treinar e demonstrar uma base sólida de lógica de programação, algoritmos e engenharia de software aplicados ao desenvolvimento Backend.

Ao invés de exercícios acadêmicos simples ou scripts isolados, o foco aqui é resolver **50 problemas do mundo real**. As soluções simulam regras de negócio complexas, arquitetura de sistemas, manipulação de dados em baixo nível e otimização de performance, refletindo os desafios enfrentados no dia a dia de sistemas corporativos em produção.

---

## 🛠️ Boas Práticas de Engenharia Aplicadas

Para garantir que o código atenda aos padrões exigidos pelo mercado de trabalho e por times de alta performance, todas as resoluções seguem rigorosamente as seguintes diretrizes:

*   **PEP 8 & Padrões Estéticos:** Código limpo, legível, com nomenclatura semântica de variáveis/funções e formatação profissional.
*   **Type Hinting Estrito:** Uso de tipagem estática nos argumentos e retornos de funções, garantindo segurança, documentação e fácil manutenção.
*   **Tratamento de Exceções Resiliente:** Tratamento robusto de erros e cenários de falha (*edge cases*), antecipando inputs inesperados.
*   **Estrutura de Pacotes Modular:** Organização limpa por pacotes e módulos Python, respeitando o princípio de responsabilidade única e evitando arquivos poluídos.
*   **Zero Dependências Externas:** Desafios resolvidos utilizando majoritariamente a *Standard Library* do Python, provando o domínio dos conceitos fundamentais por baixo dos panos das ferramentas.

---

## 📂 Estrutura do Repositório e Índice de Desafios

O projeto está estruturado em 5 grandes blocos estratégicos. Cada subpasta representa um pacote Python com suas respectivas resoluções:

### ⚙️ Bloco 1: Estruturas de Dados Puras e Algoritmos de Core Engine
*Foco em manipulação de dados brutos, lógica matemática e estruturas fundamentais.*
1. Validador de CPF/CNPJ Profissional (Algoritmo de dígitos verificadores)
2. Gerador de Payload de Pagamento (String Pix EMV Estático com CRC16)
3. Conversor de Notação Polonesa Inversa (RPN com estrutura de Pilha)
4. Filtro Avançado de Logs Gigantes (Busca Binária por intervalo de milissegundos)
5. Algoritmo de Rate Limiting (Implementação pura de Token Bucket por IP)
6. Diferença Profunda entre JSONs (Algoritmo Recursivo de Deep Diff)
7. Paginador de Resultados Manual (Cálculo de offset, limites e metadados)
8. Validador de Expressões Sintáticas (Checagem de símbolos balanceados via Pilha)
9. Sistema de Permissões Corporativas (Uso de Bitwise Masks / Máscara de Bits)
10. Gerador e Validador de Cupom de Desconto (Geração com Hash Checksum antifraude)

### 💼 Bloco 2: Regras de Negócio e Engenharia de Software Backend
*Simulação de lógica corporativa, motores financeiros e fluxos de e-commerce.*

11. Motor de Amortização Financeira (Cálculo de Tabelas SAC e Price)
12. Motor de Checkout com Descontos Cumulativos e Progressivos
13. Agendador de Consultas/Eventos sem Sobreposição de Horários
14. Motor de Matchmaking de Vagas de Emprego (Cálculo de Score de Compatibilidade)
15. Conversor de Moedas Multi-atendida com Histórico de Cotações Diárias
16. Validador de Senhas Fortes (Lógica posicional e RegEx com relatório de falhas)
17. Cálculo de Frete Logístico por Cubagem e Distância (Regras de e-commerce)
18. Pipeline de Sanitização e Limpeza de Dados de Cadastro (*Data Cleaning*)
19. Sistema de Pontuação de Fidelidade e Milhas com Multiplicadores por Categoria
20. Gerenciador de Status de Pedido (Máquina de estados manual / *State Pattern*)

### 🗄️ Bloco 3: Arquivos, Parsers e Persistência de Dados (I/O)
*Leitura, escrita, transformação de arquivos e simulação de armazenamento.*

21. Parser Manual de Arquivos CSV (Conversão para dicionários sem a biblioteca `csv`)
22. Banco de Dados Key-Value Baseado em Arquivo Textual (Simulador de Redis)
23. Parser de XML de Nota Fiscal Eletrônica (NF-e) para JSON Estruturado
24. Sistema de Migrations Manual para Arquivos JSON
25. Compactador e Descompactador de Texto (Algoritmo Run-Length Encoding - RLE)
26. Gerenciador de Configurações `.env` Customizado (Leitor e injetor de variáveis)
27. Exportador de Relatórios Consolidados em Formato Markdown
28. Sistema de Auditoria de Arquivos (Geração de logs de histórico de alterações)
29. Validador de Schema de JSON Manual (Checagem de tipos e obrigatoriedade)
30. Rotacionador Automático de Arquivos de Log por Limite de Tamanho

### 🌐 Bloco 4: Concorrência, Assincronismo e Redes
*Gerenciamento de recursos, esperas de rede, paralelismo e resiliência.*

31. Simulador de Pooling de Conexões de Banco de Dados com Timeout
32. Fila de Mensagens Assíncronas Em Memória (Padrão Produtor-Consumidor)
33. Simulador de Requisições HTTP com Retentativas (*Exponential Backoff*)
34. Agrupador de Requisições para Processamento em Lote (*Batch Processing*)
35. Implementação de Circuit Breaker Pattern para Proteção de APIs
36. Parser Manual de Query Strings de URL para Dicionários Tipados
37. Simulador de Upload de Arquivos em Pedaços (Validação de Multipart Upload)
38. Cache In-Memory com Tempo de Expiração (Mecanismo de TTL - Time to Live)
39. Validador de Cabeçalhos HTTP de Segurança (OWASP-driven)
40. Processador Paralelo Multicore de Tarefas Simuladas (`concurrent.futures`)

### 📐 Bloco 5: Desafios Avançados de Arquitetura e Engenharia Reversa
*Estruturas de dados avançadas, grafos, segurança e engines complexas.*

41. Motor de Busca Textual Simples com Índice Invertido (*Inverted Index*)
42. Interpretador Genérico de Máquina de Estado para Workflows por Dicionário
43. Gerenciador de Dependências de Tarefas (Ordenação Topológica usando Grafos/DAG)
44. Algoritmo de Criptografia Manual Baseado em Cifra de Chave Alternada
45. Simulador de Estrutura de Blockchain (Blocos encadeados por Hash SHA-256)
46. Alocador Dinâmico de Recursos de Servidor (Algoritmo da Mochila Adaptado)
47. Sintetizador e Reconstrutor de Histórico de Saldo Bancário Retroativo
48. Engine de Validação Dinâmica de Regras Textuais (*Expression Evaluator*)
49. Sistema de Desfazer e Refazer Operações (Padrão *Command* com Pilhas Undo/Redo)
50. Sistema de Rotas e Matcher de URL Dinâmico (Core Engine de Framework Web)

---

## 🚀 Como Executar e Testar os Desafios

Cada desafio foi desenvolvido como um módulo isolado e autoexecutável. Na base de cada arquivo, há uma seção `if __name__ == "__main__":` contendo asserções (`assert`) e casos de teste que validam o comportamento do algoritmo.

Para executar qualquer um dos desafios, navegue até a raiz do projeto e execute o módulo utilizando o interpretador do Python (recomendado Python 3.10 ou superior):

```bash
# Exemplo: Executando o desafio 01 do Bloco 1
python -m bloco_01_core_engine.desafio01_validador_cpf
