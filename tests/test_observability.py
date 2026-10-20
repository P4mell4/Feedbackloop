from feedbackloop.observability import Observability

def test_registra_latencia_e_percentis():
    obs = Observability()
    for value in (1, 2, 3, 4, 5):
        obs.record(value)
    snapshot = obs.snapshot()
    assert snapshot["requests"] == 5
    assert snapshot["latency_p50_seconds"] == 3
    assert snapshot["latency_p95_seconds"] == 5
    assert snapshot["latency_p99_seconds"] == 5

def test_conta_erros_e_calcula_taxa():
    obs = Observability(error_threshold=0.25)
    obs.record(1, success=True)
    obs.record(1, success=False)
    assert obs.errors == 1
    assert obs.error_rate == 0.5
    assert "error_rate" in obs.alert_events

def test_limite_de_latencia_registra_evento_de_alerta():
    obs = Observability(latency_threshold_seconds=2)
    obs.record(3, success=True)
    assert "latency" in obs.alert_events
    assert obs.alert_destination == "console/teste"
