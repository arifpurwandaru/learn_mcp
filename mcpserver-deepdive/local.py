from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("LocalNotes")


NOTES_FILE = Path(__file__).resolve().with_name("notes.txt")



@mcp.tool()
def add_note_to_file(content: str) -> str:
    """Appends the given content to user's local notes.
    Args:
        content: The content to append to the file."""

    try:
        with open(NOTES_FILE, "a", encoding="utf-8") as file:
            file.write(content + "\n")
        return f"Content appended to {NOTES_FILE.name}."
    except Exception as e:
        return f"Error appending to file {NOTES_FILE.name}: {e}"
    

@mcp.tool()
def read_notes() -> str:
    """
    Reads and returns the content of the user's local notes.
    """
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.read()
            return notes if notes else "no notes found."
    except FileNotFoundError:
        return "no notes file found."
    except Exception as e:
        return f"Error reading file {NOTES_FILE.name}: {e}"
    

if __name__ == "__main__":
    mcp.run()