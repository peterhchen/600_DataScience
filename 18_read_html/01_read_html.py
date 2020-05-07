try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from bs4 import BeautifulSoup

# Fetch the html file
response = urllib2.urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()

# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

# Format the parsed html file
strhtm = soup.prettify()

# Print the first few characters
print (strhtm[:100])

# Extract tag value
print('soup.title:', soup.title)
print('soup.title.string:', soup.title.string)
# print tag <a ... />
print('First p tage => soup.p.string:')
print(soup.p.string)
print('First a tag =>soup.a.string:')
print(soup.a.string)
print('Firt b tag => soup.b.string:')
print(soup.b.string)

# Find all tags
print("find_all('a') print first not None 5 tags:")
i = 0
for x in soup.find_all('a'):
      if (i > 5):
            break 
      if (x.string != None):
            print(x.string)
            i = i + 1
print("find_all('b') print first not None 5 tags:")
j = 0
for x in soup.find_all('b'):
      if (j > 5):
            break
      if (x.string != None): 
            print(x.string)
            j = j + 1