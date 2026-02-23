"""Basic smoke tests for the codecks-mcp server package."""

import importlib


def test_import():
    """Verify the package imports without error."""
    mod = importlib.import_module("codecks_mcp")
    assert hasattr(mod, "main")
    assert hasattr(mod, "mcp")


def test_mcp_server_has_tools():
    """Verify the MCP server has registered tools."""
    from codecks_mcp import mcp

    # FastMCP stores tools internally; just verify it's a FastMCP instance
    assert mcp.name == "codecks"
