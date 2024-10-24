import pandas as pd
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def calculate_lexical_quality_scores(texts: np.ndarray) -> pd.DataFrame:
    vectorized_sigmoid = np.vectorize(sigmoid)
    vectorized_lexical_quality_score_calculation = np.vectorize(calculate_lexical_quality_score)

    return vectorized_sigmoid(vectorized_lexical_quality_score_calculation(texts))


def calculate_lexical_quality_score(text: str) -> float:
    return len(text)
