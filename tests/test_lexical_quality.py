from cleanlab.lexical_quality import LexicalQuality


def test_correctly_spelled_text_gets_top_score():
    text = "Every word here is a real word"

    lexical_quality = LexicalQuality()

    assert lexical_quality._calculate_lexical_quality_score(text) == 1
