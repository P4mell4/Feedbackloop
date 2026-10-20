"""Filtro inicial de dados pessoais. Não garante anonimização completa."""
import re
from dataclasses import dataclass

@dataclass(frozen=True)
class PrivacyResult:
    text: str
    replacements: int

PATTERNS = [
    ("CPF", re.compile(r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b")),
    ("EMAIL", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)),
    ("URL", re.compile(r"https?://[^\s\"'<>]+|www\.[^\s\"'<>]+", re.I)),
    ("TELEFONE", re.compile(
        r"(?<!\d)(?:\+?55\s*)?(?:\(?\d{2}\)?\s*)?9?\d{4}[-\s]?\d{4}(?!\d)"
    )),
]
# Heurística: cobre nomes explicitamente introduzidos e tratamentos.
# Não é reconhecimento de entidades nomeadas completo.
NAME_PATTERNS = [
    re.compile(
        r"\b(?:meu nome é|me chamo|nome:)\s+"
        r"([A-ZÁÀÂÃÉÊÍÓÔÕÚÇ][a-záàâãéêíóôõúç]+"
        r"(?:\s+[A-ZÁÀÂÃÉÊÍÓÔÕÚÇ][a-záàâãéêíóôõúç]+){0,2})",
        re.I,
    ),
    re.compile(
        r"\b(?:Sr\.?|Sra\.?|Dr\.?|Dra\.?)\s+"
        r"[A-ZÁÀÂÃÉÊÍÓÔÕÚÇ][a-záàâãéêíóôõúç]+"
        r"(?:\s+[A-ZÁÀÂÃÉÊÍÓÔÕÚÇ][a-záàâãéêíóôõúç]+)?",
        re.I,
    ),
]

def anonymize_text(text: str) -> PrivacyResult:
    sanitized = text or ""
    total = 0
    for label, pattern in PATTERNS:
        sanitized, count = pattern.subn(f"[{label}_REMOVIDO]", sanitized)
        total += count
    for pattern in NAME_PATTERNS:
        sanitized, count = pattern.subn(
            lambda match: match.group(0).split()[:3][0] + " [NOME_REMOVIDO]"
            if match.group(0).lower().startswith(("meu nome é", "me chamo", "nome:"))
            else "[NOME_REMOVIDO]",
            sanitized,
        )
        total += count
    return PrivacyResult(text=sanitized, replacements=total)
