import numpy as np
from spellchecker import SpellChecker


class LexicalQuality:
    def __init__(self, spellchecker=None):
        if spellchecker == None:
            spellchecker = SpellChecker()
        self.spellchecker = spellchecker

    def calculate_lexical_quality_scores(self, texts: np.ndarray) -> np.ndarray:
        return np.vectorize(self._calculate_lexical_quality_score)(texts)

    def _calculate_lexical_quality_score(self, text: str) -> float:
        """
        Currently this only takes into account spelling mistakes.
        TODO: take into account grammar correctness, readability, and coherence.

        Given a sentence, this gives a score between 0 and 1 (1 if every
        word is spelt correctly and 0 if every word is spelt incorrectly).
        """

        words = text.split(" ")
        misspelled_words = self.spellchecker.unknown(words)

        return (len(words) - len(misspelled_words)) / len(words)
