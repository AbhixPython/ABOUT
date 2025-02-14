from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SERVERX</title>
    <style>
      .container {
            display: flex;
            flex-direction: column;
            align-items: center; /* Center horizontally */
            text-align: center; /* Center text within elements */
            padding: 20px;
        }

      .image-container {
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.2); /* 20px box shadow */
            margin-bottom: 20px; /* Space between image and text */
            /* Add other styling for your image container if needed */
        }
        img {
            max-width: 100%; /* Make image responsive */
            height: auto;
        }
      .message {
          max-width: 600px; /* Adjust as needed */
          margin: 0 auto; /* Center the message text */
          text-align: justify; /* Justify the text */
        }
        footer {
          margin-top: 20px; /* Add some space above the footer */
          text-align: center;
          font-size: smaller;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="image-container">
        <img src="https://i.ibb.co/jPYnhPBR/20250214-201643.jpg" alt="">  </div>

    <div class="message">
        <p>Welcome to SERVERX! We are a leading provider of automated tools designed to enhance your social media presence and productivity.</p>
<p> Our solutions are trusted by thousands of users across the globe to streamline Facebook interactions, manage conversations, and extract valuable data effortlessly. At Serverx, our mission is to simplify and automate the tasks that take up your valuable time, giving you more control over your online engagements. We offer a suite of tools including  Messenger Management Tools, and Token Getters, all with the goal of making social media work for you.</p>

        <p>Founded in 2025, By Abhi And All Codes Made By Abhi we continue to innovate and bring cutting-edge solutions to the table, ensuring that our users stay ahead of the competition. Our commitment to quality, security, and user-friendly interfaces is what sets us apart in the industry.</p>
    </div>
    <footer>
    ©2025 Serverx Abhi. All rights reserved.
    </footer>
</div>

</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    
