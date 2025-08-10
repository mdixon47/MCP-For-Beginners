#!/usr/bin/env python3
"""
Basic Python MCP Server (stdio) using the official Python SDK (FastMCP).

Tools:
- add(a:int, b:int) -> int
- echo(message:str) -> str

Run (Inspector dev mode):
  uv run mcp dev server.py

Direct run (stdio only):
  python server.py
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP, Context
from lib import (
    add as lib_add,
    echo as lib_echo,
    system_info as lib_system_info,
    fetch_url as lib_fetch_url,
)

mcp = FastMCP(name="basic-python-mcp-server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return lib_add(a, b)


@mcp.tool()
def echo(message: str = "Hello from Python MCP!") -> str:
    """Return the same message back to the caller."""
    return lib_echo(message)


@mcp.tool()
def system_info() -> dict:
    """Return basic system information (OS, Python version)."""
    return lib_system_info()


@mcp.tool()
def fetch_url(url: str, timeout: float = 8.0) -> dict:
    """Fetch a URL using Python stdlib and return status and first 2000 chars of body."""
    return lib_fetch_url(url, timeout)


if __name__ == "__main__":
    # Runs with stdio transport by default
    mcp.run()
