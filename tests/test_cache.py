from feedbackloop.cache import ClassificationCache
from feedbackloop.pipeline import classificar_resposta
from feedbackloop.privacy import anonymize_text
from test_pipeline import ClienteFake

class FakeClock:
    def __init__(self):
        self.value = 100.0
    def __call__(self):
        return self.value
    def advance(self, seconds):
        self.value += seconds

def classify_with_cache(client, response, cache, model="modelo-teste", prompt_version="classificacao-v1"):
    safe_text = anonymize_text(response).text
    return cache.get_or_compute(
        safe_text, model, prompt_version,
        lambda: classificar_resposta(client, safe_text)
    )

def test_primeira_analise_chama_cliente_uma_vez():
    client = ClienteFake()
    cache = ClassificationCache(ttl_seconds=60)
    classify_with_cache(client, "Resposta única", cache)
    assert client.chamadas == 1
    assert cache.stats.misses == 1
    assert cache.stats.hits == 0

def test_repeticao_usa_cache_sem_nova_chamada():
    client = ClienteFake()
    cache = ClassificationCache(ttl_seconds=60)
    classify_with_cache(client, "Resposta repetida", cache)
    classify_with_cache(client, "Resposta repetida", cache)
    assert client.chamadas == 1
    assert cache.stats.hits == 1

def test_resposta_diferente_faz_nova_chamada():
    client = ClienteFake()
    cache = ClassificationCache(ttl_seconds=60)
    classify_with_cache(client, "Resposta A", cache)
    classify_with_cache(client, "Resposta B", cache)
    assert client.chamadas == 2

def test_expiracao_faz_nova_chamada():
    clock = FakeClock()
    client = ClienteFake()
    cache = ClassificationCache(ttl_seconds=5, clock=clock)
    classify_with_cache(client, "Resposta com TTL", cache)
    clock.advance(6)
    classify_with_cache(client, "Resposta com TTL", cache)
    assert client.chamadas == 2
    assert cache.stats.expirations == 1

def test_textos_equivalentes_apos_privacidade_compartilham_cache():
    client = ClienteFake()
    cache = ClassificationCache(ttl_seconds=60)
    classify_with_cache(client, "Contato maria@example.com", cache)
    classify_with_cache(client, "Contato joao@example.com", cache)
    # Ambos viram "Contato [EMAIL_REMOVIDO]" antes de gerar a chave.
    assert client.chamadas == 1
    assert cache.stats.hits == 1

def test_chave_nao_contem_texto_original():
    secret = "maria@example.com"
    key = ClassificationCache.make_key(secret, "modelo", "v1")
    assert secret not in key
    assert len(key) == 64
