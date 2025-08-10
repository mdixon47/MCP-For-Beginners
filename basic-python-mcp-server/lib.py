from __future__ import annotations

import os
import platform
import sys
import urllib.request
import urllib.error


def add(a: int, b: int) -> int:
    return a + b


def echo(message: str = "Hello from Python MCP!") -> str:
    return message


def system_info() -> dict:
    return {
        "platform": platform.platform(),
        "python": sys.version.split()[0],
        "pid": os.getpid(),
    }


def fetch_url(url: str, timeout: float = 8.0) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "basic-python-mcp/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(2048 * 2)  # up to ~4KB
            return {
                "url": url,
                "status": getattr(resp, "status", None),
                "headers": dict(getattr(resp, "headers", {}).items()),
                "body_preview": body.decode(errors="replace"),
            }
    except urllib.error.HTTPError as e:
        return {"url": url, "status": e.code, "error": str(e)}
    except Exception as e:
        return {"url": url, "status": None, "error": str(e)}

