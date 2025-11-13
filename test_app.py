import pytest
from extract_data import create_dict

def test_create_dict_output():
    df = create_dict("stockholm")
    assert "tid" in df.columns or "time" in df.columns
    assert "grad" in df.columns or "degree" in df.columns
    assert len(df) > 0
