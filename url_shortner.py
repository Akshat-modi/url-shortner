import pyshorteners

main_url = input("Enter the Main URL: ")
#initialize the Shortener

url_shortener = pyshorteners.Shortener()
#short the url with tinyurl

short_url = url_shortener.tinyurl.short(main_url)
print(f"The Short Url of {main_url} is: ")
print(short_url)