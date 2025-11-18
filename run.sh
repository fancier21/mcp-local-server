#!/usr/bin/env bash
# MCP server launcher script with correct environment for Cloud Desktop

# Explicitly set PATH so uv can be found
export PATH=$PATH:/home/f/.local/bin

# Ensure the correct environment is inherited
# Log environment for debugging purposes to stderr
echo '{"status": "debug", "message": "Current environment variables:", "env":' "$(env)" '}' >&2

# Change to the directory of this script
cd "$(dirname "$0")" || {
  echo '{"jsonrpc": "2.0", "error": {"code": -32603, "message": "Failed to change directory"}, "id": null}' >&2
  exit 1
}

# Print the current directory after cd
echo '{"status": "debug", "message": "Changed to directory: $(pwd)"}' >&2

# Run the MCP server via uv
exec uv run main.py
