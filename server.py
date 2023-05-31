import asyncio
import websockets

connected_clients = set()


async def notify_clients(message):
    if connected_clients:  # Check if there are connected clients
        await asyncio.gather(*[client.send(message) for client in connected_clients])


async def handle_client(websocket, path):
    connected_clients.add(websocket)  # Add the client to the set of connected clients
    try:
        print("Client connected")
        print(f"Total connected clients: {len(connected_clients)}")
        while True:
            # Handle incoming messages (if needed)
            await asyncio.sleep(1)  # Example: Simulate some background task
            await notify_clients(
                "New user created!"
            )  # Send notification to connected clients
    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected")
    finally:
        connected_clients.remove(
            websocket
        )  # Remove the client from the set of connected clients
    

async def start_server(port: int = 8765):
    async with websockets.serve(handle_client, "localhost", port):
        await asyncio.Future()  # Keep the server running indefinitely


if __name__ == "__main__":
    port = 8765
    print(f"Starting server on port localhost:{port}...")
    asyncio.run(start_server(port=port))
