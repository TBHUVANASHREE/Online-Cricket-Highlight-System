import pandas as pd
import time
import json

df = pd.read_excel("t20_full_match_dataset.xlsx")

prev_event = None
last_highlight = -10
highlights = []

# Player importance
player_weight = {
    "Kohli": 1.5,
    "Rohit": 1.4,
    "Gill": 1.2,
    "Hardik": 1.3,
    "Jadeja": 1.2
}

# -----------------------------
# SCORE FUNCTION (BALANCED)
# -----------------------------
def compute_score(row, prev_event):
    score = 0

    # Balanced event importance
    if row["Event"] == "SIX":
        score += 12
    elif row["Event"] == "FOUR":
        score += 8
    elif row["Event"] == "WICKET":
        score += 10   # reduced

    # Force boost SIX
    if row["Event"] == "SIX":
        score += 5

    # Death overs
    if row["Over"] >= 18:
        score += 6

    # Pressure
    pressure = row["RunsNeeded"] / max(row["BallsLeft"], 1)
    if pressure > 1.5:
        score += 6

    # Momentum
    if prev_event == "SIX" and row["Event"] == "SIX":
        score += 6

    # Player importance
    score *= player_weight.get(row["Batsman"], 1)

    return score


# Extra conditions
def is_critical(row):
    return row["RunsNeeded"] <= 10 and row["BallsLeft"] <= 6


print("📡 FINAL Highlight Engine Running...\n")

# -----------------------------
# MAIN LOOP
# -----------------------------
for i, row in df.iterrows():

    print(f"Ball {row['Over']}.{row['Ball']} → {row['Event']}")

    # ❌ Skip useless events
    if row["Event"] not in ["SIX", "FOUR", "WICKET"]:
        prev_event = row["Event"]
        continue

    score = compute_score(row, prev_event)

    # -----------------------------
    # PREVENT BAD PATTERNS
    # -----------------------------

    # ❌ Avoid 3 wickets in a row
    if len(highlights) >= 2:
        last_two = [h["event"] for h in highlights[-2:]]
        if last_two.count("WICKET") == 2 and row["Event"] == "WICKET":
            prev_event = row["Event"]
            continue

    # ❌ Avoid same player repeated wicket
    if len(highlights) >= 1:
        if highlights[-1]["batsman"] == row["Batsman"] and row["Event"] == "WICKET":
            prev_event = row["Event"]
            continue

    # -----------------------------
    # FINAL DECISION
    # -----------------------------
    if (
        score >= 12 or
        row["Event"] == "SIX" or
        (row["Event"] == "FOUR" and score >= 10) or
        is_critical(row)
    ):

        # Gap control
        if (i - last_highlight >= 2) or (score > 18):

            highlight = {
                "over": int(row["Over"]),
                "ball": int(row["Ball"]),
                "event": row["Event"],
                "batsman": row["Batsman"],
                "score": round(score, 2),
                "excitement": int(row["ExcitementScore"])
            }

            highlights.append(highlight)
            last_highlight = i

            print(f"🔥 Highlight Selected | {row['Event']} | Score {score}")

            # Save JSON
            with open("highlights.json", "w") as f:
                json.dump(highlights, f)

    prev_event = row["Event"]

    time.sleep(0.25)

print("\n✅ Simulation Complete")