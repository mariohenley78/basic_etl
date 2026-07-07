import pandas as pd

sales = pd.DataFrame({
    'sale_id': [1, 2, 3],
    'product_id': [101, 102, 101],
    'amount': [1, 2, 1]
})

products = pd.DataFrame({
    'product_id': [101, 102],
    'product_name': ['Apple', 'Banana']
})

# Hacé un merge para traer el nombre del producto a sales
# Usá how='left'
sales_enriched = None
sales_enriched = pd.merge (sales, products, on='product_id', how='left')
print(sales_enriched)