import pandas as pd
import numpy as np

data = {
    'student': ['A', 'B', 'C', 'D', 'E'],
    'score': [85, np.nan, 90, np.nan, 75]
}
df = pd.DataFrame(data)

# 1. Calculá el promedio de 'score'
# 2. Rellená los NaNs con ese promedio
mean_score = None
df_filled = df.copy()
# Tu código aquí
mean_score = df_filled['score'].mean()
df_filled['score'] = df_filled['score'].fillna(mean_score)
print(df_filled)