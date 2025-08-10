# Basic Python MCP Server + MCP Inspector

This example shows a minimal Python MCP server using the official Python SDK (FastMCP), along with instructions to run it with the MCP Inspector.

## Prerequisites
- Python 3.10+
- MCP Inspector installed (from modelcontextprotocol.io or GitHub releases)

## Files
- `server.py` — FastMCP server with tools: add, echo, system_info, fetch_url
- `lib.py` — pure functions used by server and tests
- `tests/run_tests.py` — simple assert-based tests
- `requirements.txt` / `pyproject.toml` — Python dependencies (mcp)

## Option A: Use virtualenv + pip (recommended here)
```bash
cd basic-python-mcp-server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run with MCP Inspector
```bash
mcp dev server.py
```

### Direct run (stdio)
```bash
python server.py
```

### Run tests
```bash
python tests/run_tests.py
```

## Option B: Use uv (if you have it installed)
```bash
cd basic-python-mcp-server
uv sync
uv run mcp dev server.py
```

## Claude Desktop config (optional)
macOS path: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "basic-python-mcp-server": {
      "command": "python",
      "args": ["/absolute/path/to/basic-python-mcp-server/server.py"]
    }
  }
}
```

Restart Claude Desktop after saving.

