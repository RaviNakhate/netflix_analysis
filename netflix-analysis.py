import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

netflix = pd.read_csv("netflix_titles.csv")

print("\nDataset Shape:", netflix.shape)
print("\nColumns:", netflix.columns)
print("\nMissing Values:\n", netflix.isnull().sum())

# Data Cleaning
# Fill missing fields with 'Unknown'
netflix['director'] = netflix['director'].fillna('Unknown')
netflix['country']  = netflix['country'].fillna('Unknown')
netflix['rating']   = netflix['rating'].fillna('Not Rated')


# Drop rows with missing 'date_added' & convert to datetime
netflix['date_added'] = pd.to_datetime(
    netflix['date_added'].str.strip(), 
    errors='coerce'
)

# Extract Year from date_added
netflix['year_added'] = netflix['date_added'].dt.year

# Exploratory Data Analysis (EDA)
# Count of Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=netflix, palette='Set2')
plt.title('Movies vs TV Shows on Netflix')
plt.show()

# Top 10 Countries with most content
plt.figure(figsize=(10,5))
netflix['country'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries with Most Netflix Content')
plt.ylabel('Count')
plt.show()

# Content added over the years
plt.figure(figsize=(12,6))
sns.histplot(netflix['year_added'], bins=20, kde=False, color='orange')
plt.title('Content Added on Netflix Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.show()

# Most common genres
plt.figure(figsize=(12,6))
all_genres = netflix['listed_in'].str.split(',').explode().str.strip()
all_genres.value_counts().head(10).plot(kind='bar', color='purple')
plt.title('Top 10 Genres on Netflix')
plt.ylabel('Count')
plt.show()

# Rating distribution
plt.figure(figsize=(12,6))
sns.countplot(y='rating', data=netflix, order=netflix['rating'].value_counts().index, palette='coolwarm')
plt.title('Distribution of Content Ratings')
plt.show()

# Insights
print("\n📌 Insights:")
print("1. Netflix has more Movies than TV Shows.")
print("2. The USA, India, and UK are the top 3 countries contributing the most content.")
print("3. Netflix has added maximum content after 2015, showing rapid growth.")
print("4. Drama, Comedy, and International Movies are the most common genres.")
print("5. Most shows are rated 'TV-MA' (Mature Audience).")
