# Interface fina com o LLM.
# (Rafael)
#
# A graça aqui é que TODO o resto do código só conhece o método `.completar()`.
# Isso deixa o pipeline testável sem chamar a API de verdade: nos testes a gente
# passa um cliente fake (um dublê) que devolve respostas fixas. Ver tests/.
#
# Hoje só tem implementação pra OpenAI. Pra trocar pro Claude
# (um modelo Haiku da Anthropic) seria mais ou menos:
#
#     from anthropic import Anthropic
#     resp = Anthropic().messages.create(model="<modelo-haiku-da-anthropic>", ...)
#
# ...mas não cheguei a fazer. Fica de TODO pra quem assumir.

import os


class ClienteLLM:
    def __init__(self, modelo: str | None = None):
        from openai import OpenAI

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "Configuração de API ausente."
            )

        self.modelo = (
            modelo or os.getenv("OPENAI_MODEL", "gpt-5.4-mini")
        )
        self._client = OpenAI(api_key=api_key)