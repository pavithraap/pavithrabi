# ==========================================
# STUDENT PLACEMENT ANALYSIS PROJECT
# ==========================================

# Import Libraries
from pathlib import Path

import pandas as pd
import numpy as np

# ------------------------------------------
# Project Files
# ------------------------------------------
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "Student_Placement_Analyst_Project FE Added and cleaned file.csv"

# ------------------------------------------
# Step 1: Read Dataset
# ------------------------------------------
if not DATA_FILE.is_file():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_FILE}\n"
        "Place the CSV file next to this script and run it again."
    )

student_placement_data = pd.read_csv(DATA_FILE)

# ------------------------------------------
# Step 2: Basic Information
# ------------------------------------------
print("\n========== FIRST 5 ROWS ==========")
print(student_placement_data.head())

print("\n========== LAST 5 ROWS ==========")
print(student_placement_data.tail())

print("\n========== DATASET SHAPE ==========")
print("Rows :", student_placement_data.shape[0])
print("Columns :", student_placement_data.shape[1])

print("\n========== COLUMN NAMES ==========")
print(student_placement_data.columns.tolist())

print("\n========== DATA TYPES ==========")
print(student_placement_data.dtypes)

print("\n========== DATASET INFO ==========")
print(student_placement_data.info())

# ------------------------------------------
# Step 3: Missing Values
# ------------------------------------------
print("\n========== MISSING VALUES ==========")
print(student_placement_data.isnull().sum())

# ------------------------------------------
# Step 4: Duplicate Records
# ------------------------------------------
print("\n========== DUPLICATE ROWS ==========")
print(student_placement_data.duplicated().sum())

# ------------------------------------------
# Step 5: Statistical Summary
# ------------------------------------------
print("\n========== NUMERICAL SUMMARY ==========")
print(student_placement_data.describe())

print("\n========== CATEGORICAL SUMMARY ==========")
print(student_placement_data.describe(include='object'))

# ------------------------------------------
# Step 6: Branch Wise Student Count
# ------------------------------------------
print("\n========== BRANCH WISE STUDENT COUNT ==========")
branch_count = student_placement_data['branch'].value_counts()
print(branch_count)

# ------------------------------------------
# Step 7: Placement Status Count
# ------------------------------------------
print("\n========== PLACEMENT STATUS ==========")
placement_count = student_placement_data['placement_status'].value_counts()
print(placement_count)

# ------------------------------------------
# Step 8: Gender Distribution
# ------------------------------------------
print("\n========== GENDER DISTRIBUTION ==========")
gender_count = student_placement_data['gender'].value_counts()
print(gender_count)

# ------------------------------------------
# Step 9: Average Salary by Company Type
# ------------------------------------------
print("\n========== COMPANY TYPE VS SALARY ==========")
company_salary = (
    student_placement_data
    .groupby('company_type')['salary_lpa']
    .mean()
)
print(company_salary)

# ------------------------------------------
# Step 10: CGPA Grade Distribution
# ------------------------------------------
if 'cgpa_grade' in student_placement_data.columns:
    print("\n========== CGPA GRADE ==========")
    print(student_placement_data['cgpa_grade'].value_counts())

# ------------------------------------------
# Step 11: Performance Category Distribution
# ------------------------------------------
if 'performance_category' in student_placement_data.columns:
    print("\n========== PERFORMANCE CATEGORY ==========")
    print(student_placement_data['performance_category'].value_counts())

# ------------------------------------------
# Step 12: Top 10 Performance Students
# ------------------------------------------
if 'performance_score' in student_placement_data.columns:
    print("\n========== TOP 10 STUDENTS ==========")

    top_students = (
        student_placement_data
        .sort_values(
            by='performance_score',
            ascending=False
        )
        .head(10)
    )

    print(
        top_students[
            ['student_id',
             'branch',
             'performance_score']
        ]
    )

# ------------------------------------------
# Step 13: Pivot Table Analysis
# ------------------------------------------
print("\n========== PIVOT TABLE ==========")

pivot_table = pd.pivot_table(
    student_placement_data,
    values='salary_lpa',
    index='branch',
    columns='placement_status',
    aggfunc='mean'
)

print(pivot_table)

