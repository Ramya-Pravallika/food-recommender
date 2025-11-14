
def compute_context_score(dish_row, user_profile):
    score = 0.0
    hour = user_profile.get('hour', 12)
    # simple peak hours example
    if 'peak_hours' in dish_row and hour in dish_row['peak_hours']:
        score += 0.2
    if dish_row.get('cuisine') == user_profile.get('fav_cuisine'):
        score += 0.3
    if dish_row.get('dish_id') in user_profile.get('repeat_items', []):
        score += 0.15
    return score
