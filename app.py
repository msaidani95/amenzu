from flask import Flask, render_template, request
from scraper import search_amazon

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        product_name = request.form['product_name']
        price = search_amazon(product_name)
        if price is not None:
            price = f"${price:.2f}"
        else:
            price = "Produit non trouvé ou erreur de scraping"
        return render_template('index.html', price=price, product_name=product_name)
    return render_template('index.html', price=None, product_name=None)

if __name__ == '__main__':
    app.run(debug=True)
