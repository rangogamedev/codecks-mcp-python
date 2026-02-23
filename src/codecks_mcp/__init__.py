"""Codecks MCP Server — standalone package.

Re-exports the MCP server from codecks-cli for standalone installation.
Install: pip install codecks-mcp
Run:     codecks-mcp  OR  python -m codecks_mcp
"""

from codecks_cli.mcp_server import main, mcp

__all__ = ["main", "mcp"]
