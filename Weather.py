from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather",port=8000)

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Gets the weather given a location
    Args:
        location: location, can be city, country, state, etc.
    Returns:
        str: weather description
    """
    return "The weather is beautiful" 

if __name__ == "__main__":
    mcp.run(transport="streamable-http")