import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

os.makedirs('data/raw', exist_ok=True)

# parameters
n_users = 2000
n_dishes = 500
n_orders = 20000

np.random.seed(42)

# users
users = pd.DataFrame({
    'user_id': np.arange(1, n_users+1),
    'registered_at': [datetime(2020,1,1) + timedelta(days=int(x)) for x in np.random.randint(0,1000,n_users)],
    'city': np.random.choice(['Hyderabad','Bengaluru','Chennai','Mumbai'], size=n_users)
})
users.to_csv('data/raw/users.csv', index=False)

# dishes
cuisines = ['South Indian','North Indian','Chinese','Italian','Fast Food','Desserts']
D = []
for i in range(1, n_dishes+1):
    D.append({'dish_id': i, 'cuisine': np.random.choice(cuisines), 'price': round(np.random.uniform(50,500),2)})

dishes = pd.DataFrame(D)
dishes.to_csv('data/raw/dishes.csv', index=False)

# generate interactions (orders)
rows = []
for oid in range(1, n_orders+1):
    user = np.random.randint(1, n_users+1)
    order_time = datetime(2023,1,1) + timedelta(minutes=int(np.random.exponential(10000)))
    n_items = np.random.choice([1,2,3], p=[0.6,0.3,0.1])
    dishes_sample = np.random.choice(np.arange(1, n_dishes+1), size=n_items, replace=False)
    for d in dishes_sample:
        rows.append({'order_id': oid, 'user_id': user, 'dish_id': d, 'order_time': order_time, 'quantity': 1})

interactions = pd.DataFrame(rows)
interactions.to_csv('data/raw/interactions.csv', index=False)

# orders table
orders = interactions.groupby('order_id').agg({'user_id':'first','order_time':'first'}).reset_index()
orders.to_csv('data/raw/orders.csv', index=False)

print('Sample data generated in data/raw/')
