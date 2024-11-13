from xmlrpc.server import SimpleXMLRPCServer

# Define a class with methods to be exposed
class MyRPCService:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

# Create the server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

# Register the service
server.register_instance(MyRPCService())

# Start the server
server.serve_forever()