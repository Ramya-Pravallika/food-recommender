import numpy as np


def hybrid_score(embed_sim, cf_score, context_score, w1=0.5, w2=0.3, w3=0.2):
    return w1 * embed_sim + w2 * cf_score + w3 * context_score


def rank_candidates(candidate_ids, embeddings_model, cf_model, user_map, item_map, user_id, dish_features, context_fn, top_n=10):
    # candidate_ids: list of dish actual ids (int or str)
    scores = []
    # map user_id to internal idx for cf
    try:
        user_idx = list(user_map).index(user_id)
    except ValueError:
        user_idx = None

    for dish in candidate_ids:
        dish_key = str(dish)
        # embedding similarity: use most-similar to the dish itself as proxy (or compute cosine with user's history embedding)
        try:
            embed_sim = 0.6  # fallback
            if embeddings_model.wv.key_to_index.get(dish_key):
                # similarity with a proxy vector (here using the vector norm as placeholder)
                embed_sim = float(np.linalg.norm(embeddings_model.wv[dish_key])) / (np.sqrt(len(embeddings_model.wv[dish_key]))*10)
        except Exception:
            embed_sim = 0.1

        # cf score
        cf_score = 0.0
        if user_idx is not None:
            try:
                # use model.score if available else 0
                cf_score = cf_model.score(user_idx, list(item_map).index(dish)) if hasattr(cf_model, 'score') else 0.0
            except Exception:
                cf_score = 0.0

        context_score = context_fn(dish_features.get(dish, {}))
        final = hybrid_score(embed_sim, cf_score, context_score)
        scores.append((dish, final))

    ranked = sorted(scores, key=lambda x: x[1], reverse=True)
    return ranked[:top_n]