# ------------------------------------------
# Step 14: Correlation Analysis
# ------------------------------------------
print("\n========== CORRELATION MATRIX ==========")

correlation = (
    student_placement_data
    .select_dtypes(include=np.number)
    .corr()
)

print(correlation)

# ------------------------------------------
# Step 15: Export Cleaned Analysis
# ------------------------------------------
student_placement_data.to_csv(
    PROJECT_DIR / "student_placement_final_analysis.csv",
    index=False
)

print("\n========== PROJECT COMPLETED ==========")
print("File exported successfully.")








                                               # Chart 1: Branch-wise Student Count



# import matplotlib.pyplot as plt

# # ==================================
# # BRANCH COUNT
# # ==================================

# branch_count = (
#     student_placement_data['branch']
#     .value_counts()
#     .sort_values(ascending=False)
# )

# # Professional Color Palette
# colors = [
#     '#4E79A7',   # Blue
#     '#F28E2B',   # Orange
#     '#59A14F',   # Green
#     '#E15759',   # Red
#     '#B07AA1',   # Purple
#     '#76B7B2'    # Teal
# ]

# # ==================================
# # PROFESSIONAL BAR CHART
# # ==================================

# plt.figure(figsize=(14,7))

# bars = plt.bar(
#     branch_count.index,
#     branch_count.values,
#     color=colors[:len(branch_count)],
#     width=0.8
# )

# # Title
# plt.title(
#     'Branch-wise Student Count',
#     fontsize=20,
#     fontweight='bold',
#     pad=20
# )

# # Axis Labels
# plt.xlabel(
#     'Branch',
#     fontsize=13,
#     fontweight='bold'
# )

# plt.ylabel(
#     'Student Count',
#     fontsize=13,
#     fontweight='bold'
# )

# # Grid
# plt.grid(
#     axis='y',
#     linestyle='--',
#     alpha=0.4
# )

# # Count Labels
# for bar in bars:

#     height = bar.get_height()

#     plt.text(
#         bar.get_x() + bar.get_width()/2,
#         height + 0.5,
#         str(int(height)),
#         ha='center',
#         va='bottom',
#         fontsize=11,
#         fontweight='bold'
#     )

# # Rotate X Labels
# plt.xticks(
#     rotation=0,
#     fontsize=11
# )

# plt.yticks(
#     fontsize=11
# )

# # Remove extra margins
# plt.tight_layout()

# plt.show()






# 2))))))))))))))))))))))))))))))))))))))))))))))))))))))


# Placement Status Count


# import matplotlib.pyplot as plt

# # ==================================
# # PLACEMENT STATUS COUNT
# # ==================================

# placement_count = (
#     student_placement_data['placement_status']
#     .value_counts()
# )

# # Professional Colors
# colors = [
#     '#59A14F',   # Green - Placed
#     '#E15759'    # Red - Not Placed
# ]

# # ==================================
# # PROFESSIONAL BAR CHART
# # ==================================

# plt.figure(figsize=(10,6))

# bars = plt.bar(
#     placement_count.index,
#     placement_count.values,
#     color=colors[:len(placement_count)],
#     width=0.6
# )

# # Title
# plt.title(
#     'Overall Placement Status Count',
#     fontsize=20,
#     fontweight='bold',
#     pad=20
# )

# # Axis Labels
# plt.xlabel(
#     'Placement Status',
#     fontsize=13,
#     fontweight='bold'
# )

# plt.ylabel(
#     'Number of Students',
#     fontsize=13,
#     fontweight='bold'
# )

# # Grid
# plt.grid(
#     axis='y',
#     linestyle='--',
#     alpha=0.4
# )

# # Value Labels
# for bar in bars:

#     height = bar.get_height()

#     plt.text(
#         bar.get_x() + bar.get_width()/2,
#         height + 1,
#         str(int(height)),
#         ha='center',
#         va='bottom',
#         fontsize=12,
#         fontweight='bold'
#     )

# # Remove extra margins
# plt.tight_layout()

# plt.show()






# 3))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

# Chart 3: Gender-wise Student Count


# import matplotlib.pyplot as plt

# # ==================================
# # GENDER COUNT
# # ==================================

# gender_count = (
#     student_placement_data['gender']
#     .value_counts()
#     .sort_values(ascending=False)
# )

