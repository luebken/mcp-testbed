# MCP Testbed

A trivial application to test tool calling with multiple MCP servers. 

## Setup
```sh
uv venv
source .venv/bin/activate
uv pip install -e .

# run / debug
uv run server.py
npx @modelcontextprotocol/inspector uv run $(PWD)/server.py
```

# /Users/YOUR_USERNAME/Library/Application Support/Claude/claude_desktop_config.json
{
  "mcpServers": {
      "products": {
          "command": "uv",
          "args": [
              "--directory",
              "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-testbed/",
              "run",
              "server.py"
          ]
      }
  }
}

## Test

Queries:
* What products does Apple have?
* What were the orders from last week??
* How many people bought products from Apple last week?"

Ensure you use all the tools at your disposal.

