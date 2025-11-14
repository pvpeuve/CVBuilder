from core.builder import CVBuilder
from core.parser import SectionParser

def test_parser_loads_sections():
    parser = SectionParser("sections")
    result = parser.load_section("perfil")
    assert isinstance(result, str)

def test_builder_merges():
    builder = CVBuilder()
    merged = builder.merge()
    assert isinstance(merged, str)
