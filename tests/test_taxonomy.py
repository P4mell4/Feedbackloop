from feedbackloop.taxonomy import TEMAS, normalizar_tema

def test_taxonomia_possui_dez_categorias():
    assert len(TEMAS) == 10
    assert "Outros" in TEMAS

def test_tema_canonico_permanece_igual():
    assert normalizar_tema("Liderança") == "Liderança"

def test_alias_salario():
    assert normalizar_tema("salário") == "Remuneração e benefícios"

def test_alias_home_office():
    assert normalizar_tema("home office") == "Trabalho remoto/híbrido"

def test_tema_desconhecido_vai_para_outros():
    assert normalizar_tema("Tema inventado") == "Outros"
