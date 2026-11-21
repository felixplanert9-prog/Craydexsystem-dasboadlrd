
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CDXSystem Dashboard</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                min-height: 100vh;
                font-family: Arial, sans-serif;
                color: white;
                background:
                    radial-gradient(circle at top, #512080, transparent 45%),
                    linear-gradient(135deg, #10091f, #1b1030, #090612);
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                padding: 20px;
            }

            .container {
                max-width: 550px;
                width: 100%;
                padding: 40px 25px;
                background: rgba(30, 15, 50, 0.85);
                border: 1px solid #8b35ff;
                border-radius: 22px;
                box-shadow: 0 0 35px #8b35ff55;
            }

            h1 {
                color: #c77dff;
                font-size: 32px;
            }

            p {
                color: #ddd0f5;
                line-height: 1.6;
            }

            .status {
                margin-top: 25px;
                color: #c77dff;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🌌 CDXSystem Dashboard</h1>

            <p>
                Willkommen im offiziellen CDXSystem Dashboard!
            </p>

            <p>
                Verwalte deinen Discord-Server und
                passe die Einstellungen deines Bots an.
            </p>

            <div class="status">
                ✨ Galaxy Edition – Website im Aufbau
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
  
