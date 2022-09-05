import requests
import pandas as pd
import io

# Web Crawler Function
def crawler(URL):
    resp = requests.get(URL)
    if resp.status_code == 200:
        print(resp)
    return resp
    """csvtext = resp.text
    csvbuffer = io.StringIO(csvtext)
    df = pd.read_csv(csvbuffer)
    print(df)"""

def main():
    URL = "https://www.reddit.com/"
    data = crawler(URL)
    # print(data)
    
if __name__ == "__main__":
    main()

# TODO
# Fetch the content of a discovered URL
# Discover any new URLs by extracting them from the fetched content
# Crawl any new URLs
# Seed the crawler with any of the sites proposed below as the start URL (first discovered URL)