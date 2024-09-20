# creating a list with three favourite websites
fav_websites = [
    "Fantasy Premier League - https://fantasy.premierleague.com",
    "Youtube - https://www.youtube.com",
    "Wikipedia - https://www.wikipedia.org"
]

print(fav_websites)
print(len(fav_websites))

# appending two more websites to the same list
fav_websites.append("Google - http://www.google.com")
fav_websites.append("BBC Sport - https://www.bbc.co.uk/sport")

print(fav_websites)
print(len(fav_websites))

# remove last website from the list
fav_websites.pop()

print(fav_websites)
print(len(fav_websites))