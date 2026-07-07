from src.core.product_scoring import ProductScorer

scorer = ProductScorer()

assert scorer.score(9,3,8,9,8) >= 80

print("All tests passed.")
