# codecks-mcp (Python)

MCP server for [Codecks](https://codecks.io) project management. Exposes 38 tools for managing cards, decks, milestones, tags, and PM workflows via the [Model Context Protocol](https://modelcontextprotocol.io).

## Install

```bash
pip install codecks-mcp
```

## Run

```bash
# stdio transport (default)
codecks-mcp

# or as a module
python -m codecks_mcp
```

## Configuration

Create a `.env` file in your project root:

```env
CODECKS_TOKEN=your_session_cookie
CODECKS_ACCOUNT=your_account_slug
```

### Tokens

| Variable | Source | Expires |
|----------|--------|---------|
| `CODECKS_TOKEN` | Browser DevTools > Cookie `at` | Yes (refresh periodically) |
| `CODECKS_REPORT_TOKEN` | `codecks-cli generate-token` | No |
| `CODECKS_ACCESS_KEY` | Codecks settings | No |
| `CODECKS_USER_ID` | Auto-discovered if unset | N/A |

### Optional Settings

| Variable | Default | Description |
|----------|---------|-------------|
| `CODECKS_MCP_RESPONSE_MODE` | `legacy` | `legacy` or `envelope` response format |
| `CODECKS_HTTP_TIMEOUT_SECONDS` | `30` | Request timeout |
| `CODECKS_HTTP_MAX_RETRIES` | `2` | Retry count for idempotent requests |

## IDE Setup

### Claude Code

```json
{
  "mcpServers": {
    "codecks": {
      "command": "codecks-mcp",
      "args": []
    }
  }
}
```

### Cursor

```json
{
  "mcpServers": {
    "codecks": {
      "command": "codecks-mcp",
      "args": []
    }
  }
}
```

## Tools (38)

### Read (10)
`get_account`, `list_cards`, `get_card`, `list_decks`, `list_projects`, `list_milestones`, `list_tags`, `list_activity`, `pm_focus`, `standup`

### Hand (3)
`list_hand`, `add_to_hand`, `remove_from_hand`

### Mutation (8)
`create_card`, `update_cards`, `mark_done`, `mark_started`, `archive_card`, `unarchive_card`, `delete_card`, `scaffold_feature`, `split_features`

### Comments (5)
`create_comment`, `reply_comment`, `close_comment`, `reopen_comment`, `list_conversations`

### PM Session (3)
`get_pm_playbook`, `get_workflow_preferences`, `save_workflow_preferences`

### Planning (4)
`planning_init`, `planning_status`, `planning_update`, `planning_measure`

### Registry (2)
`get_tag_registry`, `get_lane_registry`

### Feedback (2)
`save_cli_feedback`, `get_cli_feedback`

## Security

- Prompt injection detection (6 regex patterns)
- `[USER_DATA]` boundary tagging on all user-authored content
- Input validation (length limits, control character stripping)
- UUID validation on all card IDs

## License

MIT
