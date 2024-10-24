from dataclasses import dataclass

import numpy as np
from spellchecker import SpellChecker


@dataclass
class LexicalQuality:
    spellchecker: SpellChecker

    def calculate_lexical_quality_scores(self, texts: np.ndarray) -> np.ndarray:
        return np.vectorize(self.calculate_lexical_quality_score)(texts)

    def calculate_lexical_quality_score(text: str) -> float:
        return len(text)
