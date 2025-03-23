from mcp.server.fastmcp import FastMCP
import sys
import datetime

mcp = FastMCP("Database")
    
products = {
    "Apple": [
        {"id": 1, "name": "iPhone 14", "price": 999},
        {"id": 2, "name": "iMac Pro", "price": 1999},
        {"id": 3, "name": "iPad Air", "price": 599}
    ],
    "Samsung": [
        {"id": 4, "name": "Galaxy S22 Ultra", "price": 999},
        {"id": 5, "name": "Galaxy Book Pro", "price": 1499},
        {"id": 6, "name": "QLED TV 75", "price": 2499}
    ],
    "Vorwerk": [
        {"id": 7, "name": "Vorwerk EasyClean 50", "price": 99},
        {"id": 8, "name": "Vorwerk EasyClean 60", "price": 149},
        {"id": 9, "name": "Vorwerk Cordless Stick", "price": 199}
    ]
}

orders = [
    {'product_id': '1', 'date' : '2025-02-20', 'quantity': 1},
    {'product_id': '2', 'date' : '2025-03-21', 'quantity': 2},
    
    {'product_id': '4', 'date' : '2025-03-22', 'quantity': 1},
    {'product_id': '5', 'date' : '2025-03-23', 'quantity': 2},

    {'product_id': '7', 'date' : '2025-03-22', 'quantity': 1},
    {'product_id': '8', 'date' : '2025-03-23', 'quantity': 2},
]

@mcp.tool()
async def get_product_list(company) -> str:
    """Get the list of products for a specific company. The result is json. 
    Here is an example {"id": 1, "name": "iPhone 14", "price": 999},
    """
    return products[company]

@mcp.tool()
async def get_orders_between(start_date, end_date) -> str:
    """Get all the orders between start_date and end_date
    """
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    return [order for order in orders if start <= datetime.datetime.strptime(order['date'], '%Y-%m-%d').date() < end]

if __name__ == "__main__":
    # test
    # import asyncio
    # print(asyncio.run(get_orders_between("2025-03-20", "2025-03-24")))
    
    print("Starting Database-MCP", file=sys.stderr)
    mcp.run(transport='stdio')
