# 🎬 IMDb Analysis Project

## 📌 Overview
This project analyzes IMDb movie datasets using Python (Pandas, Matplotlib, Seaborn).  
It explores ratings, genres, years, and popularity trends.

## 🗂️ Project Structure
- **imdb_datasets/** → Original IMDb CSV files  
- **data_clean/** → Cleaned dataset (`imdb_clean.csv`)  
- **scripts/** → Python scripts (`imdb_analysis.py`, `imdb_analysis_clean.py`)  
- **reports/** → Metadata and quality reports (JSON files)  
- **visuals/** → Graphs (`ratings_distribution.png`, `top_genres.png`, etc.)

## ⚙️ Approach
1. Load raw IMDb datasets  
2. Clean missing values and duplicates  
3. Merge datasets into one (`imdb_clean.csv`)  
4. Perform exploratory data analysis (EDA)  
5. Answer questions:
   - Top 10 highest/lowest rated movies  
   - Most common genres  
   - Ratings distribution and trends over years  
   - Movies with most/fewest votes  
   - Genre comparisons (Action vs Romance, etc.)

📈 Visuals
Graphs are saved in the visuals/ folder:

Ratings distribution
Top genres
Ratings trend over years


## 🚀 How to Run
```bash
python scripts/imdb_analysis.py
python scripts/imdb_analysis_clean.py



