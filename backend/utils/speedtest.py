import subprocess
import json

def run_speedtest():
    result = subprocess.getoutput("speedtest --format json")
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        return {"error": "Speedtest failed"}