# total = gender_count.sum()

# colors = [
#     '#4E79A7',
#     '#F28E2B'
# ]

# # ==================================
# # FIGURE
# # ==================================

# fig, ax = plt.subplots(figsize=(12,7))

# bars = ax.bar(
#     gender_count.index,
#     gender_count.values,
#     color=colors,
#     width=0.55
# )

# # ==================================
# # HEADER
# # ==================================

# ax.set_title(
#     'Gender-wise Student Count',
#     fontsize=20,
#     fontweight='bold',
#     pad=20
# )

# # ==================================
# # AXIS
# # ==================================

# ax.set_xlabel(
#     'Gender',
#     fontsize=13,
#     fontweight='bold'
# )

# ax.set_ylabel(
#     'Student Count',
#     fontsize=13,
#     fontweight='bold'
# )

# # ==================================
# # GRID
# # ==================================

# ax.grid(
#     axis='y',
#     linestyle='--',
#     alpha=0.3
# )

# # ==================================
# # LABELS
# # ==================================

# for bar in bars:

#     count = bar.get_height()

#     percentage = (
#         count / total
#     ) * 100

#     ax.text(
#         bar.get_x()+bar.get_width()/2,
#         count+1,
#         f'{count}\n{percentage:.1f}%',
#         ha='center',
#         fontsize=11,
#         fontweight='bold'
#     )

# # ==================================
# # REMOVE EXTRA BORDERS
# # ==================================

# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# # ==================================
# # FOOTER
# # ==================================

# plt.figtext(
#     0.5,
#     0.01,
#     'Student Placement Analysis Project',
#     ha='center',
#     fontsize=9
# )

# plt.tight_layout()

# plt.show()






# # 4))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))


# import matplotlib.pyplot as plt

# # ==================================
# # CGPA GRADE COUNT
# # ==================================

# cgpa_count = (
#     student_placement_data['cgpa_grade']
#     .value_counts()
#     .reindex([
#         'Average',
#         'Good',
#         'Very Good',
#         'Excellent'
#     ])
# )

# # Professional Colors
# colors = [
#     '#E15759',   # Average
#     '#F28E2B',   # Good
#     '#4E79A7',   # Very Good
#     '#59A14F'    # Excellent
# ]

# # ==================================
# # CREATE FIGURE
# # ==================================

# fig, ax = plt.subplots(figsize=(12,7))

# # ==================================
# # BAR CHART
# # ==================================

# bars = ax.bar(
#     cgpa_count.index,
#     cgpa_count.values,
#     color=colors,
#     width=0.6
# )

# # ==================================
# # TITLE
# # ==================================

# plt.suptitle(
#     'STUDENT PLACEMENT ANALYSIS',
#     fontsize=20,
#     fontweight='bold'
# )

# ax.set_title(
#     'CGPA Grade Distribution',
#     fontsize=15,
#     fontweight='bold',
#     pad=15
# )

# # ==================================
# # AXIS LABELS
# # ==================================

# ax.set_xlabel(
#     'CGPA Grade',
#     fontsize=12,
#     fontweight='bold'
# )

# ax.set_ylabel(
#     'Student Count',
#     fontsize=12,
#     fontweight='bold'
# )

# # ==================================
# # GRID
# # ==================================

# ax.grid(
#     axis='y',
#     linestyle='--',
#     alpha=0.3
# )

# # ==================================
# # COUNT LABELS
# # ==================================

# for bar in bars:

#     count = bar.get_height()

#     ax.text(
#         bar.get_x() + bar.get_width()/2,
#         count + 1,
#         str(int(count)),
#         ha='center',
#         va='bottom',
#         fontsize=11,
#         fontweight='bold'
#     )

# # ==================================
# # KPI BOXES
# # ==================================

# total = cgpa_count.sum()

# for i, grade in enumerate(cgpa_count.index):

#     percentage = (
#         cgpa_count.iloc[i] / total
#     ) * 100

#     ax.text(
#         1.02,
#         0.85 - i*0.18,
#         f"{grade}\n{percentage:.1f}%",
#         transform=ax.transAxes,
#         fontsize=10,
#         fontweight='bold',
#         color='white',
#         bbox=dict(
#             facecolor=colors[i],
#             edgecolor='black',
#             boxstyle='round,pad=0.5'
#         )
#     )

