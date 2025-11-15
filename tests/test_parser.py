from core.parser import SectionParser

def test_parser_loads_sections():
    parser = SectionParser("sections")
    result = parser.load_section("perfil")
    assert isinstance(result, str)
