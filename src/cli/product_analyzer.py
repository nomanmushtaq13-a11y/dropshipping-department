from src.core.product_scoring import ProductScorer

print("=" * 50)
print("Product Analyzer v1.0")
print("=" * 50)

name = input("Product Name: ")
demand = int(input("Demand (0-10): "))
competition = int(input("Competition (0-10): "))
profit = int(input("Profit (0-10): "))
supplier = int(input("Supplier (0-10): "))
organic = int(input("Organic Potential (0-10): "))

score = ProductScorer().score(
    demand,
    competition,
    profit,
    supplier,
    organic
)

print("\nResult")
print("-" * 30)
print("Product :", name)
print("Score   :", score)

if score >= 80:
    print("Recommendation: APPROVED")
elif score >= 65:
    print("Recommendation: REVIEW")
else:
    print("Recommendation: REJECT")
