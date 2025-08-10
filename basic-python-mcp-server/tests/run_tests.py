import os
import sys
from importlib import import_module

# Ensure the project root is on sys.path so we can import lib.py
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Import the pure functions from lib.py to avoid requiring mcp package for tests
lib = import_module("lib")


def test_add():
    assert lib.add(2, 3) == 5
    assert lib.add(-1, 1) == 0


def test_echo():
    assert lib.echo("hi") == "hi"
    assert isinstance(lib.echo(), str)


def test_system_info():
    info = lib.system_info()
    assert isinstance(info, dict)
    assert "platform" in info and "python" in info


def test_fetch_url():
    # Basic smoke test against a public URL
    result = lib.fetch_url("https://example.com")
    assert isinstance(result, dict)
    assert result.get("url") == "https://example.com"
    # status may be None if network restrictions, so just ensure keys exist
    assert "status" in result and "body_preview" in result


if __name__ == "__main__":
    failures = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"✓ {name} passed")
            except AssertionError as e:
                failures += 1
                print(f"✗ {name} failed: {e}")
            except Exception as e:
                failures += 1
                print(f"✗ {name} error: {e}")
    sys.exit(1 if failures else 0)
