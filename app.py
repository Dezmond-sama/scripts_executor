import sys
from flask import Flask, request
import io
from contextlib import redirect_stdout

app = Flask(__name__)

@app.route("/api/run", methods=["POST"])
def run_script():
    data = request.json
    script = data.get("script", "print(\"NO SCRIPT PROVIDED\")")
    sys.argv = data.get("argv", ["script.py"])
    try:
        stdout =  io.StringIO()
        with redirect_stdout(stdout):
            exec(script, {'__name__':'__main__'})
        out = stdout.getvalue()
        return {"res":out}, 200
    except Exception as e:
        print(e)
        return {"error": str(e)}, 400
    
    
def create_app():
   return app

if __name__ == "__main__":
    # app.run()
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)