import asyncio
import logging

import websockets

import settings
from server.server import handler

if __name__ == '__main__':
    # Run websocket server
    logging.basicConfig(level=logging.DEBUG)
    start_server = websockets.serve(handler, settings.SERVER_URL, settings.SERVER_PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    logging.info("Server started")
