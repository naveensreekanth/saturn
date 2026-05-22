import requests
from bs4 import BeautifulSoup
import pandas as pd


amazon_product_url = "https://www.amazon.com/product-reviews/B08N5WRWNW" 


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


response = requests.get(amazon_product_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

reviews_list = []
reviews = soup.find_all("div", {"data-hook": "review"})

for review in reviews:
    title = review.find("a", {"data-hook": "review-title"})
    rating = review.find("i", {"data-hook": "review-star-rating"})
    text = review.find("span", {"data-hook": "review-body"})

    review_data = {
        "Title": title.text.strip() if title else "N/A",
        "Rating": rating.text.strip() if rating else "N/A",
        "Review": text.text.strip() if text else "N/A",
    }
    reviews_list.append(review_data)


df = pd.DataFrame(reviews_list)
df.to_csv("amazon_reviews.csv", index=False)

print("Scraping completed! Reviews saved to amazon_reviews.csv")
