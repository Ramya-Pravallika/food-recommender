# 🍽️ Food Recommendation Engine for Marketplace Personalization  
### Hybrid ML System — item2vec + Collaborative Filtering + Contextual Ranking  
![Python](https://img.shields.io/badge/Python-3.10-blue) 
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Status](https://img.shields.io/badge/Build-Production_Ready-brightgreen)

---

## 📌 Overview  
This repository contains a **production-ready end-to-end Recommendation System** built for food-delivery marketplaces such as **Swiggy, Zomato, UberEats**, etc.

The system delivers **personalized Top-N dish recommendations** using a hybrid ML approach:

- 🧠 **item2vec dish embeddings** (trained from user order sequences)  
- 🔍 **Collaborative Filtering (Implicit ALS)**  
- 🎯 **Contextual ranking** (time of day, cuisine preferences, repeat habits)  
- ⚡ **Hybrid scoring** combining similarity, affinity, and context  
- 🚀 **FastAPI inference service**  
- 🧪 **A/B testing with CUPED** for variance reduction  
- 🐳 **Dockerized deployment** for production use  

This project is built using **ML Engineering best practices** and is designed to be portfolio-ready & interview-ready.

---

# 🔧 Tech Stack

| Layer | Tech |
|------|------|
| Embeddings | Gensim item2vec |
| Collaborative Filtering | Implicit ALS |
| Contextual Modeling | Python custom logic |
| API / Serving | FastAPI + Uvicorn |
| Storage | SQL + CSV |
| Deployment | Docker + docker-compose |
| Experimentation | CUPED, A/B Testing |
| Evaluation | sklearn metrics |

---

#Sample Output 
<img width="446" height="312" alt="image" src="https://github.com/user-attachments/assets/255311f9-e96c-48f3-82dd-17f0fef5e70f" />

