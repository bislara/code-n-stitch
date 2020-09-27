import pyshorteners

pyShort = pyshorteners.Shortener()
#using TinyURL.com to shorten URL
URL = input("Enter your URL: ")
print(pyShort.tinyurl.short(URL))

#to expant what shorten from TinyURL.com
#pyShort.tinyurl.expand('tinyURL.shortened.URL')

#using Bit.ly to shortening the URL
#pyShort = pyshorteners.Shortener(api_key="your Access Token")
#look at https://dev.bitly.com/docs/getting-started/authentication/ to get your Token
#pyShort.bitly.short(URL)

#look at https://pyshorteners.readthedocs.io/en/latest/apis.html#bit-ly for other URL shortener
