from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time


# ---------- CPU ----------
def get_cpu():
    with open("/proc/stat") as f:
        line = f.readline()

    parts = list(map(int, line.split()[1:]))
    idle, total = parts[3], sum(parts)

    time.sleep(0.1)

    with open("/proc/stat") as f:
        line2 = f.readline()

    parts2 = list(map(int, line2.split()[1:]))
    idle2, total2 = parts2[3], sum(parts2)

    idle_diff = idle2 - idle
    total_diff = total2 - total

    return round((1 - idle_diff / total_diff) * 100, 2) if total_diff else 0


# ---------- RAM ----------
def get_ram():
    with open("/proc/meminfo") as f:
        mem = f.readlines()

    data = {}
    for line in mem:
        k, v = line.split(":")
        data[k] = int(v.strip().split()[0])

    used = data["MemTotal"] - data["MemAvailable"]
    return round((used / data["MemTotal"]) * 100, 2)


# ---------- STATS ----------
def get_stats():
    return {
        "cpu": get_cpu(),
        "ram": get_ram(),
        "timestamp": time.time()
    }


# ---------- SERVER ----------
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/stats":
            data = json.dumps(get_stats()).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(data)
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8787), Handler)
    print("SysStats server running at http://127.0.0.1:8787/stats")
    server.serve_forever()
