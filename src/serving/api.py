from fastapi import FastAPI
from .recommend import recommend_top_n


app = FastAPI(title="Food Recommendation API")


@app.get("/")
def root():
return {"status": "ok"}


@app.get("/recommend/{user_id}")
def recommend(user_id: int, n: int = 10):
recs = recommend_top_n(user_id, n)
return {"user_id": user_id, "recommendations": recs}
