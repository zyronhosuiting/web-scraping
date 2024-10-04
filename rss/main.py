import feedparser
from bs4 import BeautifulSoup

# Replace with the RSS feed URL you want to scrape
rss_url = "https://www.cryptocity.tw/rss"

# Parse the RSS feed
feed = feedparser.parse(rss_url)

# Loop through each entry in the feed
for entry in feed.entries:
    # Print basic information
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print(f"Published: {entry.published}\n")

    # Get the encoded content
    content = entry.content[0].value  # Access the CDATA content

    # Parse the HTML content
    soup = BeautifulSoup(content, "html.parser")

    # print the content
    print(soup.get_text())

    print("=" * 50)
    print("\n")
