from bs4 import BeautifulSoup # Used for webscraping
import re # For creating REGEX formulas

from timeit import default_timer as timer
from datetime import datetime
from datetime import timedelta

def checkBlocks(parse):
    print("Block Check In Process...", end=" ")
    if(parse.find("title", text=re.compile('.*forbidden.*', re.I))
    or parse.find("pre", text=re.compile('.*cloudfront.*', re.I))
    ):
        return [True, "FORBIDDEN PAGE"]
    
    if(parse.find("title", text=re.compile('.*cloudflare.*', re.I))
    ):
        print("True", end="\n")
        return [True, "CloudFlare Protected"]
    print("False", end="\n")
    return [False]
    

def ruleEmailCheck(parse):
    # Input Field Check
    print("Rule Email Check In Process...", end=" ")
    if(a := parse.find_all("input", attrs={"type" : {re.compile('.*mail.*', re.I)}})
    or parse.find_all("input", attrs={"name" : re.compile('.*mail.*', re.I)})
    or parse.find_all("input", attrs={"value" : re.compile('.*mail.*', re.I)})
    or parse.find_all("input", attrs={"placeholder" : re.compile('.*mail.*', re.I)})
    or parse.find_all("input", attrs={"placeholder" : re.compile('.*subscribe.*', re.I)})
    or parse.find_all("input", attrs={"placeholder" : re.compile('.*newsletter.*', re.I)})
    
    # Attribute Check
    or parse.find_all(attrs={"class" : re.compile('.*mail.*', re.I)})
    or parse.find_all(attrs={"class" : re.compile('.*newsletter.*', re.I)})
    or parse.find_all(attrs={"id" : re.compile('.*mail.*', re.I)})
    or parse.find_all(attrs={"name" : re.compile('.*mail.*', re.I)})
    or parse.find_all(attrs={"value" : re.compile('.*mail.*', re.I)})
    or parse.find_all(attrs={"placeholder" : re.compile('.*mail.*', re.I)})
    ):
        print("True", end="\n")
        return True, a
    print("False", end="\n")
    return False, []

def ruleButtonCheck(parse):
    print("Button Rule Check In Process...", end=" ")
    if(parse.find_all("button")
    or parse.find_all("input", attrs={"value" : re.compile('.*submit.*', re.I)})
    or parse.find_all("input", attrs={"type" : re.compile('.*submit.*', re.I)})
    or parse.find_all(attrs={"id" : re.compile('.*submit.*', re.I)})
    or parse.find_all(attrs={"id" : re.compile('.*button.*', re.I)})
    or parse.find_all(attrs={"class" : re.compile('.*submit.*', re.I)})
    or parse.find_all(attrs={"class" : re.compile('.*button.*', re.I)})
    or parse.find_all(attrs={"class" : re.compile('.*btn.*', re.I)})
    or parse.find_all("button", attrs={"class" : re.compile('.*subscribe.*', re.I)})
    or parse.find_all(attrs={"text" : re.compile('.*subscribe.*', re.I)})
    or parse.find_all(attrs={"text" : re.compile('.*mail.*', re.I)})
    or parse.find_all(attrs={"value" : re.compile('.*submit.*', re.I)})
    ):
        print("True", end="\n")
        return True
    print("False", end="\n")
    return False

def ruleTextAreaAndPasswordCheck(ruleForms):
    print("Text Area and Password Rule Check In Process...", end=" ")
    for form in ruleForms:
        if(parent := form.find_parent('form')):
            if(parent.find("textarea")):
                if(parent.find("input", attrs={"type" : re.compile('.*password.*', re.I)})):
                    continue
            else:
                if(parent.find("input", attrs={"type" : re.compile('.*password.*', re.I)})):
                    continue
            print("True", end="\n")
            return True
    print("False", end="\n")
    return False

