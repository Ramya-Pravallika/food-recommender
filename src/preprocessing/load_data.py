import pandas as pd
from ..utils.config import load_config

cfg = load_config()

def load_raw():
    orders = pd.read_csv(cfg['data']['orders'], parse_dates=['order_time'])
    users = pd.read_csv(cfg['data']['users'], parse_dates=['registered_at'])
    dishes = pd.read_csv(cfg['data']['dishes'])
    interactions = pd.read_csv(cfg['data']['interactions'], parse_dates=['order_time'])
    return orders, users, dishes, interactions
