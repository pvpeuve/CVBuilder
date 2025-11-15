from core.builder import CVBuilder

def test_builder_merge():
    builder = CVBuilder()
    merged = builder.merge()
    assert isinstance(merged, str)
