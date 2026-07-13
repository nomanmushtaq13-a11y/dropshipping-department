from dataclasses import dataclass

@dataclass
class Product:
    id: str
    product_name: str
    category: str
    target_country: str
    cost_usd: float
    selling_price_usd: float
    profit_margin: float
    demand_score: int
    competition_score: int
    organic_score: int
    supplier: str
    status: str = "Pending"
