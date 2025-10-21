from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    return f"The weather in {location} is hot and dry."


if __name__ == "__main__":
    mcp.run()