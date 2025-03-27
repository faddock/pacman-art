import os
import datetime
import random
import urllib.request
import re
from better_profanity import profanity

# Function to get random commit messages from whatthecommit.com
def get_commit_message():
    try:
        with urllib.request.urlopen("https://whatthecommit.com/index.txt") as response:
            message = response.read().decode('utf-8').strip()
            censor_words = ["wholesome", "friendly", "oops", "beep", "fixed", "clean"]
            censored_message = profanity.censor(message, random.choice(censor_words))
            return censored_message
    except:
        return "added files"

HACKERSCHOOL = [
  [4,4,4,4,4,4],
  [4,3,3,3,3,4],
  [4,1,3,3,1,4],
  [4,3,3,3,3,4],
  [4,4,4,4,4,4],
  [1,1,4,4,1,1],
  [4,4,4,4,4,4],
]


KITTY = [
  [0,0,0,4,0,0,0,0,4,0,0,0],
  [0,0,4,2,4,4,4,4,2,4,0,0],
  [0,0,4,2,2,2,2,2,2,4,0,0],
  [2,2,4,2,4,2,2,4,2,4,2,2],
  [0,0,4,2,2,3,3,2,2,4,0,0],
  [2,2,4,2,2,2,2,2,2,4,2,2],
  [0,0,0,3,4,4,4,4,3,0,0,0],
]

ONEUP = [
  [0,4,4,4,4,4,4,4,0],
  [4,3,2,2,1,2,2,3,4],
  [4,2,2,1,1,1,2,2,4],
  [4,3,4,4,4,4,4,3,4],
  [4,4,1,4,1,4,1,4,4],
  [0,4,1,1,1,1,1,4,0],
  [0,0,4,4,4,4,4,0,0],
]

ONEUP2 = [
  [0,0,4,4,4,4,4,4,4,0,0],
  [0,4,2,2,1,1,1,2,2,4,0],
  [4,3,2,2,1,1,1,2,2,3,4],
  [4,3,3,4,4,4,4,4,3,3,4],
  [0,4,4,1,4,1,4,1,4,4,0],
  [0,0,4,1,1,1,1,1,4,0,0],
  [0,0,0,4,4,4,4,4,0,0,0],
]

HACKERSCHOOL = [
  [4,4,4,4,4,4],
  [4,3,3,3,3,4],
  [4,1,3,3,1,4],
  [4,3,3,3,3,4],
  [4,4,4,4,4,4],
  [0,0,4,4,0,0],
  [4,4,4,4,4,4],
]

OCTOCAT = [
  [0,0,0,4,0,0,0,4,0],
  [0,0,4,4,4,4,4,4,4],
  [0,0,4,1,3,3,3,1,4],
  [4,0,3,4,3,3,3,4,3],
  [0,4,0,0,4,4,4,0,0],
  [0,0,4,4,4,4,4,4,4],
  [0,0,4,0,4,0,4,0,4],
]

OCTOCAT2 = [
  [0,0,4,0,0,4,0],
  [0,4,4,4,4,4,4],
  [0,4,1,3,3,1,4],
  [0,4,4,4,4,4,4],
  [4,0,0,4,4,0,0],
  [0,4,4,4,4,4,0],
  [0,0,0,4,4,4,0],
]

HELLO = [
  [0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,4],
  [0,2,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,4],
  [0,3,3,3,0,2,3,3,0,3,0,3,0,1,3,1,0,3],
  [0,4,0,4,0,4,0,4,0,4,0,4,0,4,0,4,0,3],
  [0,3,0,3,0,3,3,3,0,3,0,3,0,3,0,3,0,2],
  [0,2,0,2,0,2,0,0,0,2,0,2,0,2,0,2,0,0],
  [0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,4],
]

HEART1 = [
  [0,1,1,0,1,1,0],
  [1,3,3,1,3,3,1],
  [1,3,4,3,4,3,1],
  [1,3,4,4,4,3,1],
  [0,1,3,4,3,1,0],
  [0,0,1,3,1,0,0],
  [0,0,0,1,0,0,0],        
]

HEART2 = [
  [0,5,5,0,5,5,0],
  [5,3,3,5,3,3,5],
  [5,3,1,3,1,3,5],
  [5,3,1,1,1,3,5],
  [0,5,3,1,3,5,0],
  [0,0,5,3,5,0,0],
  [0,0,0,5,0,0,0],        
]

