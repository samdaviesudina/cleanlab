from cleanlab.lexical_quality import LexicalQuality


def test_when_text_is_correctly_spelled_it_gets_top_score():
    text = "Every word here is a real word"

    lexical_quality = LexicalQuality()

    assert lexical_quality._calculate_lexical_quality_score(text) == 1


def test_when_every_word_is_wrong_it_gets_lowest_score():
    text = "Evry wuhd heea iz nott reeyal"

    lexical_quality = LexicalQuality()

    assert lexical_quality._calculate_lexical_quality_score(text) == 0


def test_higher_scores_correspond_to_better_text():
    better_text = "This bit of text is pretty good, though it has one misteak."
    worse_text = "This bit of tekst is prettie gud, though it haz many misteaks."

    lexical_quality = LexicalQuality()
    better_text_score = lexical_quality._calculate_lexical_quality_score(better_text)
    worse_text_score = lexical_quality._calculate_lexical_quality_score(worse_text)

    assert 0 < worse_text_score
    assert worse_text_score < better_text_score
    assert better_text_score < 1
