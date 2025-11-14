import implicit
import scipy.sparse as sp
import pandas as pd


def build_interaction_matrix(interactions):
    # interactions: DataFrame with user_id, dish_id, quantity
    user_codes = interactions['user_id'].astype('category')
    dish_codes = interactions['dish_id'].astype('category')
    user_idx = user_codes.cat.codes
    dish_idx = dish_codes.cat.codes
    matrix = sp.coo_matrix((interactions['quantity'].astype(float), (user_idx, dish_idx)))
    return matrix.tocsr(), user_codes.cat.categories, dish_codes.cat.categories


def train_als(matrix, factors=64, regularization=0.01, iterations=20):
    model = implicit.als.AlternatingLeastSquares(factors=factors, regularization=regularization, iterations=iterations)
    # implicit expects item-user matrix
    model.fit(matrix.T)
    return model


def recommend_for_user(model, user_idx, user_items, K=10):
    # user_idx: integer internal id, user_items: scipy csr matrix
    recs = model.recommend(userid=user_idx, user_items=user_items, N=K)
    # returns list of (item_idx, score)
    return recs
