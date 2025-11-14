
def build_sequences(interactions):
    # interactions: DataFrame with user_id, dish_id, order_time
    interactions_sorted = interactions.sort_values(['user_id','order_time'])
    sequences = interactions_sorted.groupby('user_id')['dish_id'].apply(lambda x: list(map(str, x))).tolist()
    return sequences
