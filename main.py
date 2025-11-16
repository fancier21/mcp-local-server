from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("local-mcp")


async def make_nws_request(url: str) -> Any:
    headers = {"User-Agent": "mcp-local-server", "Accept": "application/json"}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool()
async def get_github_repos(username: str) -> str:
    """
    Get a list of GitHub repositories for a given username.

    Args:
        username (str): The GitHub username.

    Returns:
        str: A string representation of the repositories.
    """
    url = f"https://api.github.com/users/{username}/repos"
    data = await make_nws_request(url)

    if not data:
        return "No repositories found."

    # GitHub API returns a list of repository objects
    repos = [repo["name"] for repo in data if isinstance(repo, dict) and "name" in repo]
    numbered_repos = [f"{i + 1}. {repo}" for i, repo in enumerate(repos)]
    return "\n\n".join(numbered_repos)


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.resource("licenses://all")
def get_info() -> str:
    """
    Get information about the licenses from a local file.

    Returns:
        str: A string representation of the licenses.
    """
    try:
        with open("licenses.docs", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Licenses not found."


def main():
    print("Hello from mcp-local-server!")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
