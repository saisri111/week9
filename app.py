
from flask import Flask, request
from html import escape

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if name and email:
            message = f"Registration successful for {escape(name)}!"
        else:
            message = "Please enter your name and email."

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Registration</title>
    </head>
    <body style="font-family:Arial;margin:50px">
        <h1>Student Registration</h1>
        <form method="post">
            <input name="name" placeholder="Enter name" required>
            <br><br>
            <input name="email" type="email"
                   placeholder="Enter email" required>
            <br><br>
            <button type="submit">Register</button>
        </form>
        <p>{message}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
