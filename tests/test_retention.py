from datetime import datetime, timedelta, timezone
from feedbackloop.retention import purge_expired

def test_remove_vencidos_e_preserva_registros_no_prazo():
    now = datetime(2026, 10, 19, tzinfo=timezone.utc)
    records = [
        {"id": "antigo", "created_at": now - timedelta(days=91)},
        {"id": "recente", "created_at": now - timedelta(days=10)},
    ]
    kept = purge_expired(records, retention_days=90, now=now)
    assert [item["id"] for item in kept] == ["recente"]

def test_preserva_registro_sem_data_para_revisao():
    now = datetime(2026, 10, 19, tzinfo=timezone.utc)
    records = [{"id": "sem-data"}]
    assert purge_expired(records, now=now) == records
