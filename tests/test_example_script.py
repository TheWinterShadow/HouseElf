"""Tests for the example script."""

from houseelf.scripts.example_script import ExampleScript


def test_example_script_initialization():
    """Test that ExampleScript initializes correctly."""
    script = ExampleScript()
    assert script.name == "ExampleScript"


def test_example_script_run():
    """Test that ExampleScript runs successfully."""
    script = ExampleScript()
    result = script.run()
    assert result == "Example task completed successfully"


def test_example_script_execute():
    """Test that ExampleScript executes successfully."""
    script = ExampleScript()
    exit_code = script.execute()
    assert exit_code == 0
