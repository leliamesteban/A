from bs4 import BeautifulSoup
import requests
from urllib.parse import quote

# Digraphs (eg. accents are supported)
# Multiple artists in one are not supported by Musicbrainz
# artist = "Freddie+Gibbs+&+Madlib" # is not supported

def getCountry(artist):
    url = "https://musicbrainz.org/search?query=" + quote(artist) + "&type=artist&method=indexed"
    data = requests.get(url).content

    soup = BeautifulSoup(data, 'html.parser')

    # Search musicbrainz database for the artist and get the text from the fourth column in the first row
    nationality_column = soup.find(attrs={"data-score": "100"}).find_all("td")[4]

    if nationality_column.a:
        nationality = nationality_column.a.bdi.text
        if nationality == "United States":
            nationality = "United States of America"
        if nationality == "United Kingdom":
            nationality = "United Kingdom of Great Britain and Northern Ireland"
    else:
        nationality = ""

    with open('knownCountries', 'r') as knownCountries:
        if nationality in knownCountries.read().splitlines():
            print(nationality)
        else:
            # Add it to another array and edit manually
            # TOOD open the href value in the parent a tag in the bdi tag and parse that page for the country
            # url = nationality.parent()
            # data = requests.get(url).content
            # if p tag class subheader.text != "Country", return p class subheader .span.a.bdi
            print("")

with open('Artists') as artists:
    for artist in artists:
        getCountry(artist)