# # ==================================
# # REMOVE EXTRA BORDERS
# # ==================================

# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# plt.tight_layout()

# plt.show()









#  5: Company Type vs Average Salary


# # ==================================
# # COMPANY TYPE VS AVERAGE SALARY
# # ==================================

# import matplotlib.pyplot as plt

# company_salary = (
#     student_placement_data
#     .groupby('company_type')['salary_lpa']
#     .mean()
#     .sort_values(ascending=False)
# )

# colors = [
#     '#4E79A7',
#     '#F28E2B',
#     '#59A14F',
#     '#E15759',
#     '#B07AA1'
# ]

# fig, ax = plt.subplots(figsize=(12,7))

# bars = ax.bar(
#     company_salary.index,
#     company_salary.values,
#     color=colors[:len(company_salary)],
#     width=0.6
# )

# # Main Title
# plt.suptitle(
#     'STUDENT PLACEMENT ANALYSIS',
#     fontsize=20,
#     fontweight='bold'
# )

# # Subtitle
# ax.set_title(
#     'Company Type vs Average Salary',
#     fontsize=15,
#     fontweight='bold',
#     pad=15
# )

# # Axis Labels
# ax.set_xlabel(
#     'Company Type',
#     fontsize=12,
#     fontweight='bold'
# )

# ax.set_ylabel(
#     'Average Salary (LPA)',
#     fontsize=12,
#     fontweight='bold'
# )

# # Grid
# ax.grid(
#     axis='y',
#     linestyle='--',
#     alpha=0.3
# )

# # Salary Labels
# for bar in bars:

#     value = bar.get_height()

#     ax.text(
#         bar.get_x() + bar.get_width()/2,
#         value + 0.1,
#         f'{value:.1f}',
#         ha='center',
#         va='bottom',
#         fontsize=11,
#         fontweight='bold'
#     )

# # KPI Percentage Boxes
# total = company_salary.sum()

# for i, company in enumerate(company_salary.index):

#     percentage = (
#         company_salary.iloc[i] / total
#     ) * 100

#     ax.text(
#         1.02,
#         0.85 - i*0.15,
#         f"{company}\n{percentage:.1f}%",
#         transform=ax.transAxes,
#         fontsize=10,
#         fontweight='bold',
#         color='white',
#         bbox=dict(
#             facecolor=colors[i],
#             edgecolor='black',
#             linewidth=2,
#             boxstyle='round,pad=0.5'
#         )
#     )

# # Remove Extra Borders
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# plt.tight_layout()

# plt.show()








# 6 : Performance Category Count (📊 Bar Chart)




# import matplotlib.pyplot as plt

# performance_count = (
#     student_placement_data['performance_category']
#     .value_counts()
# )

# colors = [
#     '#59A14F',
#     '#4E79A7',
#     '#F28E2B',
#     '#E15759'
# ]

# fig, ax = plt.subplots(figsize=(12,7))

# bars = ax.bar(
#     performance_count.index,
#     performance_count.values,
#     color=colors[:len(performance_count)],
#     width=0.6
# )

# plt.suptitle(
#     'STUDENT PLACEMENT ANALYSIS',
#     fontsize=20,
#     fontweight='bold'
# )

# ax.set_title(
#     'Performance Category Distribution',
#     fontsize=15,
#     fontweight='bold'
# )

# ax.set_xlabel(
#     'Performance Category',
#     fontsize=12,
#     fontweight='bold'
# )

# ax.set_ylabel(
#     'Student Count',
#     fontsize=12,
#     fontweight='bold'
# )

# ax.grid(
#     axis='y',
#     linestyle='--',
#     alpha=0.3
# )

# for bar in bars:

#     count = bar.get_height()

#     ax.text(
#         bar.get_x()+bar.get_width()/2,
#         count+1,
#         str(int(count)),
#         ha='center',
#         fontweight='bold'
#     )

# total = performance_count.sum()

# for i, category in enumerate(performance_count.index):

#     percentage = (
#         performance_count.iloc[i]/total
#     )*100

