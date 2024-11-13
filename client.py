import xmlrpc.client

# Create an RPC client
server_url = "http://localhost:8000"
client = xmlrpc.client.ServerProxy(server_url)

# Call the remote methods
result_add = client.add(5, 3)
result_subtract = client.subtract(5, 3)

print(f"5 + 3 = {result_add}")
print(f"5 - 3 = {result_subtract}")