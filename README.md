# 🎬 Netflix Analysis Project  

## 📌 Project Overview  
This project performs an **Exploratory Data Analysis (EDA)** on the **Netflix Movies & TV Shows dataset** from Kaggle.  
Using **Pandas, NumPy, Matplotlib, and Seaborn**, we explore trends, patterns, and insights about Netflix content.  

---

## 🛠️ Tools & Libraries  
- **Python** 🐍  
- **Pandas** → Data cleaning & preprocessing  
- **NumPy** → Numerical operations  
- **Matplotlib & Seaborn** → Data visualization  

---

## 📂 Dataset  
- Source: [Netflix Titles Dataset - Kaggle](https://www.kaggle.com/shivamb/netflix-shows)  
- Shape: **8807 rows × 12 columns**  
- Columns:  
  - `show_id`, `type`, `title`, `director`, `cast`,  
  - `country`, `date_added`, `release_year`,  
  - `rating`, `duration`, `listed_in`, `description`  

---

## 🔎 Data Cleaning Steps  
1. Filled missing values in `director`, `country`, `rating` with `"Unknown"` or `"Not Rated"`.  
2. Stripped extra spaces in `date_added` and converted to datetime.  
3. Extracted `year_added` from `date_added`.  
4. Handled invalid/missing values safely.  

---

## 📊 Exploratory Data Analysis (EDA)  

### ✅ 1. Movies vs TV Shows  
Visualized count of Movies and TV Shows available on Netflix.  

### ✅ 2. Top 10 Countries  
Identified countries contributing the most content.  

### ✅ 3. Content Over the Years  
Analyzed how Netflix’s library has grown over time.  

### ✅ 4. Most Common Genres  
Extracted and visualized top genres.  

### ✅ 5. Rating Distribution  
Studied how Netflix content is rated (TV-MA, PG, R, etc.).  

---

## 📈 Visualizations  
Some sample charts generated in this project:  
- Movies vs TV Shows distribution  
- Top 10 content-producing countries  
- Growth of content year-wise  
- Top genres on Netflix  
- Rating distribution  

---

## 📌 Insights  
1. Netflix has **more Movies than TV Shows**.  
2. **USA, India, and UK** are the top 3 countries producing Netflix content.  
3. Netflix’s library **expanded rapidly after 2015**.  
4. **Drama, Comedy, and International Movies** are the most common genres.  
5. Most shows are rated **TV-MA (Mature Audience)**.  

