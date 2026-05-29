import subprocess, json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/cmd':
            action = parse_qs(parsed.query).get('action', [''])[0]
            if action in ['play-pause', 'next', 'previous', 'play', 'pause']:
                subprocess.run(['playerctl', action])
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            return
        try:
            out = subprocess.check_output(
                ['playerctl', 'metadata', '--format', '{{title}}|||{{artist}}|||{{mpris:artUrl}}']
            ).decode().strip().split('|||')
            status = subprocess.check_output(['playerctl', 'status']).decode().strip()
            art = out[2].strip()
            # Spotify returns a small image URL, upgrade to highest res (640px)
            art = art.replace('/image/ab67616d00001e02', '/image/ab67616d0000b273')
            data = {'title': out[0], 'artist': out[1], 'art': art, 'status': status}
        except:
            data = {'title': '', 'artist': '', 'art': '', 'status': 'Stopped'}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def log_message(self, *a): pass

HTTPServer(('127.0.0.1', 8765), H).serve_forever()
