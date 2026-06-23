# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset (from imdb_datasets folder)
# Basics file = movie info (title, year, genre)
df_basics = pd.read_csv("imdb_datasets/title.basics.csv")

# Ratings file = ratings and votes
df_ratings = pd.read_csv("imdb_datasets/title.ratings.csv")

# Merge them together on the 'tconst' column (unique movie ID)
df = pd.merge(df_basics, df_ratings, on="tconst")

# Show first 5 rows and dataset size
print(df.head())
print("Rows and Columns:", df.shape)

# Step 3: Preprocessing (cleaning data)
df.dropna(inplace=True)          # remove missing values
df.drop_duplicates(inplace=True) # remove duplicate rows

# Step 4: Exploratory Data Analysis (EDA)
print(df.describe())             # summary statistics

# Ratings distribution
sns.histplot(df['averageRating'], bins=20, kde=True)
plt.savefig("ratings_distribution.png")   # save graph
plt.show()

# Top genres
df['genres'].value_counts().head(10).plot(kind='bar')
plt.savefig("top_genres.png")             # save graph
plt.show()

# Step 5: Analysis
print("Top 10 Movies by Rating:")
print(df.nlargest(10, 'averageRating')[['primaryTitle','averageRating']])

print("Most Common Genres:")
print(df['genres'].value_counts().head(5))

# Ratings trend over years
df.groupby('startYear')['averageRating'].mean().plot()
plt.savefig("ratings_trend.png")          # save graph
plt.show()

# 🎬 Movies
print("\nTop 10 Highest-Rated Movies:")
print(df.nlargest(10, 'averageRating')[['primaryTitle','averageRating']])

print("\nLowest-Rated Movies:")
print(df.nsmallest(10, 'averageRating')[['primaryTitle','averageRating']])

print("\nMovies with the Most Votes (Most Popular):")
print(df.nlargest(10, 'numVotes')[['primaryTitle','numVotes']])

print("\nMovies with the Fewest Votes (Hidden Gems):")
print(df.nsmallest(10, 'numVotes')[['primaryTitle','numVotes']])

# ⭐ Ratings
print("\nAverage Rating Overall:")
print(df['averageRating'].mean())

print("\nMovies with Rating Above 9 (Exceptional):")
print(df[df['averageRating'] > 9][['primaryTitle','averageRating']])

print("\nMovies with Rating Below 5 (Poorly Rated):")
print(df[df['averageRating'] < 5][['primaryTitle','averageRating']])

# 📅 Years
print("\nYears with the Most Movies:")
print(df['startYear'].value_counts().head(10))

print("\nYears with the Highest Average Rating:")
print(df.groupby('startYear')['averageRating'].mean().sort_values(ascending=False).head(10))

print("\nMovies Released Before 1950 with High Ratings:")
print(df[(df['startYear'] < 1950) & (df['averageRating'] > 8)][['primaryTitle','startYear','averageRating']])

print("\nMovies Released After 2010 with Most Votes:")
print(df[df['startYear'] > 2010].nlargest(10, 'numVotes')[['primaryTitle','startYear','numVotes']])

# 🎭 Genres
print("\nMost Common Genres:")
print(df['genres'].value_counts().head(10))

print("\nHighest-Rated Genres:")
print(df.groupby('genres')['averageRating'].mean().sort_values(ascending=False).head(10))

print("\nGenres with the Most Votes (Popularity):")
print(df.groupby('genres')['numVotes'].sum().sort_values(ascending=False).head(10))

print("\nCompare Average Rating of Action vs Romance:")
print(df[df['genres'].isin(['Action','Romance'])].groupby('genres')['averageRating'].mean())

print("\nMovies Belonging to Multiple Genres (Action, Adventure):")
print(df[df['genres'].str.contains('Action') & df['genres'].str.contains('Adventure')][['primaryTitle','genres','averageRating']])

# Top 10 Movies by Rating
print("Top 10 Movies by Rating:")
print(df.nlargest(10, 'averageRating')[['primaryTitle','averageRating']])

# Most Common Genres
print("Most Common Genres:")
print(df['genres'].value_counts().head(5))

# Ratings trend over years
df.groupby('startYear')['averageRating'].mean().plot()
plt.savefig("ratings_trend_final.png")    # save graph
plt.show()

# Which year had the most movies?
print(df['startYear'].value_counts().head(10))

# Which genre has the highest average rating?
print(df.groupby('genres')['averageRating'].mean().sort_values(ascending=False).head(10))

# Save cleaned dataset
df.to_csv("imdb_clean.csv", index=False)
