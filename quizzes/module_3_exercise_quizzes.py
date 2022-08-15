from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest
from .free_text_test import FreeTextTest
from .select_multiple_quiz import SelectMultipleQuiz
from .value_test import ValueTest
from .quiz_hint import QuizHint
from datetime import datetime
import ipywidgets as widgets

hint_mortality_by_race = QuizHint(hints=[
    widgets.HTML("""Your query should select from two tables and use a DISTINCT keyword to deduplicate patients who
    had multiple hospitalizations."""),
    widgets.HTML("""The column hospital_expire_flg means that the patient died in the hospital."""),
    widgets.HTML("""The first option is to aggregate in pandas. 
    If you have a binary column of 0 and 1's or TRUE and FALSE, 
    you can calculate the proportion with df["col_name"].mean().</br>
    Alternatively, you could everything in SQL using a 
    <a href="https://www.w3schools.com/sql/sql_case.asp" target="_blank">CASE WHEN</a> statement 
    (which we didn't cover in class)"""),
    widgets.HTML("""Here is an example of what a bar plot with all categories would look like: </br>
    <img src="./media/hint_barplot_prop_mortality.png" width="50%"></img>
    """),
])

hint_hematocrit_viz = QuizHint(hints=[
    widgets.HTML("""Your output should look something like this: </br>
    <img src="./media/hint_hematocrit_dist.png" width="50%"></img>""")
])

quiz_hematocrit_normal = MultipleChoiceQuiz("Among the 20,000 rows, how many have a 'Normal' result?", answer=11862,
                   options=[11862, 20000, 8088, 50])

quiz_count_abi = MultipleChoiceQuiz("How many rows are in abi before/after dropping missing values?",
                  answer="364; 189", options=["10000; 5000", "2632; 2632"])

hint_abi = QuizHint(hints=[
    widgets.HTML("""We did something similar in <a href="./03-Labs-and-Vitals.ipynb" target="_blank">03-Labs-and-Vitals</a>
    with systolic and diastolic blood pressure."""),
                widgets.HTML("""In a histogram, a larger number of bins shows more detail, a smaller number shows less. 
                Here are two examples of histograms for abi with different numbers of bins:</br>
                <img src="./media/hint_abi_hist.png" width="50%"></img>""")
])

hint_prevalence_by_race = QuizHint(hints=[
    widgets.HTML("""To do this, you'll need to use two different subqueries (one to get the total counts by ethnicity,
    another to get the counts of each disease by ethnicity) and join them together."""),
    widgets.HTML("""The first subquery should group by ethnicity_descr, the second should group by ethnicity_descr and ICD-9 code."""),
    widgets.HTML("""Here is a visualization showing the results: </br>
    <img src="./media/hint_prop_disease_by_race.png" width="50%"></img>""")
])

quiz_dx_prevalence_by_race = SelectMultipleQuiz(
    "Which of the diseases in question appear to be more prevalent among patients who are Black/African American?",
    answer=["Hypertensive chronic kidney disease"],
    options=[
        "Unspecified essential hypertension",
        "Congestive heart failure unspecified",
        "Atrial fibrillation",
        "Hypertensive chronic kidney disease",
        "Acute kidney failure, unspecified"

    ], shuffle_answer=False)