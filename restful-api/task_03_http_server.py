#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom handler class to process HTTP requests.
    Inherits from BaseHTTPRequestHandler to handle protocol details.
    """

    def do_GET(self):
        """
        Handles HTTP GET requests.
        The method name 'do_GET' is required by BaseHTTPRequestHandler.
        """

        # --- Endpoint: Root URL ("/") ---
        if self.path == "/":
            # 1. Send the HTTP status code (200 = OK)
            self.send_response(200)
            
            # 2. Send headers (Define the type of content being sent)
            self.send_header("Content-Type", "text/plain")
            self.end_headers() # Must strictly call this to finish header section
            
            # 3. Write the body content
            # Note: wfile.write requires a bytes object (b"string"), not a standard string
            self.wfile.write(b"Hello, this is a simple API!")

        # --- Endpoint: Data ("/data") ---
        elif self.path == "/data":
            # Prepare a Python dictionary
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            
            self.send_response(200)
            # Set content type to JSON so the client knows how to parse it
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            
            # Serialize dictionary to JSON string -> Encode string to bytes (UTF-8)
            self.wfile.write(json.dumps(data).encode("utf-8"))

        # --- Endpoint: Status ("/status") ---
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # --- Endpoint: Info ("/info") ---
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # --- Catch-all: 404 Not Found ---
        else:
            # Handle any path that wasn't defined above
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """
    Sets up and starts the HTTP server.
    """
    # Define server address. "" means bind to all interfaces (localhost/network IP)
    server_address = ("", 8000)
    
    # Instantiate the server
    httpd = server_class(server_address, handler_class)
    
    print("Starting server on port 8000...")
    
    # Start the event loop to listen for requests indefinitely
    httpd.serve_forever()


if __name__ == "__main__":
    # execute run() only if the script is run directly (not imported as a module)
    run()
