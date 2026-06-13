# Liberia Port Data Analysis
# Author: Philomena
# Liberian Navy - Data Science Portfolio

import pandas as pd

# Load the port data
# Note: Replace the filename with your actual CSV filename
file_path = "data/liberia-port-data.csv"

try:
    df = pd.read_csv(file_path)
    print("✅ Data loaded successfully!")
    print("\n" + "=" * 50)
    print("LIBERIA PORT ACTIVITY DATA")
    print("=" * 50)
    
    # Show basic information
    print(f"\n📊 Number of rows: {len(df)}")
    print(f"📊 Number of columns: {len(df.columns)}")
    
    # Show column names
    print("\n📋 Columns in this dataset:")
    for col in df.columns:
        print(f"   - {col}")
    
    # Show first 5 rows
    print("\n🔍 First 5 rows of data:")
    print(df.head())
    
    # Show last 5 rows
    print("\n🔍 Last 5 rows of data:")
    print(df.tail())
    
    # Basic statistics
    print("\n📈 Basic Statistics:")
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 0:
        for col in numeric_cols:
            print(f"\n   {col}:")
            print(f"      Min: {df[col].min()}")
            print(f"      Max: {df[col].max()}")
            print(f"      Average: {df[col].mean():.2f}")
    else:
        print("   No numeric columns found for statistics")
    
    print("\n" + "=" * 50)
    print("✅ Exploration complete!")
    
except FileNotFoundError:
    print(f"❌ File not found: {file_path}")
    print("Make sure the CSV file is in the 'data' folder")
    print("Check that the filename matches exactly")
    
except Exception as e:
    print(f"❌ An error occurred: {e}")
