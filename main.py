import feedparser

# https://status.docusign.com/rss/feed.xml
rssfeed = 'https://www.standaard.be/rss/section/451c8e1e-f9e4-450e-aa1f-341eab6742cc'


def scrape (url):
    
    try:
        data = feedparser.parse(url)
        for entry in data.entries:

            print(f"Title: {entry.title}")
            print(f'Date: {entry.published}')
            print(f"Summary: {entry.summary_detail.value}")
            print('\n---------------------------------\n')
        
    except:
        print('Error')

scrape(rssfeed)

