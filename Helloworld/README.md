### Environment Setup
1. Install Requirement: Python, NPM, Node, UV, VSCode, Claude Desktop
2. Create Project
`uv init`
3. Create Virtual Environment
`uv venv`

4. Activate Virtual environment
`.venv\Scripts\activate`
5. Install MCP CLI Dependency
`uv add mcp[cli]`

### Useful command for project

1. Run Inspector
`mcp dev weather.py`

2. Run Server locally
`uv run weather.py`

3. Run Claude Desktop: File > Setting > Developer > Edit Config: open and edit file 'claude_desktop_config.json' then add this:
```json
{
  "mcpServers": {
	  "weather": {
		  "command": "uv",
		  "args": [
			"--directory",
			"D:\\workspace\\learn_mcp\\Helloworld",
			"run",
			"weather.py"
		  ]
	  }
  }
}
```

4. Install Automatically to claude desktop. will add to claude config file automatically
`mcp install weather.py`