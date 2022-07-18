import os
# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

example_blocks = {
	"blocks": [
		{
			"type": "divider"
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Projects",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*drtsans*"
			}
		},
		{
			"type": "image",
			"title": {
				"type": "plain_text",
				"text": "next",
				"emoji": True
			},
			"image_url": "https://github.com/MicrosoftDocs/azure-devops-docs/raw/main/docs/pipelines/media/azure-pipelines-succeeded.png",
			"alt_text": "inspiration"
		},
		{
			"type": "image",
			"title": {
				"type": "plain_text",
				"text": "qa",
				"emoji": True
			},
			"image_url": "https://github.com/MicrosoftDocs/azure-devops-docs/raw/main/docs/pipelines/media/azure-pipelines-succeeded.png",
			"alt_text": "qa"
		},
		{
			"type": "divider"
		}
	]
}

# "https://code.ornl.gov/sns-hfir-scse/sans/sans-backend/badges/next/pipeline.svg",
# "https://code.ornl.gov/reflectometry/web_reflectivity/badges/next/pipeline.svg"
# "https://github.com/MicrosoftDocs/azure-devops-docs/raw/main/docs/pipelines/media/azure-pipelines-succeeded.png"

# Add functionality here
@app.event("app_mention")
def greetings(ack, say):
    ack()
    say("Build status summary for Neutron projects:")
    say(example_blocks)


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))