def ruleKeywordCheck(parse, keywords):
    print("Keyword Check In Process...")

    print("Checking Subscribe/Newsletter Related...", end=" ")
    if(parse.find('a', string=re.compile(f'.*subscribe.*', re.I))
    or parse.find('b', string=re.compile(f'.*subscribe.*', re.I))
    or parse.find('a', string=re.compile(f'.*newsletter.*', re.I))
    or parse.find('b', string=re.compile(f'.*newsletter.*', re.I))
    or parse.find('span', string=re.compile(f'.*newsletter.*', re.I))
    or parse.find('input', string=re.compile(f'.*newsletter.*', re.I))
    or parse.find('input', string=re.compile(f'.*subscribe.*', re.I))
    or parse.find('td', string=re.compile(f'.*newsletter.*', re.I))
    or parse.find('li', string=re.compile(f'.*newsletter.*', re.I))
    or parse.find(attrs={"alt" : re.compile(f'.*subscribe.*', re.I)})
    or parse.find(attrs={"placeholder" : re.compile(f'.*subscribe.*', re.I)})
    or parse.find(attrs={"id" : re.compile(f'.*subscribe.*', re.I)})
    or parse.find(attrs={"id" : re.compile(f'.*newsletter.*', re.I)})
    or parse.find(attrs={"class" : re.compile(f'.*newsletter.*', re.I)})
    or parse.find(attrs={"class" : re.compile(f'.*subscribe.*', re.I)})
    or parse.find(attrs={"placeholder" : re.compile(f'.*newsletter.*', re.I)})
    or parse.find(attrs={"data-sf-element" : re.compile(f'.*subscribe.*', re.I)})
    or parse.find(attrs={"data-sf-element" : re.compile(f'.*newsletter.*', re.I)})
    ):
        print("True", end="\n")
        return True
    print("False", end="\n")

    for keyword in keywords:
        print(f"Checking {keyword}...", end=" ")
        regex = re.compile(f'.*{keyword}.*', re.I)

        # if(parse.find(string=lambda x: x and x.lower()==keyword)
        # or parse.find(attrs={"data-type" : lambda x: x and x.lower()==keyword})
        # or parse.find(attrs={"text" : lambda x: x and x.lower()==keyword})
        # or parse.find(attrs={"class" : lambda x: x and x.lower()==keyword})
        # ):

        # if(parse.find('div', attrs={"text" : re.compile(f'.*{keyword}.*', re.I)}) 
        # or parse.find('div', attrs={"class" : re.compile(f'.*{keyword}.*', re.I)})
        # or parse.find('p', attrs={"text" : re.compile(f'.*{keyword}.*', re.I)})
        # or parse.find('p', attrs={"class" : re.compile(f'.*{keyword}.*', re.I)})
        # or parse.find('form', attrs={"id" : re.compile(f'.*{keyword}.*', re.I)})
        # or parse.find('form', attrs={"class" : re.compile(f'.*{keyword}.*', re.I)})
        # or parse.find('a', attrs={"text" : re.compile(f'.*{keyword}.*', re.I)})
        # or parse.find('a', attrs={"class" : re.compile(f'.*{keyword}.*', re.I)})
        # or parse.find(attrs={"data-type" : re.compile(f'.*{keyword}.*', re.I)})
        # or parse.find(attrs={"class" : re.compile(f'.*{keyword}.*', re.I)})

        # if(parse.find('div', text=lambda t: t and keyword in t) 
        # or parse.find('div', class_=lambda t: t and keyword in t) 
        # or parse.find('p', text=lambda t: t and keyword in t) 
        # or parse.find('p', class_=lambda t: t and keyword in t) 
        # or parse.find('form', id=lambda t: t and keyword in t) 
        # or parse.find('form', class_=lambda t: t and keyword in t) 
        # or parse.find('a', text=lambda t: t and keyword in t)
        # or parse.find('a', class_=lambda t: t and keyword in t)
        # or parse.find(attrs={"class" : lambda t: t and keyword in t})
        # or parse.find(attrs={"data-type" : lambda t: t and keyword in t})
        
        start = timer()
        if(parse.find('div', string=regex) 
        or parse.find('a', string=regex)
        or parse.find('a', string=regex)
        or parse.find('b', string=regex)
        or parse.find('b', attr={"text" : regex})
        or parse.find('p', string=regex)
        or parse.find('h1', string=regex)
        or parse.find('h2', string=regex)
        or parse.find('h3', string=regex)
        or parse.find('h4', string=regex)
        or parse.find('label', string=regex)
        or parse.find('span', string=regex)
        or parse.find('form', string=regex)
        or parse.find('td', string=regex)
        or parse.find('input', string=regex)
        or parse.find('input', attrs={"name" : regex})
        or parse.find('button', string=regex)
        or parse.find(attrs={"data-type" : regex})
        or parse.find(attrs={"class" : regex})
        or parse.find('input', attrs={"value" : regex})
        ):
            end = timer()
            timeTaken = "%s" % timedelta(seconds=end-start).total_seconds()
            print(f"Successful {timeTaken} seconds", end="\n")
            return True
        end = timer()    
        timeTaken = "%s" % timedelta(seconds=end-start).total_seconds()
        print(f"Not Found {timeTaken} seconds", end="\n")
    print("Keyword Check Returned False")
    return False

# def ruleKeyWordsV2(parse, keywords):
#     for keyword in keywords:
#         print(f"Checking {keyword}", end= " ")
#         start = timer()
#         check = re.search(re.compile(f'.*{keyword}.*', re.I), parse.text)
#         end = timer()
#         timeTaken = "%s" % timedelta(seconds=end-start).total_seconds()
#         print(f"{timeTaken} seconds", end ="\n")

#         if(check):
#             print("Keyword Check True")
#             return True

#     print("Keyword Check False")
#     return False


def findIframes(parse):
    print("iframe Check In Process...")
    iframes = parse.find_all('iframe')
    srcs = []
    for iframe in iframes:
        srcs.append(iframe['src'])

    print(f"iframe Check Complete. {len(srcs)} Detected.")
    return srcs

# 