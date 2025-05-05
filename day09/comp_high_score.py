scores = {"A":95, "B": 80, "C": 65, "D": 88}

high_scores_loop = {}

for name,score in scores.items():
    if score>=85:
        high_scores_loop[name] = score
print(f"Loop High Scores: {high_scores_loop}")


high_scores_comp = {name: score for name, score in scores.items() if score>=85}
print(f"Comp high scores: {high_scores_comp}")

assert high_scores_loop == high_scores_comp