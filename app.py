from flask import Flask, request, redirect
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1205311769854087168/jh9-cPXQe5ks0LtHH229LMcCdkj7glJ5ENPJc7RTnfwZ4Mgh3KE9Rf4JfqUy4TbEi07a"

@app.route('/')
def hello_world():
    # Extract the user's city and state from the request (customize this based on your application)
    city = request.args.get('city', 'Unknown City')
    state = request.args.get('state', 'Unknown State')

    # Send message to Discord webhook
    discord_message = f"Someone got rickrolled in {city}, {state}! Redirect them: https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    payload = {'content': discord_message}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)

    # Redirect to the Rick Astley video
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)

if __name__ == "__main__":
    app.run()
