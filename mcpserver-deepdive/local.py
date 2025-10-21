from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LocalNotes")

@mcp.tool()
def add_note_to_file(content: str) -> str:
    """Appends the given content to user's local notes.
    Args:
        content: The content to append to the file."""

    filename = "notes.txt"
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(content + "\n")
        return f"Content appended to {filename}."
    except Exception as e:
        return f"Error appending to file {filename}: {e}"
    return "Note added."

@mcp.tool()
def read_notes() -> str:
    """
    Reads and returns the content of the user's local notes.
    """
    filename = "notes.txt"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            notes = file.read()
            return notes if notes else "no notes found."
    except FileNotFoundError:
        return "no notes file found."
    except Exception as e:
        return f"Error reading file {filename}: {e}"