#     ax.text(
#         1.02,
#         0.85-i*0.18,
#         f"{category}\n{percentage:.1f}%",
#         transform=ax.transAxes,
#         color='white',
#         fontsize=10,
#         fontweight='bold',
#         bbox=dict(
#             facecolor=colors[i],
#             edgecolor='black',
#             linewidth=2,
#             boxstyle='round,pad=0.5'
#         )
#     )

# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# plt.tight_layout()
# plt.show()







# 7: Placement Status Count (Pie Chart)



# import matplotlib.pyplot as plt

# # ==================================
# # PLACEMENT STATUS COUNT
# # ==================================

# placement_count = (
#     student_placement_data['placement_status']
#     .value_counts()
# )

# # Professional Colors
# colors = [
#     '#59A14F',   # Placed
#     '#E15759'    # Not Placed
# ]

# # ==================================
# # CREATE FIGURE
# # ==================================

# fig, ax = plt.subplots(figsize=(8,8))

# # ==================================
# # DONUT CHART
# # ==================================

# wedges, texts, autotexts = ax.pie(
#     placement_count.values,
#     labels=placement_count.index,
#     colors=colors,
#     autopct='%1.1f%%',
#     startangle=90,
#     pctdistance=0.78,      # Percentage position
#     labeldistance=1.08,    # Label position
#     wedgeprops=dict(
#         width=0.40,
#         edgecolor='white',
#         linewidth=2
#     ),
#     textprops={
#         'fontsize':12,
#         'fontweight':'bold'
#     }
# )

# # ==================================
# # CENTER TEXT
# # ==================================

# ax.text(
#     0,
#     0,
#     f'Total\n{placement_count.sum()}',
#     ha='center',
#     va='center',
#     fontsize=16,
#     fontweight='bold'
# )

# # ==================================
# # TITLE
# # ==================================

# plt.suptitle(
#     'STUDENT PLACEMENT ANALYSIS',
#     fontsize=20,
#     fontweight='bold',
#     y=0.97
# )

# ax.set_title(
#     'Placement Distribution',
#     fontsize=15,
#     fontweight='bold',
#     pad=20
# )

# # ==================================
# # ALIGNMENT FIX
# # ==================================

# for autotext in autotexts:
#     autotext.set_fontsize(11)
#     autotext.set_fontweight('bold')
#     autotext.set_color('black')

# for text in texts:
#     text.set_fontsize(12)
#     text.set_fontweight('bold')

# # Perfect circle
# ax.axis('equal')

# plt.tight_layout()

# plt.show()







# 8:Branch-wise Average Performance Score (Trend Chart)


# import matplotlib.pyplot as plt

# # ==================================
# # BRANCH-WISE PERFORMANCE
# # ==================================

# branch_performance = (
#     student_placement_data
#     .groupby('branch')['performance_score']
#     .mean()
#     .sort_values(ascending=False)
# )

# # ==================================
# # KPI VALUES
# # ==================================

# top_branch = branch_performance.idxmax()
# top_score = branch_performance.max()
# avg_score = branch_performance.mean()
# total_branches = len(branch_performance)

# # ==================================
# # DASHBOARD LAYOUT
# # ==================================

# fig = plt.figure(figsize=(16,8))

# gs = fig.add_gridspec(
#     4,
#     2,
#     width_ratios=[3,1]
# )

# # ==================================
# # LEFT : TREND CHART
# # ==================================

# ax = fig.add_subplot(gs[:,0])

# ax.plot(
#     branch_performance.index,
#     branch_performance.values,
#     marker='o',
#     linewidth=3
# )

# # Value labels
# for x, y in zip(
#         branch_performance.index,
#         branch_performance.values):

#     ax.text(
#         x,
#         y,
#         f'{y:.1f}',
#         ha='center',
#         va='bottom',
#         fontsize=10,
#         fontweight='bold'
#     )

# ax.set_title(
#     'Branch-wise Average Performance Trend',
#     fontsize=18,
#     fontweight='bold'
# )

# ax.set_xlabel(
#     'Branch',
#     fontsize=12,
#     fontweight='bold'
# )

# ax.set_ylabel(
#     'Performance Score',
#     fontsize=12,
#     fontweight='bold'
# )

# ax.grid(
#     linestyle='--',
#     alpha=0.3
# )

# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# # ==================================
# # RIGHT : KPI CARDS
# # ==================================

# kpis = [
#     ("Top Branch", top_branch),
#     ("Top Score", f"{top_score:.1f}"),
#     ("Average", f"{avg_score:.1f}"),
#     ("Branches", total_branches)
# ]

# colors = [
#     '#4E79A7',
#     '#59A14F',
#     '#F28E2B',
#     '#E15759'
# ]

# for i, (title, value) in enumerate(kpis):

#     ax_kpi = fig.add_subplot(gs[i,1])

#     ax_kpi.set_xticks([])
#     ax_kpi.set_yticks([])

#     ax_kpi.set_facecolor(colors[i])

#     for spine in ax_kpi.spines.values():
#         spine.set_visible(True)
#         spine.set_linewidth(2)
#         spine.set_edgecolor('black')

#     ax_kpi.text(
#         0.5,
#         0.70,
#         title,
#         ha='center',
#         va='center',
#         fontsize=12,
#         fontweight='bold',
#         color='white'
#     )

#     ax_kpi.text(
#         0.5,
#         0.30,
#         str(value),
#         ha='center',
#         va='center',
#         fontsize=18,
#         fontweight='bold',
#         color='white'
#     )

# # ==================================
# # HEADER
# # ==================================

# plt.suptitle(
#     'STUDENT PLACEMENT ANALYSIS DASHBOARD',
#     fontsize=22,
#     fontweight='bold'
# )

# plt.tight_layout()
# plt.show()







# 9: Performance Category Count - Donut+ KPI Cards


# import matplotlib.pyplot as plt

# # ==================================
# # PERFORMANCE CATEGORY COUNT
# # ==================================

# performance_count = (
#     student_placement_data['performance_category']
#     .value_counts()
# )

# # Professional Colors
# colors = [
#     '#59A14F',
#     '#4E79A7',
#     '#F28E2B',
#     '#E15759'
# ]

# # ==================================
# # DASHBOARD LAYOUT
# # ==================================

# fig = plt.figure(figsize=(16,8))

# gs = fig.add_gridspec(
#     4,
#     2,
#     width_ratios=[3,1]
# )

# # ==================================
# # LEFT : DONUT CHART
# # ==================================

# ax = fig.add_subplot(gs[:,0])

# wedges, texts, autotexts = ax.pie(
#     performance_count.values,
#     labels=performance_count.index,
#     colors=colors[:len(performance_count)],
#     autopct='%1.1f%%',
#     startangle=90,
#     pctdistance=0.80,
#     wedgeprops=dict(
#         width=0.40,
#         edgecolor='white',
#         linewidth=2
#     )
# )

# # Center text
# ax.text(
#     0,
#     0,
#     f'Total\n{performance_count.sum()}',
#     ha='center',
#     va='center',
#     fontsize=18,
#     fontweight='bold'
# )

# ax.set_title(
#     'Performance Category Distribution',
#     fontsize=18,
#     fontweight='bold'
# )

# # ==================================
# # RIGHT : KPI CARDS
# # ==================================

# total = performance_count.sum()

# for i, category in enumerate(performance_count.index):

#     ax_kpi = fig.add_subplot(gs[i,1])

#     ax_kpi.set_xticks([])
#     ax_kpi.set_yticks([])

#     ax_kpi.set_facecolor(colors[i])

#     for spine in ax_kpi.spines.values():
#         spine.set_visible(True)
#         spine.set_linewidth(2)
#         spine.set_edgecolor('black')

#     percentage = (
#         performance_count.iloc[i]
#         / total
#     ) * 100

#     ax_kpi.text(
#         0.5,
#         0.70,
#         category,
#         ha='center',
#         va='center',
#         fontsize=12,
#         fontweight='bold',
#         color='white'
#     )

#     ax_kpi.text(
#         0.5,
#         0.30,
#         f"{performance_count.iloc[i]}\n({percentage:.1f}%)",
#         ha='center',
#         va='center',
#         fontsize=15,
#         fontweight='bold',
#         color='white'
#     )

# # ==================================
# # HEADER
# # ==================================

