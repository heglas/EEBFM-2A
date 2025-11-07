import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
categorias = {
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [15, 30, 40, 10]
}
df_cat = pd.DataFrame(categorias)

# Gráfico de pizza
df_cat.set_index('Categoria').plot.pie(y='Valores', autopct='%1.1f%%', title='Distribuição de Categorias')
plt.ylabel('')
plt.tight_layout()
plt.show()