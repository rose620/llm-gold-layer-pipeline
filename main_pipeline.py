import pandas as pd
from claude_utils import analyze_customer_feedback

# Simulate incoming data from a generic consumer pipeline
retail_silver_data = {
    'review_id': [101, 102],
    'review_text': [
        "The smart watch arrived 3 days late and the battery only lasts 2 hours. Extremely disappointed, returning immediately.",
        "Absolutely love this wireless speaker! The bass is incredible and it paired with my laptop instantly. Highly recommend."
    ]
}
df = pd.DataFrame(retail_silver_data)

print("Starting E-Commerce Gold Layer Pipeline processing via Claude API...\n")

# Map API function across the DataFrame rows
df['gold_layer_tags'] = df['review_text'].apply(analyze_customer_feedback)

print("--- Pipeline Execution Complete ---\n")

# Display the clean results cleanly on the terminal screen
for idx, row in df.iterrows():
    print(f"=== Review ID: {row['review_id']} ===")
    print(row['gold_layer_tags'])
    print("-" * 50)
