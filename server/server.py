import logging

connections = set()


async def handler(websocket, path) -> None:
    """
    Handle every websocket connection
    :param websocket: Current websocket connection
    :param path: Path after / in url socket connection
    """
    logging.debug(f"Connected to server: {websocket}")
    connections.add(websocket)
    try:
        async for message in websocket:
            for conn in connections:
                    await conn.send(f'Hello {websocket}. Message {message}')
    finally:
        connections.remove(websocket)
        logging.debug(f"Disconnected from server: {websocket}")
