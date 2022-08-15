from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest
from .free_text_test import FreeTextTest
from .select_multiple_quiz import SelectMultipleQuiz
from .value_test import ValueTest
from .quiz_hint import QuizHint
from datetime import datetime
import ipywidgets as widgets

quiz_data_type_test_pt_roster = MultipleChoiceQuiz(description="What data type is `test_pt_roster`?", answer="dict",
                   options=["dict", "list", "set", "int"])

quiz_data_type_pt_roster_rachel = MultipleChoiceQuiz(description='What data type is `test_pt_roster["Rachel"]`?', answer="dict",
                   options=["dict", "list", "set", "int"])

quiz_data_type_severity = MultipleChoiceQuiz(description='What data type is `test_pt_roster["Rachel"]["severity"]`?', answer="int",
                   options=["dict", "list", "set", "int"])

test_rachel_age = FreeTextTest("What code would give you Rachel's age?", answer='pt_roster["Rachel"]["age"]')

test_laura_time = FreeTextTest("What code would give you Laura's arrival time?", answer='pt_roster["Laura"]["arrival_time"]')

hint_sort_severity = QuizHint(
    hints=[
        widgets.HTML("""One option is to use a for-loop and keep track of the highest/lowest scores you've seen and the corresponding names."""),
        widgets.HTML("""Here is the beginning of a block of code which uses the for-loop approach:
        <img src="./media/hint_sort_severity_loop.png" width="75%"></img>"""),
        widgets.HTML("""<strong>(Advanced)</strong> Another approach is to use the sorted() function with a custom key and a <em>lambda function</em>. 
        See <a target="_blank" href="https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/?ref=lbp">this article</a> for more information.""")
    ]
)

def _discretize_bmi(bmi):
    if bmi < 18.5:
        return "< 18.5"
    if bmi <= 24.9:
        return "18.5-24.9"
    if bmi <= 29.9:
        return "25.0-29.9"
    if bmi <= 39.9:
        return "30-39.9"
    return ">=40"


def _discretize_bmi(bmi):
    if bmi < 18.5:
        return "< 18.5"
    if bmi <= 24.9:
        return "18.5-24.9"
    if bmi <= 29.9:
        return "25.0-29.9"
    if bmi <= 39.9:
        return "30-39.9"
    return ">=40"


def test_discretize_bmi_validation_func(func):
    for val in range(0, 50, 5):
        actual = func(val)
        expected = _discretize_bmi(val)
        try:
            assert actual == expected
        except AssertionError:
            print(f"Incorrect. When bmi = {_discretize_bmi(val)}, got {func(val)} expected")
            return
    print("That is correct!")


test_discretize_bmi = FunctionTest(validation_func=test_discretize_bmi_validation_func)

def load_dx_subject_sets():
    fp = "../data/dx_subject_sets.csv"
    icd9_subject_sets = {
        "pneumonia": set(),
        "sepsis": set(),
        "respiratory": set()
    }
    with open(fp) as f:
        lines = f.read().splitlines()
    for line in lines[1:]:
        subject, dx = line.split(",")
        icd9_subject_sets[dx].add(int(subject))
    return icd9_subject_sets

test_dx_subject_counts = ValueTest(expected={'pneumonia': 318, 'sepsis': 911, 'respiratory': 1145})

test_pna_sepsis = FreeTextTest("How many patients have <strong>both</strong> pneumonia <strong>and</strong> sepsis?",
                              answer=137)

test_pna_sepsis_resp = FreeTextTest("How many patients have <strong>all 3 of</strong> pneumonia, sepsis, and respiratory disease?",
                              answer=110)

test_pna_or_sepsis_or_resp = FreeTextTest("How many patients have <strong>any of</strong> pneumonia, sepsis, and respiratory disease?",
                              answer=1671)

test_pna_only = FreeTextTest("How many patients have <strong>only</strong> pneumonia?",
                              answer=75)

test_dx_subject_probs = ValueTest(expected={'pneumonia': 0.19030520646319568,
 'sepsis': 0.5451825254338719,
 'respiratory': 0.6852184320766008}, show_answer=True)

hint_comorbidities = QuizHint(hints=[
    widgets.HTML("""Refer back to the set methods we learned earlier. Imagine this problem as a venn diagram. Which parts of the venn diagram are these questions describing?""")
])

hint_prob_icd = QuizHint(hints=[
   widgets.HTML("The probability of a patient having a disease can be calculated as the count of patients with the disease divided by the total number of patients (defined here as any of the patients in this dataset)."),
    widgets.HTML("We calculated the total number of patients in 3.3")
])