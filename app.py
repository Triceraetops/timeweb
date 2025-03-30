##timeweb app.py a6 devops
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def time():
    rn = datetime.now().strftime("%b %d, %Y, %H:%M")
    return f"""
    <html>
        <head>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: white;
                }}
                h1 {{
                    font-family: 'Comic Sans MS', cursive, sans-serif;
                    color: pink;
                    font-size: 3em;
                }}
            </style>
        </head>
        <body>
            <h1>{rn}</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8086)

