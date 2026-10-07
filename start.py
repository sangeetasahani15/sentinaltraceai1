"""Optional launcher: python start.py  (or just double-click index.html)"""
import http.server, socketserver, webbrowser, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
socketserver.TCPServer.allow_reuse_address = True
for port in range(8000, 8011):
    try:
        srv = socketserver.TCPServer(("127.0.0.1", port), H); break
    except OSError:
        continue
else:
    raise SystemExit("No free port between 8000-8010")
url = f"http://127.0.0.1:{port}/index.html"
print("SentinelTrace AI running at", url, "- press Ctrl+C to stop")
webbrowser.open(url)
try: srv.serve_forever()
except KeyboardInterrupt: print("\nStopped")
