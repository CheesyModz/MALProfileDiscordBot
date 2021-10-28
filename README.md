# MALProfileDiscordBot
This discord bot uses selenium and prints the username's MAL profile information

# What is MAL?
MAL stands for MyAnimeList and is a collection of animes that keeps track of one user's data (Anime watched, completed, plan to watch, scores, and many more).

# Why should you use this bot?
The code is very simple and easy to understand

Allows you to flex your MAL profile to your friend's on discord.

# How to use
Once you have everything set up, type the command `??mal username`

For example `??mal CheeseyModz`


# How to install and run (Windows Users)
1. Download python
2. If you plan to run this bot on Heroku skip to step 14 (Want to learn why? Read Explanation section)
3. Open command promopt
4. Type `pip` If you get an error, you have to config pip otherwise move onto step 4
5. Type `pip install selenium`
6. Install Google Chrome
7. At the top, press the 3 dots
8. Go to `help` then `About Google Chrome`
9. You should see your current version of Google Chrome
10. Go to `https://chromedriver.chromium.org/downloads` or download the one provided above (Version ChromeDriver 95.0.4638.17)
11. Download the ChromeDriver accordingly to your chrome version and operating system
12. One you have the file, extract the zip file
13. Download `bot.py` from above
14. Change the `ENTERYOURTOKENHERE` on line 6 to your own token (From Discord Portal Applications)
15. Add your own discord bot to a server
16. Run `bot.py`

# Explanation
Why skip installing selenium and chrome driver if you host this bot on Heroku?

The main reason for that is that Heroku's servers does not supply chrome web driver therefore meaning heroku cant have selenium
