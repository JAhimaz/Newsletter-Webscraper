# Scraping Tools
import requests # Used for getting each webpage that can be further used for BeautifulSoup
from time import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup # Used for webscraping

import random

from timeit import default_timer as timer
from datetime import datetime
from datetime import timedelta

# Modules
import scraperFunc as sf

# Overwrite Results (This will overwrite the results.csv upon start)
overwriteResults = True

# Imports the URLS provided to check
urls = open("./urls.txt", "r").read().splitlines()

# Imports the list of Keywords to check for in Rule 5
keywords = open("./keywords.txt", "r").read().splitlines()

# Checks if the file exists, if it does, remove the current results.
if(overwriteResults):
    try:
        file = open("results.csv","r+")
        file.truncate(0)
        file.close()
    except:
        print("[No results.csv found]")

# Creates a HTMLSession 
session = HTMLSession()

# Gets a random User Agent from the text file list
def get_random_ua():
    with open("./ua_file.txt", "r") as f:
        lines = f.readlines()
        line = random.choice(lines)
        return line.rstrip('\n')

def scrapeSite(url):

    # Loads a random user agent
    # Using random user agents prevents websites from blocking same-level connections from constantly accessing the site.
    user_agent = get_random_ua()
    headers = {
        "User-Agent": user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    }


    try:
        # page = requests.get(url, headers=headers, timeout=10)
        resp = session.get(url, headers=headers, allow_redirects=True, timeout=15)
        # resp.html.render(timeout=5)
    except requests.exceptions.SSLError:
        return "Error (SSL)"
    except requests.exceptions.ConnectionError:
        return "Error (Connection)"
    except requests.exceptions.RequestException:
        return "Error (Request)"
    except requests.exceptions.HTTPError:
        return "Error (HTTP)"
    except requests.exceptions.ProxyError:
        return "Error (Proxy)"
    except:
        return "Error"

    try:
        parse = BeautifulSoup(resp.html.html, 'lxml')
    except:
        return "Error"

    # print(parse)

    # Checks for Forbidden pages and Cloudflare Protection
    blocked = sf.checkBlocks(parse)

    if(blocked[0]):
        return blocked[1]

    # Declare Variables
    ruleEmail = False
    ruleButton = False
    ruleTextAreaAndPassword = False
    ruleKeywords = False

    # Check for email input
    ruleEmail, ruleForms = sf.ruleEmailCheck(parse)

    if(ruleEmail):

        # Check for submit button
        ruleButton = sf.ruleButtonCheck(parse)

        if(ruleButton and ruleForms):
            ruleTextAreaAndPassword = sf.ruleTextAreaAndPasswordCheck(ruleForms)

    print("Keyword Check")

    # ruleKeywords = sf.ruleKeyWordsV2(resp, keywords)
    ruleKeywords = sf.ruleKeywordCheck(parse, keywords)

    # Check for iFrames
    # iframeSrcs = sf.findIframes(parse)

    # if(iframeSrcs):
    #     for iframeSrc in iframeSrcs:
    #         print(iframeSrc)
    #         resp = session.get(iframeSrc, headers=headers)
    #         parse = BeautifulSoup(resp.html.html, 'lxml')
    #         ruleKeywords = sf.ruleKeywordCheck(parse, keywords)

    if(ruleEmail and ruleButton and ruleTextAreaAndPassword):
        return "Yes"

    if(ruleKeywords):
        return "Yes"

    return "No"

if(overwriteResults):
    with open('results.csv', 'a') as the_file:
        the_file.write(f'URL, Has Newsletter, Time Taken\n')

def main():
    for url in urls:
        print(f"### {url}")
        start = timer()
        hasNewsLetter = scrapeSite(url)
        end = timer()

        timeTaken = "%s" % timedelta(seconds=end-start).total_seconds()

        with open('results.csv', 'a') as the_file:
            the_file.write(f'{url}, {hasNewsLetter}, {timeTaken}\n')
        print(f"######")
main()



