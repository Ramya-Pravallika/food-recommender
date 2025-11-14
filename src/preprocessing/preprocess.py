import pandas as pd
from ..preprocessing.load_data import load_raw
from ..preprocessing.build_sequences import build_sequences


def preprocess_and_save():
    orders, users, dishes, interactions = load_raw()
    # basic cleaning
    interactions = interactions.dropna(subset=['user_id','dish_id'])
    # save processed
    interactions.to_csv('data/processed/interactions.csv', index=False)
    sequences = build_sequences(interactions)
    # write sequences for item2vec training
    with open('data/processed/sequences.txt','w') as f:
        for seq in sequences:
            f.write(' '.join(seq) + '\n')
    print('Preprocessing complete. Processed files in data/processed/')

if __name__ == '__main__':
    preprocess_and_save()
