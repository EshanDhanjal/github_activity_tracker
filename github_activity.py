import sys
import urllib.request
import json

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200:
                print(f"Failed to fetch data. HTTP Status Code: {response.status}")
                return
            
            data = json.loads(response.read().decode())
            if not data:
                print("No recent activity found.")
                return

            shown_any = False

            for event in data:
                event_type = event['type']
                repo_name = event['repo']['name']

                if event_type == 'PushEvent':
                    commit_count = len(event['payload']['commits'])
                    print(f"- Pushed {commit_count} commit(s) to {repo_name}")
                    shown_any = True

                elif event_type == 'IssuesEvent':
                    action = event['payload']['action']
                    print(f"- {action.capitalize()} a new issue in {repo_name}")
                    shown_any = True

                elif event_type == 'WatchEvent':
                    print(f"- Starred {repo_name}")
                    shown_any = True

                elif event_type == 'ForkEvent':
                    print(f"- Forked {repo_name}")
                    shown_any = True

                elif event_type == 'PullRequestEvent':
                    action = event['payload']['action']
                    print(f"- {action.capitalize()} a pull request in {repo_name}")
                    shown_any = True

                elif event_type == 'CreateEvent':
                    ref_type = event['payload'].get('ref_type', 'item')
                    print(f"- Created a new {ref_type} in {repo_name}")
                    shown_any = True

            if not shown_any:
                print("No recent activity found that matches known event types.")

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("User not found.")
        else:
            print(f"HTTP Error: {e.code}")
    
    except urllib.error.URLError:
        print("Network error. Please check your internet connection.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        return
        
    username = sys.argv[1]
    fetch_github_activity(username)

if __name__ == "__main__":
    main()