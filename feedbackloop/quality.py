"""Métricas básicas para comparar previsões com rótulos revisados por humanos."""
def accuracy(expected: list[str], predicted: list[str]) -> float:
    if len(expected) != len(predicted):
        raise ValueError("expected e predicted precisam ter o mesmo tamanho")
    if not expected:
        return 0.0
    return sum(a == b for a, b in zip(expected, predicted)) / len(expected)

def evaluate_classifications(gold: list[dict], predicted: list[dict]) -> dict:
    if len(gold) != len(predicted):
        raise ValueError("gold e predicted precisam ter o mesmo tamanho")
    if not gold:
        return {"samples": 0, "theme_accuracy": 0.0, "sentiment_accuracy": 0.0}
    return {
        "samples": len(gold),
        "theme_accuracy": accuracy([x["tema"] for x in gold], [x["tema"] for x in predicted]),
        "sentiment_accuracy": accuracy([x["sentimento"] for x in gold], [x["sentimento"] for x in predicted]),
    }

def summary_checklist(summary: str) -> dict:
    sentences = [s.strip() for s in summary.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    return {
        "non_empty": bool(summary.strip()),
        "has_recommendation_marker": any(word in summary.casefold() for word in ("ação", "recomend", "recomenda")),
        "sentence_count": len(sentences),
        "within_3_to_5_sentences": 3 <= len(sentences) <= 5,
    }
