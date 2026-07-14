def calculate(product):

    demand=float(product.get("demand_score",0))
    organic=float(product.get("organic_score",0))
    competition=float(product.get("competition_score",0))

    score=(demand*4)+(organic*4)+((10-competition)*2)

    return round(score,2)
