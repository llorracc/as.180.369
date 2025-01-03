**Getting a Token for GitHub

1. Open SciServer and log in
- open a terminal
- type: 
```
gh auth login
```
- select: GitHub.com (What account do you want to log into?)
- select: SSH (What is your preferred protocol for Git operations?)
- select: yes (Generate a new SSH key to add to your GitHub account?)
- select: (Enter a passphrase for your new SSH key (Optional))
- select: AS180369 (Title for your SSH key:)
- select: Paste an authentication token (How would you like to authenticate GitHub CLI?)
- go to: https://github.com/settings/tokens
- click on: Generate new token --> Generate new token (classic)
- type: AS180369 (Note)
- select: all
- click on create token
- copy: Token
- go to: terminal in SciServer
- paste Token
- press enter
