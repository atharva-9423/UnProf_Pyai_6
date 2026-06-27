import pandas as pd

MARKS_FILE = "students.csv"
INFO_FILE  = "student_info.csv"
SUBJECTS   = ["math", "science", "english", "history", "geography"]


def load_data():
    marks_df = pd.read_csv(MARKS_FILE)
    info_df  = pd.read_csv(INFO_FILE)
    print(f"✅ Loaded {len(marks_df)} student records.")
    return marks_df, info_df


def clean_data(df):
    print(f"\n⚠️  Missing values before cleaning:\n{df[SUBJECTS].isnull().sum().to_string()}")
    subject_means = df[SUBJECTS].mean()
    df[SUBJECTS]  = df[SUBJECTS].fillna(subject_means.round(2))
    print(f"\n✅ Missing values after cleaning:\n{df[SUBJECTS].isnull().sum().to_string()}")
    return df


def add_total_and_average(df):
    df["total"]   = df[SUBJECTS].sum(axis=1).round(2)
    df["average"] = df[SUBJECTS].mean(axis=1).round(2)
    return df


def get_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    elif avg >= 50: return "D"
    else: return "F"


def subject_wise_averages(df):
    return df[SUBJECTS].mean().round(2)


def generate_report(df, subject_avgs):
    df["grade"] = df["average"].apply(get_grade)

    print("\n" + "=" * 60)
    print("          📊 STUDENT MARKS ANALYSIS REPORT")
    print("=" * 60)

    print("\n📌 Subject-wise Average Marks:")
    print("-" * 35)
    for subject, avg in subject_avgs.items():
        bar = "█" * int(avg // 10)
        print(f"  {subject.capitalize():<12}: {avg:>6.2f}  {bar}")

    overall_avg = subject_avgs.mean()
    best_subject  = subject_avgs.idxmax().capitalize()
    weak_subject  = subject_avgs.idxmin().capitalize()

    print(f"\n  Overall Class Average : {overall_avg:.2f}")
    print(f"  Best Subject          : {best_subject}")
    print(f"  Weakest Subject       : {weak_subject}")

    print("\n📌 Top 3 Performers:")
    print("-" * 35)
    top3 = df.nlargest(3, "average")[["name", "average", "grade"]]
    for _, row in top3.iterrows():
        print(f"  🏆 {row['name']:<25} Avg: {row['average']}  Grade: {row['grade']}")

    print("\n📌 Students Needing Attention (Average < 70):")
    print("-" * 35)
    weak = df[df["average"] < 70][["name", "average", "grade"]]
    if weak.empty:
        print("  ✅ All students are performing well!")
    else:
        for _, row in weak.iterrows():
            print(f"  ⚠️  {row['name']:<25} Avg: {row['average']}  Grade: {row['grade']}")

    print("\n📌 Grade Distribution:")
    print("-" * 35)
    grade_counts = df["grade"].value_counts().sort_index()
    for grade, count in grade_counts.items():
        print(f"  Grade {grade} : {count} student(s)")

    print("\n" + "=" * 60)


def main():
    print("📚 Student Marks Analysis — Day 6 (Pandas)")
    print("-" * 45)

    marks_df, info_df = load_data()

    marks_df = clean_data(marks_df)

    marks_df = add_total_and_average(marks_df)

    merged_df = pd.merge(marks_df, info_df, on="student_id")
    print(f"\n✅ Merged with student info. Columns: {list(merged_df.columns)}")

    city_group = merged_df.groupby("city")["average"].mean().round(2)
    print(f"\n📍 Average Marks by City:\n{city_group.to_string()}")

    subject_avgs = subject_wise_averages(marks_df)
    generate_report(marks_df, subject_avgs)


if __name__ == "__main__":
    main()
