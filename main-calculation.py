# from typing import Any

# import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("local-mcp")


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b


@mcp.tool()
def subtract_numbers(a: int, b: int) -> int:
    """Subtract two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The difference of the two numbers.
    """
    return a - b


@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of the two numbers.
    """
    return a * b


@mcp.tool()
def divide_numbers(a: int, b: int) -> float:
    """Divide two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        float: The quotient of the two numbers.
    """
    return a / b


def main():
    print("Hello from mcp-local-server!")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
