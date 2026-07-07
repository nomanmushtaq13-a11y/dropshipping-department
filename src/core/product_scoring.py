class ProductScorer:
    def __init__(self):
        self.weights = {
            "demand": 30,
            "competition": 20,
            "profit": 20,
            "supplier": 10,
            "organic": 20,
        }

    def score(self, demand, competition, profit, supplier, organic):
        score = (
            (demand / 10) * self.weights["demand"] +
            ((10 - competition) / 10) * self.weights["competition"] +
            (profit / 10) * self.weights["profit"] +
            (supplier / 10) * self.weights["supplier"] +
            (organic / 10) * self.weights["organic"]
        )

        return round(score, 2)

if __name__ == "__main__":
    scorer = ProductScorer()
    total = scorer.score(
        demand=9,
        competition=3,
        profit=8,
        supplier=9,
        organic=8
    )

    print("Final Score:", total)
