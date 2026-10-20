"""Taxonomia controlada de temas para classificação de respostas."""
import unicodedata

TEMAS = (
    "Carga de trabalho",
    "Liderança",
    "Remuneração e benefícios",
    "Reconhecimento e carreira",
    "Comunicação",
    "Ferramentas e processos",
    "Cultura e ambiente",
    "Trabalho remoto/híbrido",
    "Desenvolvimento e aprendizagem",
    "Outros",
)

def _key(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", (value or "").casefold())
    without_marks = "".join(c for c in normalized if not unicodedata.combining(c))
    return " ".join(without_marks.strip().split())

ALIASES = {
    "sobrecarga": "Carga de trabalho",
    "salario": "Remuneração e benefícios",
    "remuneracao": "Remuneração e benefícios",
    "salarios": "Remuneração e benefícios",
    "beneficios": "Remuneração e benefícios",
    "reconhecimento": "Reconhecimento e carreira",
    "carreira": "Reconhecimento e carreira",
    "ferramentas": "Ferramentas e processos",
    "processos": "Ferramentas e processos",
    "cultura": "Cultura e ambiente",
    "ambiente de trabalho": "Cultura e ambiente",
    "home office": "Trabalho remoto/híbrido",
    "trabalho remoto": "Trabalho remoto/híbrido",
    "hibrido": "Trabalho remoto/híbrido",
    "aprendizagem": "Desenvolvimento e aprendizagem",
    "treinamento": "Desenvolvimento e aprendizagem",
}

def normalizar_tema(tema: str) -> str:
    key = _key(tema)
    for canonical in TEMAS:
        if _key(canonical) == key:
            return canonical
    return ALIASES.get(key, "Outros")
