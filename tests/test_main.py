import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import generate_summary

def test_generate_summary_not_empty():

    summary = generate_summary()

    assert not summary.empty

def test_summary_contains_type_column():

    summary = generate_summary()

    assert "type" in summary.columns

def test_summary_contains_count_column():

    summary = generate_summary()

    assert "count" in summary.columns