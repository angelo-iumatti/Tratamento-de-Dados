# Bloco 01 – Saúde dos Dados 🩺

### Objetivo
Validar consistência dos arquivos operacionais (OP01‑OP17) que alimentam os painéis da GIO / Arsae‑MG.

### Passo a passo
1. Gerar arquivo‑teste **OP01_202506.csv** (15 linhas, erros intencionais).  
2. Executar `validation.py` → cria **erros_validacao.csv** com detalhes.  
3. Registrar inconsistências na aba **Log** de `Checklist_Validação.xlsx`.  
4. Corrigir o CSV e repetir até obter relatório vazio.

### Scripts
| Arquivo | Função |
|---------|--------|
| `validation.py` | Checa nulos, duplicatas, perda > 100 %, volume negativo |

### Resultado
Relatório vazio = arquivo pronto para ingestão (ETL).

### Próximos passos
Automatizar execução no Power Automate Desktop e salvar logs no banco.