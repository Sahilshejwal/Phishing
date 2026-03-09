from flask import Flask, render_template, request
import re

# Create Flask app
app = Flask(__name__)

# Function to check if URL is phishing
def check_phishing(url):

    score = 0

    # Rule 1: Long URL check
    if len(url) > 50:
        score += 1

    # Rule 2: Suspicious characters
    if "@" in url or "-" in url:
        score += 1

    # Rule 3: HTTPS check
    if not url.startswith("https"):
        score += 1

    # Rule 4: IP address detection
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 1

    # Final result
    if score >= 2:
        return "⚠ Possible Phishing Website"
    else:
        return "✅ URL is Safe"


# Website route
@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        url = request.form["url"]
        result = check_phishing(url)

    return render_template("index.html", result=result)


# Run server
if __name__ == "__main__":
    app.run(debug=True)
