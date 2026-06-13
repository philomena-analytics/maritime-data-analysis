# Maritime Patrol Analysis
# Author: Philomena
# Liberian Navy - Data Science Portfolio

# Sample patrol data (hours spent at sea each month)
patrol_hours = [45, 52, 38, 47, 55, 42, 48, 51, 44, 49, 53, 46]

# Month names
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Calculate basic statistics
total_hours = sum(patrol_hours)
average_hours = total_hours / len(patrol_hours)
max_hours = max(patrol_hours)
min_hours = min(patrol_hours)

# Print results
print("=" * 40)
print("MARITIME PATROL ANALYSIS REPORT")
print("=" * 40)
print(f"Total patrol hours for the year: {total_hours}")
print(f"Average patrol hours per month: {average_hours:.1f}")
print(f"Busiest month: {max_hours} hours")
print(f"Quietest month: {min_hours} hours")
print("=" * 40)

# Find which month had the highest patrol hours
max_index = patrol_hours.index(max_hours)
print(f"Month with most patrol activity: {months[max_index]}")

# Simple recommendation
if average_hours > 45:
    print("\nRecommendation: Patrol activity is high. Consider crew rotation.")
else:
    print("\nRecommendation: Patrol levels are sustainable.")
