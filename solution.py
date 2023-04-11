import pandas as pd
import numpy as np
from statsmodels. stats.weightstats import ztest as ztest

chat_id = 224851402 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.1
    z, pvalue = ztest(x,  value=500, alternative='larger')
    return pvalue < alpha
