# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the cleaned dataset
df = pd.read_csv("imdb_clean.csv")

print(df.head())
print("Rows and Columns:", df.shape)

# Step 3: Exploratory Data Analysis (EDA)
print(df.describe())

# Ratings distribution
sns.histplot(df['averageRating'], bins=20, kde=True)
plt.savefig("ratings_distribution_clean.png")
plt.show()

# Top genres
df['genres'].value_counts().head(10).plot(kind='bar')
plt.savefig("top_genres_clean.png")
plt.show()

# Step 4: Analysis
print("\nTop 10 Movies by Rating:")
print(df.nlargest(10, 'averageRating')[['primaryTitle','averageRating']])

print("\nMost Common Genres:")
print(df['genres'].value_counts().head(5))

# Ratings trend over years
df.groupby('startYear')['averageRating'].mean().plot()
plt.savefig("ratings_trend_clean.png")
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

# Extra checks
print("\nWhich year had the most movies?")
print(df['startYear'].value_counts().head(10))

print("\nWhich genre has the highest average rating?")
print(df.groupby('genres')['averageRating'].mean().sort_values(ascending=False).head(10))
