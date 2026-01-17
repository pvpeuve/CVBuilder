from core.builder import build

def test_builder_merge():
    builder = build()
    merged = builder.merge()
    assert isinstance(merged, str)
