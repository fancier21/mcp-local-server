## Context Servers Configuration  

# Local MCP Server - Zed configuration

```json
{
  "context_servers": {
    "mcp-local-server": {
      "enabled": true,
      "source": "custom",
      "command": "uv",
      // "command": "/home/f/.local/bin/uv",
      "args": ["run", "/home/f/Dev/MCPs/mcp-local-server/main.py"],
      "env": {}
    }
  }
}
```

# Local MCP Server - Zed configuration with run script

```json
{
  "context_servers": {
    "mcp-local-server": {
      "enabled": true,
      "source": "custom",
      "command": "/bin/bash",
      "args": ["/home/f/Dev/MCPs/mcp-local-server/run.sh"],
      "env": {}
    }
  },
```


# Local MCP Server - Cloude Desktop / Cursor configuration with run script

```json
{
  "mcpServers": {
    "mcp-local-server": {
      "command": "/home/f/Dev/MCPs/mcp-local-server/run.sh",
      "args": [],
      "env": {}
    }
  }
}
```
