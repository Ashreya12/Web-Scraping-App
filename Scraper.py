import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('#')

soup = BeautifulSoup(response.text, 'html.parser')

enclosing_div = "_31qSD5"

products = soup.find_all(class_=enclosing_div)

with open('product.csv', 'w', newline='') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Product Name', 'Rating', 'Price', 'EMI']
    csv_writer.writerow(headers)

    for product in products:
        name = product.find(class_="_3wU53n").get_text().replace('\n', '')
        rating = product.find(class_="hGSR34").get_text().replace('\n', '')
        price = product.find(
            class_="_1vC4OE").get_text().replace('\u20b9', 'Rs')
        emi = product.find(class_="_3MCpsc").get_text().replace('\u20b9', 'Rs')
        csv_writer.writerow([name, rating, price, emi])
