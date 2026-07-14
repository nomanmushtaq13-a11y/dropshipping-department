from src.services.product_score import calculate

def approve(product):

    score=calculate(product)

    if score>=80:
        return "Approved"

    if score>=60:
        return "Research"

    return "Rejected"
