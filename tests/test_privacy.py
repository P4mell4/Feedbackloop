from feedbackloop.privacy import anonymize_text

def test_remove_email():
    result = anonymize_text("Meu contato é maria@example.com")
    assert "maria@example.com" not in result.text
    assert "[EMAIL_REMOVIDO]" in result.text

def test_remove_cpf():
    result = anonymize_text("Meu CPF é 123.456.789-09")
    assert "123.456.789-09" not in result.text
    assert "[CPF_REMOVIDO]" in result.text

def test_remove_telefone():
    result = anonymize_text("Meu telefone é (11) 98765-4321")
    assert "98765-4321" not in result.text
    assert "[TELEFONE_REMOVIDO]" in result.text

def test_remove_url():
    result = anonymize_text("Meu perfil é https://example.com/perfil")
    assert "https://example.com/perfil" not in result.text
    assert "[URL_REMOVIDO]" in result.text

def test_remove_nome_declarado():
    result = anonymize_text("Meu nome é Ana Silva e trabalho no setor.")
    assert "Ana Silva" not in result.text
    assert "[NOME_REMOVIDO]" in result.text
