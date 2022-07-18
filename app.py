import os
import requests
# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

status2emoji = {
    "success": ":white_check_mark:",
    "failed": ":x:",
    "running": ":hourglass:",
    "error": ":ghost:",
}

def get_status_blocks():
    blocks = []
    #
    projects = {
        "drtSANS": 4955,
        "Web_Reflectivity": 5380,
        "django-remote-submission": 10248,
        "Web Monitor Test AMQ Message Generator": 10770,
    }
    for project, project_id in projects.items():
        branches_status = {
            "next": "error",
            "qa": "error",
            "main": "error",
        }
        url = f"https://code.ornl.gov/api/v4/projects/{project_id}/pipelines"
        for branch, status in branches_status.items():
            response = requests.get(url, params={"ref": branch})
            if response.status_code == 200:
                try:
                    status = response.json()[0]["status"]
                except:
                    print(project)
                    print(branch)
                    print(response.json())
            try:
                status_emoji = status2emoji[status]
            except:
                print(project)
                print(branch)
                print(response.json())
                print(status)
            branches_status[branch] = status_emoji
        # build the block
        blocks += [
            {
                "type": "divider"
            },
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"{project}",
                    "emoji": True
			    }
		    },
		    {
			    "type": "divider"
		    },
		    {
			    "type": "section",
			    "text": {
				    "type": "mrkdwn",
				    "text": f"*next* {branches_status['next']}\t:white_small_square:\t*qa*{branches_status['qa']}\t:white_small_square:\t*main*{branches_status['main']}"
			    }
		    },
        ]
    return blocks

# Add functionality here
@app.event("app_mention")
def greetings(ack, say):
    ack()
    say("Build status summary for Neutron projects:")
    status_blocks = {"blocks": get_status_blocks()}
    say(status_blocks)


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))