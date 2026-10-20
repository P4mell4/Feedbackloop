"""Primitivas simples de métricas; não enviam alertas para serviços externos."""
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Observability:
    error_threshold: float = 0.05
    latency_threshold_seconds: float = 10.0
    alert_destination: str = "console/teste"
    latencies: list[float] = field(default_factory=list)
    requests: int = 0
    errors: int = 0
    alert_events: list[str] = field(default_factory=list)

    def record(self, duration_seconds: float, success: bool = True) -> None:
        self.requests += 1
        self.latencies.append(max(0.0, float(duration_seconds)))
        if not success:
            self.errors += 1
        if self.error_rate > self.error_threshold:
            self.alert_events.append("error_rate")
        if duration_seconds > self.latency_threshold_seconds:
            self.alert_events.append("latency")

    @property
    def error_rate(self) -> float:
        return self.errors / self.requests if self.requests else 0.0

    def percentile(self, p: float) -> Optional[float]:
        if not self.latencies:
            return None
        if not 0 <= p <= 100:
            raise ValueError("percentil deve estar entre 0 e 100")
        ordered = sorted(self.latencies)
        # nearest-rank: rank = ceil(p*n/100), com mínimo 1
        import math
        rank = max(1, math.ceil(p / 100 * len(ordered)))
        return ordered[rank - 1]

    def snapshot(self) -> dict:
        return {
            "requests": self.requests,
            "errors": self.errors,
            "error_rate": self.error_rate,
            "latency_p50_seconds": self.percentile(50),
            "latency_p95_seconds": self.percentile(95),
            "latency_p99_seconds": self.percentile(99),
            "alert_events": list(self.alert_events),
        }
