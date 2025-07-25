import pandas as pd
from pathlib import Path

ARQUIVO = Path("OP01_202506.csv")

# 1. Carregar
df = pd.read_csv(ARQUIVO)

# 2. Validações básicas
erros = []

# 2.1. Campos obrigatórios sem nulos
campos_obrig = ["municipio", "mes_referencia", "volume_produzido_m3"]
for c in campos_obrig:
    n_nulos = df[c].isna().sum()
    if n_nulos:
        erros.append(f"{c}: {n_nulos} nulos")

# 2.2. Duplicatas
duplicatas = df.duplicated(subset=["municipio", "mes_referencia"]).sum()
if duplicatas:
    erros.append(f"{duplicatas} linhas duplicadas")

# 2.3. Regras de negócio
if (df["perda_percentual"] > 100).any():
    erros.append("perda_percentual > 100% detectada")

if (df["volume_produzido_m3"] < 0).any():
    erros.append("volume negativo detectado")

# 3. Relatório
pd.Series(erros, name="erros").to_csv("erros_validacao.csv", index=False)
print("Validação concluída! Veja erros_validacao.csv")

# 4. Exportar DataFrame corrigido
df.to_csv("OP01_202506_corrigido.csv", index=False)
print("DataFrame corrigido exportado como OP01_202506_corrigido.csv")