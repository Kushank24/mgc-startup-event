import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

def main():
    """
    Serve the Trisarg startup event website locally
    """
    # Change to the directory containing the HTML files
    web_dir = Path(__file__).parent
    os.chdir(web_dir)
    
    PORT = 8000
    
    class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()
    
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🎉 त्रिसर्ग (Trisarg) Website Server Started!")
            print(f"🌐 Server running at: http://localhost:{PORT}")
            print(f"📁 Serving files from: {web_dir}")
            print(f"🚀 Opening website in your default browser...")
            print(f"⏹️  Press Ctrl+C to stop the server")
            
            # Open the website in the default browser
            webbrowser.open(f'http://localhost:{PORT}')
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print(f"\n🛑 Server stopped by user")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Please try a different port or stop the existing server.")
        else:
            print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main()
