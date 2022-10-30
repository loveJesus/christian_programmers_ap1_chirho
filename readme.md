# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life

## Introduction
A Discord BOT to help with applying to the Christian Programmers channel God willing and if we live.

## Installation
Below is an example on how to install in bash or another POSIX environment.

First you will want to create a [discord app and bot](https://discordpy.readthedocs.io/en/stable/discord.html). 
Make sure to set up the right permissions and intent. In the Bot page enable the 3 intent switches.
You will also want to [enable developer mode](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) 
in order to get the admin user id and channel id to post the join link for new users.

```bash
# 1. Clone the repository
git clone https://github.com/loveJesus/christian_programmers_ap1_chirho.git
cd christian_programmers_ap1_chirho

# 2. Setup environment (optional)
python3 -m venv venv_chirho
source venv_chirho/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install --upgrade -r requirements_chirho.txt

# 4. Copy and edit the environment file
cp aleluya_rename_to.env .env
nano .env

# 5. Run the bot
python3 christian_programmers_ap1_chirho.py
```

## Other notes
you can use `?apply` in a channel with the Bot to start the application process over.

## Todo:
 - [ ] Spam protection, hallelujah
 - [ ] Not  apply after you have already been accepted
 - [ ] Automate more of the process perhaps through buttons to the admin. God is good!.