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

### VSCode Editor Problem
In some case, VSCode Editor did not recognize libraries installed on venv. It can be fixed by selecting the correct Python Interpreter from venv folder. Open the command pallete (Ctrl + Shift + P). Type 'Python: Select Interpreter' or similar with it. Click it and there will be dropdown for the right python interpreter, something like ".venv\Scripts\python.exe" (Please activate your venv in the terminal first)