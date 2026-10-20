"""Cache LRU em memória com TTL. As chaves armazenadas são hashes, não textos."""
from collections import OrderedDict
from dataclasses import dataclass
import hashlib
import json
import time
from typing import Callable, Any

@dataclass
class CacheStats:
    hits: int = 0
    misses: int = 0
    evictions: int = 0
    expirations: int = 0

class ClassificationCache:
    def __init__(self, ttl_seconds: int = 86400, max_entries: int = 500,
                 clock: Callable[[], float] = time.monotonic):
        if ttl_seconds <= 0:
            raise ValueError("ttl_seconds deve ser maior que zero")
        if max_entries <= 0:
            raise ValueError("max_entries deve ser maior que zero")
        self.ttl_seconds = ttl_seconds
        self.max_entries = max_entries
        self._clock = clock
        self._entries = OrderedDict()
        self.stats = CacheStats()

    @staticmethod
    def make_key(sanitized_text: str, model: str, prompt_version: str) -> str:
        payload = json.dumps(
            [sanitized_text, model, prompt_version],
            ensure_ascii=False, separators=(",", ":")
        ).encode("utf-8")
        return hashlib.sha256(payload).hexdigest()

    def get_or_compute(self, sanitized_text: str, model: str,
                       prompt_version: str, compute: Callable[[], Any]):
        key = self.make_key(sanitized_text, model, prompt_version)
        now = self._clock()
        entry = self._entries.get(key)
        if entry is not None:
            expires_at, value = entry
            if now < expires_at:
                self._entries.move_to_end(key)
                self.stats.hits += 1
                # evita que o chamador altere o objeto guardado no cache
                return value.copy() if isinstance(value, dict) else value
            del self._entries[key]
            self.stats.expirations += 1

        self.stats.misses += 1
        value = compute()
        stored = value.copy() if isinstance(value, dict) else value
        self._entries[key] = (now + self.ttl_seconds, stored)
        self._entries.move_to_end(key)
        while len(self._entries) > self.max_entries:
            self._entries.popitem(last=False)
            self.stats.evictions += 1
        return value.copy() if isinstance(value, dict) else value

    def clear(self):
        self._entries.clear()

    @property
    def size(self) -> int:
        return len(self._entries)
