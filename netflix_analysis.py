import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv("data/netflix_titles.csv")
df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

# Plot 1: Bar Chart of Type
type_counts = df['type'].value_counts()
plt.figure(figsize=(4, 3))
plt.bar(type_counts.index, type_counts.values, color=['blue', 'orange'])
plt.title('Values of Types')
plt.savefig('images/type-counts.png')
plt.tight_layout()
plt.show()

# Plot 2: Pie Chart of Ratings
ratings_count = df['rating'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(ratings_count, labels=ratings_count.index, autopct='%1.1f%%', startangle=90)
plt.title('Rating Distribution')
plt.savefig('images/ratings-count.png')
plt.tight_layout()
plt.show()

# Plot 3: Histogram of Movie Durations
movies_df = df[df['type'] == 'Movie'].copy()
movies_df['duration'] = movies_df['duration'].str.replace(' min', '').astype(int)
plt.figure(figsize=(8, 6))
plt.hist(movies_df['duration'], bins=30, color='green', edgecolor='black')
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Counts')
plt.savefig('images/movie-duration-distribution.png')
plt.tight_layout()
plt.show()

# Plot 4: Scatter Plot of Release Years
release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.scatter(release_counts.index, release_counts.values, color='purple')
plt.title('Release Year vs Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Counts')
plt.grid(linestyle='--', alpha=0.5)
plt.savefig('images/release-year-counts.png')
plt.tight_layout()
plt.show()

# Plot 5: Top 10 Countries
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.bar(country_counts.index, country_counts.values, color='cyan')
plt.title('Top 10 Countries with Most Shows')
plt.xlabel('Country')
plt.ylabel('Counts')
plt.savefig('images/top-10-countries.png')
plt.tight_layout()
plt.show()

# Plot 6: Content by Year (Movies vs TV Shows)
content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].plot(content_by_year.index, content_by_year['Movie'], label='Movies', color='blue')
ax[0].set_title('Number of Movies by Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('No of Movies')

ax[1].plot(content_by_year.index, content_by_year['TV Show'], label='TV Shows', color='orange')
ax[1].set_title('Number of TV Shows by Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('No of TV Shows')

plt.suptitle('Content by Year')
plt.tight_layout()
plt.savefig('images/content-by-year.png')
plt.show()
