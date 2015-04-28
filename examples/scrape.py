"""
Let's scrape the Nebraska Game and Parks database of trophy animals.

"""

from mechanize import Browser
from bs4 import *
from time import *
import re

# Start a browser
mech = Browser()

# Add a user-agent string
mech.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Define the URL
url = "http://outdoornebraska.ne.gov/trophy/"

# Soup the page
page = mech.open(url)
html = page.read()
soup = BeautifulSoup(html)

# Target the number of the last page to step through with a regular expression and store as an integer
r = soup.find(text=re.compile("Page\s\d+")).parent.text.replace("\r","").replace("\n","").replace("\s\s+","").replace("\t","").strip()
q = re.search(r'of \d+', r)
pagelimit = int(q.group().replace('of ',''))

# Set a counter variable
paging = 0

# Open a text file to write the results to
f = open('trophies.txt', 'wb')

# Loop through the table on each page 
while (paging < pagelimit):
   print 'Scraping page', paging
   table = soup.find("table", class_="data-grid")
   for row in table.findAll('tr')[2:]:
       col = row.findAll('td')
       year = col[0].string
       score = col[1].string
       species = col[2].string
       weapon = col[3].string
       killtype = col[4].string
       county = col[5].string
       first = col[6].string
       last = col[7].string
       city = col[8].string
       details = 'http://outdoornebraska.ne.gov' + col[9].find('a').get('href')
       animals = (year.strip(), score.strip(), species.strip(), weapon.strip(), killtype.strip(), county.strip(), first.strip(), last.strip(), city.strip(), details.strip())
       f.write("|".join(animals) + "\n")
   sleep(3)
   nextpage = mech.follow_link(text_regex="Next >")
   nexthtml = nextpage.read()
   soup = BeautifulSoup(nexthtml)
   paging += 1

f.flush()
f.close()