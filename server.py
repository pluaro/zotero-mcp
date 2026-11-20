from zotero_mcp.server import mcp

if __name__ == "__main__":
    import foro
    foro.run(mcp)  # startet den Server als streamable HTTP auf $PORT
