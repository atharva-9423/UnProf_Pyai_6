# UnProf_Pyai_6
Python data analysis project using Pandas to read, clean, and summarize student marks from a CSV file.

<div align="center">

# 📚 Student Marks Analysis

A Python data analysis project built with **Pandas** that reads, cleans, and summarizes student marks from a CSV file.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Atharva%20Phatangare-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/atharva-phatangare)
[![GitHub](https://img.shields.io/badge/GitHub-atharva--9423-black?style=for-the-badge&logo=github)](https://github.com/atharva-9423/UnProf_Pyai_6)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-darkblue?style=for-the-badge&logo=pandas)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 📥 Read CSV | Loads student marks from `students.csv` using `read_csv()` |
| 🧹 Clean Data | Fills missing marks with subject-wise averages using `fillna()` |
| 📊 Subject Averages | Calculates average marks per subject |
| 🔗 Merge Data | Combines marks with student info (class, city) using `merge()` |
| 📍 City Analysis | Groups average performance by city using `groupby()` |
| 🏆 Summary Report | Shows top performers, weak students & grade distribution |

---

## 📺 Sample Output

```
📌 Subject-wise Average Marks:
-----------------------------------
  Math        :  78.38  ███████
  Science     :  82.50  ████████
  English     :  77.67  ███████
  History     :  82.62  ████████
  Geography   :  84.33  ████████

  Overall Class Average : 81.10
  Best Subject          : Geography
  Weakest Subject       : English

📌 Top 3 Performers:
-----------------------------------
  🏆 Fatima Sheikh        Avg: 93.4  Grade: A+
  🏆 Meena Joshi          Avg: 90.2  Grade: A+
  🏆 Ali Khan             Avg: 87.0  Grade: A
```

---

## 🧠 Concepts Used

- **DataFrame** — core Pandas data structure for tabular data
- **`read_csv()`** — loads CSV files into a DataFrame
- **`fillna()`** — replaces missing values with subject-wise mean
- **`groupby()`** — groups data by city to compare regional performance
- **`merge()`** — joins student marks with student info on `student_id`

---

## 📁 File Structure

```
📂 day-6/
├── student_analysis.py   ← Main analysis script
├── students.csv          ← Raw marks data (with missing values)
├── student_info.csv      ← Student details (class, section, city)
└── README.md             ← This file
```

---

## 🚀 How To Run

**Step 1** — Install dependencies:
```bash
pip install pandas
```

**Step 2** — Clone the repo and navigate to day-6:
```bash
git clone https://github.com/atharva-9423/Unprof_Pyai_6
cd
```

**Step 3** — Run the script:
```bash
python3 student_analysis.py
```

---

## 📅 Internship Context

Built as part of **Day 6 – Data Wrangling with Pandas** of my Python & AI Internship at **UnProf**.

---

<div align="center">

Made with ❤️ by **Atharva Phatangare**

[![LinkedIn](https://img.shields.io/badge/Let's%20Connect-LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/atharva-phatangare)
[![GitHub](https://img.shields.io/badge/More%20Projects-GitHub-black?style=for-the-badge&logo=github)](https://github.com/atharva-9423)

</div>
