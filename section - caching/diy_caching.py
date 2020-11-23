import requests

'''
Implement Basic DIY caching
'''
cache = dict()


def get_content_from_server(url):
    print("Fetching content from remote server...")
    response = requests.get(url)
    return response.text


def get_content(url):
    print("\nGetting content from network or cache")
    '''
    given a URL, try finding that page in the cache
    if the page is in the cache:
        return the cached page
    else:
        generate the page
        save the generated page in the cache (for next time)
        return the generated page
    '''
    if url not in cache:
        print("\nGetting content from network")
        cache[url] = get_content_from_server(url)
    else:
        print("content is already in cache")

    return cache[url]

if __name__ == '__main__':
    # DIY cache using a dict to store KV pairs
    get_content("https://docs.python.org/3.7/library/functools.html")
    get_content("https://docs.python.org/3.7/library/functools.html")
