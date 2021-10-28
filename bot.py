import discord
import time
from selenium import webdriver

BOT_PREFIX = ("??")
TOKEN = "ENTERYOURTOKENHERE"
client = Bot (command_prefix = BOT_PREFIX)

@client.command(name="mal",
                description = "Checks someone's MyAnimeList",
                brief = "list mal profile",
                aliases = ["MAL"])
async def mal(ctx, Username):
    PATH = 'chromedriver.exe'
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(PATH, chrome_options=options)

    url = "https://myanimelist.net/profile/" + Username
    driver.get(url)
    
    title = driver.title
    if title == "404 Not Found - MyAnimeList.net":
        await ctx.send("Profile not found. Try again!")
        emb = discord.Embed(colour = discord.Colour.purple())
        emb.set_image(url = "https://c.tenor.com/ZNSvL6hJJ3MAAAAC/impostersus-the-impostor-is-sus.gif")
        await ctx.send(embed = emb)
        driver.close()
        return
    # remove - MyAnimeList.net from title
    title = title[0:len(title)-17]

    emb = discord.Embed(colour = discord.Colour.purple())
    emb.add_field(name = title, value = "Anime Stats", inline = False)

    # Get the image
    images = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div/div[1]/img')
    for image in images:
        emb.set_image(url = image.get_attribute("src"))
        # emb.set_thumbnail(url = image.get_attribute("src"))

    # days = driver.find_elements_by_xpath('//*[@id="statistics"]/div[1]/div[1]/div[1]/div[1]/text()').getText()
    # for day in days:
    #     dayNum = day.text
    # emb.add_field(name = "Days", value = str(days), inline = True)

    meanScore = driver.find_element_by_xpath('//*[@id="statistics"]/div[1]/div[1]/div[1]/div[2]/span[2]').text
    emb.add_field(name = "Mean Score: ", value = meanScore, inline = True)

    watching = driver.find_element_by_xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[1]/li[1]/span').text
    emb.add_field(name = "Watching: ", value = watching, inline = True)

    completed = driver.find_element_by_xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[1]/li[2]/span').text
    emb.add_field(name = "Completed: ", value = completed, inline = True)

    onHold = driver.find_element_by_xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[1]/li[3]/span').text
    emb.add_field(name = "On-Hold: ", value = onHold, inline = True)

    dropped = driver.find_element_by_xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[1]/li[4]/span').text
    emb.add_field(name = "Dropped: ", value = dropped, inline = True)

    planToWatch = driver.find_element_by_xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[1]/li[5]/span').text
    emb.add_field(name = "Plan to Watch: ", value = planToWatch, inline = True)

    totalEntries = driver.find_element_by_xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[2]/li[1]/span[2]').text
    emb.add_field(name = "Total Entries: ", value = totalEntries, inline = True)

    rewatched = driver.find_element_by_xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[2]/li[2]/span[2]').text
    emb.add_field(name = "Rewatched: ", value = rewatched, inline = True)

    episodes = driver.find_element_by_xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[2]/li[3]/span[2]').text
    emb.add_field(name = "Episodes: ", value = episodes, inline = True)

    emb.set_footer(text=f"Information provided by MAL {url}")

    await ctx.send(embed = emb)

    time.sleep(5)

    driver.close()

    
@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

client.run(TOKEN)
