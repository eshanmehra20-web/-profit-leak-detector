from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT / "static")

if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    print(f"Profit Leak Detector running at http://{address[0]}:{address[1]}")
    print("Local-only server. Press Ctrl+C to stop.")
    ThreadingHTTPServer(address, SimpleHTTPRequestHandler).serve_forever()
