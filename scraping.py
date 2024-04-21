from bs4 import BeautifulSoup
import requests

URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
response = requests.get(URL)

# Check if HTTP request was successful
if response.status_code == 200:
    lst_of_items = []
    cleaned_items= []
    item_prices = []
    lst_of_ratings = []
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Item names
    items = soup.find_all("a", class_ = "title")
    for item in items:
        lst_of_items.append(item.text)
    for name in lst_of_items:
        new_name = name.split("...")[0]
        cleaned_items.append(new_name)

    # Price of the items
    prices = soup.find_all("h4", class_="price float-end card-title pull-right")
    for price in prices:
        price = price.text.split("$")[1]
        item_prices.append(float(price))

    # Get the rating of the items
    ratings = soup.find_all("p", class_="review-count float-end")
    for rating in ratings:
        rating = rating.text
        rating = rating.split(" ")[0]
        lst_of_ratings.append(rating)

    # A list of tuples with item name as first index and the item price as second index
    item_and_prices = list(zip(cleaned_items,item_prices))

    # Printing out filtered items with product name, product price and rating
    for index,product in enumerate(item_and_prices):
        cost = (product[1])
        if cost <= 999.0 and cost >= 600.0:
            print(f"Items between your desired prices: {product[0]} ${product[1]}. Reviews: {lst_of_ratings[index]}") 
        else:
            continue