HIREME = [
  [1,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [3,3,3,0,2,0,3,3,3,0,2,3,3,0,0,3,3,0,3,0,0,2,3,3],
  [4,0,4,0,4,0,4,0,0,0,4,0,4,0,0,4,0,4,0,4,0,4,0,4],
  [3,0,3,0,3,0,3,0,0,0,3,3,3,0,0,3,0,3,0,3,0,3,3,3],
  [2,0,2,0,2,0,2,0,0,0,2,0,0,0,0,2,0,2,0,2,0,2,0,0],
  [1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,1],
]

BEER = [
  [0,0,0,0,0,0,0,3,3,3,0,0,3,3,3,0,3,3,3,0,3,3,3,0,0],
  [0,0,1,1,1,1,0,3,0,0,3,0,3,0,0,0,3,0,0,0,3,0,0,3,0],
  [0,2,2,2,2,2,0,3,0,0,3,0,3,0,0,0,3,0,0,0,3,0,0,3,0],
  [2,0,2,2,2,2,0,3,3,3,0,0,3,3,3,0,3,3,3,0,3,3,3,0,0],
  [2,0,2,2,2,2,0,3,0,0,3,0,3,0,0,0,3,0,0,0,3,0,3,0,0],
  [0,2,2,2,2,2,0,3,0,0,3,0,3,0,0,0,3,0,0,0,3,0,0,3,0],
  [0,0,2,2,2,2,0,3,3,3,0,0,3,3,3,0,3,3,3,0,3,0,0,3,0],
]

GLIDERS = [
  [0,0,0,4,0,4,0,0,0,0,4,0,0,0],
  [0,4,0,4,0,0,4,4,0,0,0,4,0,0],
  [0,0,4,4,0,4,4,0,0,4,4,4,0,0],
  [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  [0,4,0,4,0,0,0,4,0,0,0,0,0,0],
  [0,0,4,4,0,4,0,4,0,0,0,0,0,0],
  [0,0,4,0,0,0,4,4,0,0,0,0,0,0],
]

HEART = [
  [0,4,4,0,4,4,0],
  [4,2,2,4,2,2,4],
  [4,2,2,2,2,2,4],
  [4,2,2,2,2,2,4],
  [0,4,2,2,2,4,0],
  [0,0,4,2,4,0,0],
  [0,0,0,4,0,0,0],
]

HEART_SHINY = [
  [0,4,4,0,4,4,0],
  [4,2,0,4,2,2,4],
  [4,0,2,2,2,2,4],
  [4,2,2,2,2,2,4],
  [0,4,2,2,2,4,0],
  [0,0,4,2,4,0,0],
  [0,0,0,4,0,0,0],
]

PACMAN = [
  [1,1,2,3,4,3,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,1],
  [1,2,3,4,4,4,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,3,4,4,4,3,1,1,1,2,3,2,1,1,3,2,3,1,1,2,3,2,1,1,1,1],
  [1,4,4,4,1,1,1,1,1,3,4,3,1,1,2,4,2,1,1,3,4,3,1,1,1,1],
  [1,3,4,4,4,3,1,1,1,2,3,2,1,1,3,2,3,1,1,2,3,2,1,1,1,1],
  [1,2,3,4,4,4,3,2,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,2,3,4,3,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,2,1,1,1],
]

logos = [PACMAN, ONEUP2]

# Function to perform commits on a specific date based on intensity
def make_commits(date, intensity):
    if intensity == 0:
        return  # Skip days with zero intensity

    # Number of commits based on intensity (1-4)
    num_commits = intensity
    for i in range(num_commits):
        # Get a random commit message
        commit_msg = get_commit_message()

        # Create or update a file with random content
        with open("commits.txt", "a") as file:
            file.write(f"Commit on {date.strftime('%Y-%m-%d')} - {i+1}\n")

        # Set environment variables for commit date
        os.environ['GIT_AUTHOR_DATE'] = date.strftime('%Y-%m-%d %H:%M:%S')
        os.environ['GIT_COMMITTER_DATE'] = date.strftime('%Y-%m-%d %H:%M:%S')

        # Add and commit changes
        os.system('git add commits.txt')
        os.system(f'git commit -m "{commit_msg}"')

# Returns a datetime object for the first Sunday before one year ago today
def get_start_date():
    today = datetime.datetime.now()
    date = datetime.datetime(today.year - 1, today.month, today.day, 12)
    # Adjust to prev Sunday (in Python, Sunday is weekday 6)
    while date.weekday() != 6:
        date -= datetime.timedelta(days=1)
    return date

def main():
    # Initialize git repository if it doesn't exist.
    if not os.path.exists(".git"):
        print("Initializing git repository...")
        os.system('git init')

    # Create README.md if it doesn't exist.
    if not os.path.exists("README.md"):
        print("Creating README.md...")
        with open("README.md", "w") as file:
            file.write("# Contribution Graph Art\n\nThis repository was created to generate logo art on my GitHub contribution graph using git commits.")
        os.system('git add README.md')
        os.system(f'git commit -m "{get_commit_message()}"')

    # Get the start date (first Sunday after one year ago)
    start_date = get_start_date()
    today = datetime.datetime.now()
    print(f"Starting commits from: {start_date.strftime('%Y-%m-%d')}")

    current_date = start_date
    while current_date <= today:
        make_commits(current_date, 1)
        current_date += datetime.timedelta(days=1)

    # --- Overlay logos on top of the background ---
    print("Adding logos to the contribution history...")
    # Track the horizontal (column) offset for each logo.
    col_offset = 0
    for logo in logos:
        num_cols = len(logo[0])
        num_rows = len(logo)  # should be 7
        for col in range(num_cols):
            for row in range(num_rows):
                # Calculate the commit date. The pattern assumes each column spans 7 days.
                commit_date = start_date + datetime.timedelta(days=((col_offset + col) * 7 + row))
                intensity = logo[row][col]-1
                make_commits(commit_date, intensity)
        col_offset += num_cols

    print("Gitfiti logos have been created successfully!")
    print("Push to GitHub with: git push -u origin main")

if __name__ == "__main__":
    main()