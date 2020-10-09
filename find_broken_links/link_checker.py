from urllib.parse import urlsplit
import re
import bs4
import requests

def link_broken(link):
    """
    Function that checks if an individual link can be accessed successfully
    """
    try:
        res = requests.get(link, headers={"User-Agent": "Mozilla/5.0"})
        #Raise for status creates HTTPError exception if request is unsuccessful
        res.raise_for_status()
        return False
    except requests.HTTPError:
        return True
    except Exception:
        return True

def find_broken_links(address):
    """Given a base URL, extracts all links found in elements that may possess them.
    Additionally, collect the broken ones (i.e., request returns HTTP error code)"""
    links = []
    #Possible visible elements with links: anchors and images
    elem_dict= {'a':'href', 'img':'src'}

    #Create soup to get page HTML
    res = requests.get(address)
    http_encoding = res.encoding if 'charset' in res.headers.get('content-type', '').lower() else None
    html_encoding = bs4.dammit.EncodingDetector.find_declared_encoding(res.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = bs4.BeautifulSoup(res.content,"html.parser", from_encoding=encoding)

    #Iterate over visible elements with potential links
    for element, attribute in iter(elem_dict.items()):
        try:
            for link_elem in soup.select(element):
                if link_elem.has_attr(attribute):
                    url_to_test = link_elem[attribute]

                    #Potential adjustments to URL, as they may not be suitable to test or not OOTB ready
                    #Local link to other element via #id, can't be broken
                    if link_elem[attribute].startswith("#"):
                        continue
                    address_split = urlsplit(link_elem[attribute])

                    #Relative path, so prepend base address provided
                    if address_split.scheme == '' and address_split.netloc == '':
                        url_to_test = address + link_elem[attribute]
                    #Special case of no protocol, non-relative URL
                    elif address_split.scheme == '' and (address_split.netloc != '' or address_split.path != ''):
                        if re.match('^//' , url_to_test):
                            path_match = re.search(r'(?<=//)\S+', url_to_test)
                            url_to_test = path_match.group(0)
                            url_to_test = "https://" + url_to_test

                    #Finally test URL to check if it is broken
                    if link_broken(url_to_test):
                        links.append(url_to_test)
        except requests.HTTPError as http_excpt:
            print(http_excpt)
    return links
