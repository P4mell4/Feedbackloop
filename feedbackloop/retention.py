"""Rotina genérica de retenção para registros com timestamp created_at."""
from datetime import datetime, timedelta, timezone
from typing import Iterable

def purge_expired(records: Iterable[dict], retention_days: int = 90,
                  now: datetime | None = None) -> list[dict]:
    if retention_days < 0:
        raise ValueError("retention_days não pode ser negativo")
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=retention_days)
    # Espera created_at como datetime timezone-aware. Registros sem data são
    # preservados para revisão, em vez de serem excluídos silenciosamente.
    kept = []
    for record in records:
        created_at = record.get("created_at")
        if not isinstance(created_at, datetime):
            kept.append(record)
        elif created_at.tzinfo is None:
            raise ValueError("created_at precisa ter fuso horário")
        elif created_at >= cutoff:
            kept.append(record)
    return kept