# plt.suptitle(
#     'STUDENT PLACEMENT ANALYSIS DASHBOARD',
#     fontsize=22,
#     fontweight='bold'
# )

# plt.tight_layout()
# plt.show()






# 10: Overall student placement Analysis (Trend dashboard)


# import matplotlib.pyplot as plt

# # ==================================
# # OVERALL DATA
# # ==================================

# overall = (
#     student_placement_data
#     .groupby('branch')['performance_score']
#     .mean()
#     .sort_values(ascending=False)
# )

# total_students = len(student_placement_data)

# placed_students = (
#     student_placement_data['placement_status']
#     .eq('Placed')
#     .sum()
# )

# placement_rate = (
#     placed_students / total_students
# ) * 100

# top_branch = overall.idxmax()
# top_score = overall.max()

# avg_cgpa = (
#     student_placement_data['cgpa']
#     .mean()
# )

# avg_salary = (
#     student_placement_data['salary_lpa']
#     .mean()
# )

# avg_performance = (
#     student_placement_data['performance_score']
#     .mean()
# )

# # ==================================
# # DASHBOARD
# # ==================================

# fig = plt.figure(figsize=(18,9))

# gs = fig.add_gridspec(
#     5,
#     2,
#     width_ratios=[3,1]
# )

# # ==================================
# # LEFT : TREND
# # ==================================

# ax = fig.add_subplot(gs[:4,0])

# ax.plot(
#     overall.index,
#     overall.values,
#     marker='o',
#     linewidth=3,
#     markersize=8
# )

# for x, y in zip(
#         overall.index,
#         overall.values):

#     ax.text(
#         x,
#         y,
#         f'{y:.1f}',
#         ha='center',
#         va='bottom',
#         fontsize=10,
#         fontweight='bold'
#     )

# ax.set_title(
#     'Overall Student Performance Trend',
#     fontsize=18,
#     fontweight='bold'
# )

# ax.set_xlabel(
#     'Branch',
#     fontsize=12,
#     fontweight='bold'
# )

# ax.set_ylabel(
#     'Average Performance Score',
#     fontsize=12,
#     fontweight='bold'
# )

# ax.grid(
#     linestyle='--',
#     alpha=0.3
# )

# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# # ==================================
# # KPI CARDS
# # ==================================

# kpis = [
#     ("Students", total_students),
#     ("Placed", placed_students),
#     ("Placement %", f"{placement_rate:.1f}%"),
#     ("Top Branch", top_branch)
# ]

# colors = [
#     '#4E79A7',
#     '#59A14F',
#     '#F28E2B',
#     '#E15759'
# ]

# for i, (title, value) in enumerate(kpis):

#     axk = fig.add_subplot(gs[i,1])

#     axk.set_xticks([])
#     axk.set_yticks([])

#     axk.set_facecolor(colors[i])

#     for s in axk.spines.values():
#         s.set_linewidth(2)

#     axk.text(
#         0.5,
#         0.70,
#         title,
#         ha='center',
#         fontsize=12,
#         fontweight='bold',
#         color='white'
#     )

#     axk.text(
#         0.5,
#         0.30,
#         str(value),
#         ha='center',
#         fontsize=18,
#         fontweight='bold',
#         color='white'
#     )

# # ==================================
# # SUMMARY TABLE
# # ==================================

# ax_table = fig.add_subplot(gs[4,:])

# ax_table.axis('off')

# table_data = [[
#     f'{avg_cgpa:.2f}',
#     f'{avg_salary:.2f}',
#     len(overall),
#     f'{avg_performance:.2f}',
#     f'{top_score:.2f}'
# ]]

# columns = [
#     'Avg CGPA',
#     'Avg Salary',
#     'Branches',
#     'Avg Performance',
#     'Top Score'
# ]

# table = ax_table.table(
#     cellText=table_data,
#     colLabels=columns,
#     loc='center',
#     cellLoc='center'
# )

# table.auto_set_font_size(False)
# table.set_fontsize(11)
# table.scale(1,2)

# # ==================================
# # HEADER
# # ==================================

# plt.suptitle(
#     'STUDENT PLACEMENT ANALYSIS - EXECUTIVE DASHBOARD',
#     fontsize=22,
#     fontweight='bold'
# )

# plt.tight_layout()

# plt.show()








