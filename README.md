# GitHub Activity

A simple command line tool to fetch and display the recent public activity of any GitHub user.

## Features

- Fetch recent public events of a GitHub user via GitHub API.
- Displays commits pushed, issues opened/closed, pull requests, stars, forks, and more.
- Handles errors gracefully like invalid usernames or network issues.
- No external libraries needed—built with Python standard libraries only.

## Usage

Run the script from the command line and provide the GitHub username as an argument:

```bash
python github_activity.py <username>

Example:

python github_activity.py EshanDhanjal

Sample output:

- Pushed 3 commit(s) to EshanDhanjal/developer-roadmap
- Opened a new issue in EshanDhanjal/developer-roadmap
- Starred EshanDhanjal/developer-roadmap

Requirements

    Python 3.x

    Internet connection to access GitHub API

Notes

    The tool only shows public activity.

    GitHub API limits the number of returned events (default 30 recent events).

    Works on any platform that can run Python scripts.

License

This project is licensed under the MIT License.
