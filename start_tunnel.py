# start_tunnel.py
import subprocess, re, time, os, sys, shutil

# 𝟭) Ensure we can find 'npx' on Windows (npx.cmd) or Unix
npx_exe = shutil.which("npx") or shutil.which("npx.cmd")
if not npx_exe:
    print("❌ ERROR: 'npx' not found in PATH. Please install Node.js (which provides npx) and ensure your npm global bin is in PATH.")
    sys.exit(1)

# 𝟮) Launch Flask via the same Python interpreter
flask_proc = subprocess.Popen(
    [sys.executable, "app.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    universal_newlines=True
)

# Give Flask a moment to spin up
time.sleep(3)

# 𝟯) Launch LocalTunnel via npx
lt_cmd = [npx_exe, "localtunnel", "--port", "5000"]
lt_proc = subprocess.Popen(
    lt_cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    universal_newlines=True
)

tunnel_url = None
for line in lt_proc.stdout:
    print("[lt]", line.strip())
    m = re.search(r"https://[a-z0-9\-]+\.loca\.lt", line)
    if m:
        tunnel_url = m.group(0)
        break

if not tunnel_url:
    print("❌ Could not detect tunnel URL. Is LocalTunnel installed? Try `npm install -g localtunnel`.")
    lt_proc.terminate()
    flask_proc.terminate()
    sys.exit(1)

print(f"✅ Detected tunnel URL: {tunnel_url}")

# 𝟰) Write it into your Flask `static/` folder
os.makedirs("static", exist_ok=True)
with open(os.path.join("static", "tunnel_url.js"), "w") as f:
    f.write(f"const BASE_URL = '{tunnel_url}';\n")

print("✅ Generated static/tunnel_url.js")

# 𝟱) Wait on the tunnel process; clean up on exit
try:
    lt_proc.wait()
finally:
    flask_proc.terminate()
