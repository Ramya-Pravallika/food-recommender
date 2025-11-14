from sklearn.metrics import precision_score, recall_score


def precision_at_k(true_items, predicted_items, k=10):
predicted_k = predicted_items[:k]
return len(set(true_items) & set(predicted_k)) / float(k)


def recall_at_k(true_items, predicted_items, k=10):
predicted_k = predicted_items[:k]
return len(set(true_items) & set(predicted_k)) / len(true_items)
