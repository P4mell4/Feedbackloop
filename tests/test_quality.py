from feedbackloop.quality import accuracy, evaluate_classifications, summary_checklist

def test_avalia_acuracia_de_temas_e_sentimentos():
    gold = [
        {"tema": "Liderança", "sentimento": "negativo"},
        {"tema": "Comunicação", "sentimento": "positivo"},
    ]
    predicted = [
        {"tema": "Liderança", "sentimento": "negativo"},
        {"tema": "Outros", "sentimento": "positivo"},
    ]
    result = evaluate_classifications(gold, predicted)
    assert result["samples"] == 2
    assert result["theme_accuracy"] == 0.5
    assert result["sentiment_accuracy"] == 1.0

def test_acuracia_rejeita_tamanhos_diferentes():
    try:
        accuracy(["a"], [])
    except ValueError:
        pass
    else:
        raise AssertionError("Esperava ValueError")

def test_verifica_resumo_com_recomendacoes():
    result = summary_checklist(
        "A equipe relata sobrecarga. A comunicação pode melhorar. "
        "Recomenda-se revisar prioridades."
    )
    assert result["non_empty"]
    assert result["has_recommendation_marker"]
    assert result["within_3_to_5_sentences"]
