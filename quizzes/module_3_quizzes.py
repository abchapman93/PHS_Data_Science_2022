from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest
from .free_text_test import FreeTextTest
from .select_multiple_quiz import SelectMultipleQuiz
from .value_test import ValueTest
from .quiz_hint import QuizHint
from datetime import datetime
import ipywidgets as widgets

quiz_relational_columns1 = SelectMultipleQuiz(
    description="The ID's of all patients who have had Covid-19.", shuffle_answer=False,
    answer=["subject_id", "diagnosis",],
    options=["subject_id", "diagnosis", "diagnosis.date", "encounter.date", "encounter_type"]
)

quiz_relational_columns2 = SelectMultipleQuiz(
    description="The number of outpatient encounters between January and May of 2022.",
    answer=["encounter_type", "encounter.date",],
    options=["subject_id", "diagnosis", "diagnosis.date", "encounter.date", "encounter_type"],
    shuffle_answer=False
)

quiz_relational_columns3 = SelectMultipleQuiz(
    description="The age at time of diagnosis for patients with cancer.",
    answer=["subject_id", "diagnosis", "diagnosis.date", "encounter_id", "encounter.date",],
    options=["subject_id", "diagnosis", "diagnosis.date", "encounter_id", "encounter.date",],
    shuffle_answer=False
)

quiz_simple_query_parts = SelectMultipleQuiz(
    shuffle_answer=False,
    description="Which clauses were included in the example query we ran?",
    answer=[
        "'SELECT' clause",
        "'FROM' clause",
        "'WHERE' clause",
        "'LIMIT' clause",
    ],
    options=[
        "'SELECT' clause",
        "'FROM' clause",
        "'JOIN' clause",
        "'WHERE' clause",
        "'ORDER' clause",
        "'LIMIT' clause",
    ]
)

quiz_tables_in_query = SelectMultipleQuiz(description="Which tables are used in the query above?",
                  answer=["d_patients", "admissions"],
                  options=["subject_id", "hospital_expire_flag", "dod"])

quiz_order_by_column = MultipleChoiceQuiz(
    "Which column is used in the query to sort the data?",
    answer="dod",
    options=["subject_id", "dob", "hospital_expire_flg"]
)


def test_query_result1_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. df should be a pandas DataFrame, not {type(actual)}")
        return
    if len(actual) != 25:
        print(f"Incorrect. df should have 25 rows. Your dataframe had {len(actual)}.")
        return

    if set(actual.columns) != {'hadm_id', 'subject_id', 'admit_dt', 'disch_dt'}:
        print(f"Incorrect. Your dataframe should have columns ['hadm_id', 'subject_id', 'admit_dt', 'disch_dt'], not {actual.columns}")
        return
    print("That is correct!")


test_query_result1 = ValueTest(validation_func=test_query_result1_validation_func)

quiz_fix_where_ambiguity = MultipleChoiceQuiz(options=["a", "b", "c", "a and b", "a, b, and c"], answer="a and b", shuffle_answer=False)


def test_fixed_where_ambiguity_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. df should be a pandas DataFrame, not {type(actual)}")
        return
    if len(actual) != 1:
        print(f"Incorrect. df should have 1 rows. Your dataframe had {len(actual)}.")
        return
    if set(actual.columns) != {'subject_id', 'dob', 'dod', 'admission_type_descr'}:
        print(
            f"Incorrect. Your dataframe should have columns ['subject_id', 'dob', 'dod', 'admission_type_descr'], not {actual.columns}")
        return
    if set(actual["subject_id"]) != {78}:
        print(f"Incorrect. Your dataframe should have one subject_id 78, not {actual.iloc[0]['subject_id']}")
        return
    print("That is correct!")


test_fixed_where_ambiguity = ValueTest(validation_func=test_fixed_where_ambiguity_validation_func)


def test_query_dob_descending(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. df should be a pandas DataFrame, not {type(actual)}")
        return
    if len(actual) != 3:
        print(f"Incorrect. df should have 3 rows. Your dataframe had {len(actual)}.")
        return
    if set(actual.columns) != {'subject_id', 'sex', 'dob', 'dod', 'hospital_expire_flg'}:
        print(
            f"Incorrect. Your dataframe should have columns ['subject_id', 'sex', 'dob', 'dod', 'hospital_expire_flg'], not {list(actual.columns)}")
        return
    if set(actual["subject_id"]) != {37, 78, 56}:
        print(f"Incorrect. Your dataframe should have subject_id's (37, 78, 56), not {tuple(actual['subject_id'])}")
        return
    if tuple(actual["subject_id"]) != (37, 78, 56):
        print(
            f"Incorrect. Your dataframe should have subject ids in the order (37, 78, 56), not {tuple(actual['subject_id'])}")
    print("That is correct!")

test_query_dob_descending = ValueTest(validation_func=test_query_dob_descending)

hint_d_patients_unq = QuizHint(
    hints=[
        widgets.HTML("""One option is to group by subject_id, count the number of rows per subject_id using .size(), and then take the max:</br>
        <p style="font-family:courier";>df_patients.groupby("subject_id").size().max()</br>>>> 1</p>"""),
        widgets.HTML("""Another option is to check whether the length of the set of subject_ids (which is deduplicated)
        equals the length of the entire table:</br>
        <p style="font-family:courier";>len(set(df_patients["subject_id"])) == len(df_patients)</br>>>> True</p>"""),
    ]
)


def validate_df_patients_renamed_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. df should be a pandas DataFrame, not {type(actual)}")
        return
    if len(actual) != 10:
        print(f"Incorrect. df should have 10 rows. Your dataframe had {len(actual)}.")
        return
    if {"date_of_birth", "date_of_death"}.difference(set(actual.columns)):
        print(
            f"Incorrect. Your dataframe should have columns 'date_of_birth' and 'date_of_death'. Your dataframe has columns {list(actual.columns)}")
        return
    print("That is correct!")


validate_df_patients_renamed = ValueTest(validation_func=validate_df_patients_renamed_validation_func)

hint_age_in_years = QuizHint(
    hints=[widgets.HTML("""In python, the following could would convert a variable called age_at_death_days into years:</br>
    <p style="font-family:courier";>age_at_death_days / 365</p>""")]
)

def test_age_at_death_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. df should be a pandas DataFrame, not {type(actual)}")
        return
    if len(actual) != 4000:
        print(f"Incorrect. df should have 4000 rows. Your dataframe had {len(actual)}.")
        return
    if "age_at_death" not in set(actual.columns):
        print(
            f"Incorrect. Your dataframe should have columns 'age_at_death'. Your dataframe has columns {list(actual.columns)}")
        return
    # Test value for a patient
    expected_value = 77.2247
    actual_value = actual.query("subject_id == 3").iloc[0]["age_at_death"]
    if expected_value != actual_value:
        print(f"Incorrect age at death for subject 3. Expected {expected_value}, got {actual_value}")
        return
    print("That is correct!")
test_age_at_death = ValueTest(validation_func=test_age_at_death_validation_func)

quiz_prop_hospital_expire_flg = MultipleChoiceQuiz(answer=0.41,
                                                  options=[0.59, 0.23, 1653])

hint_boxplot_age_death_by_sex = QuizHint(hints=[
    widgets.HTML("""One option is to use seaborn to create a visualization like this one:</br>
    <img src="./media/output_boxplot_age_death_sex.png" width="50%"></img>
    """)
])

quiz_count_n = MultipleChoiceQuiz(answer="There are 5,074 ICU admissions in MIMIC",
                  options=["There are 5,074 patients in MIMIC.", "There are 5,074 columns in `admissions`."])

quiz_count_ed_admit = MultipleChoiceQuiz(answer="3,193", options=["3,193", "5,074", "4,000", "2,000"])

quiz_count_admission_source = MultipleChoiceQuiz(description="How many admissions had a source from the emergency room/transfer from a hospital, respectively?",
                                                answer="3193; 957",
                                                options=["3193; 211", "616; 79", "957; 3193"])

hint_count_hospital_expire_by_sex = QuizHint(
    hints=[widgets.HTML("Your query should select from a single table and have two group by columns. It may also be useful to have a WHERE clause.")]
)

quiz_count_hospital_expire_by_sex = MultipleChoiceQuiz("How many female/male patients, respectively, died in the hospital?",
                  answer="809;841",
                  options=["1047;1290", "841;809", "10;3"])

quiz_error_ambiguous = MultipleChoiceQuiz("What do you think the error above means?",
                  answer="More than one table has a column subject_id",
                  options=["There is no column named subject_id", "There's no row where subject_id = 78"])

quiz_summary_stats_age_years = FreeTextTest("Enter the min, max, mean, and standard deviations of age at death in years. </br>Round to the nearest whole number and enter each separated by a comma (e.g., '10,45,22,3')",
                                           answer="0,105,72,16")

hint_plot_icd9_counts = QuizHint(
    hints=[
        widgets.HTML("""A good plot would look something like this. (Why is this better than a vertical bar plot?)</br>
        <img src="./media/hint_plot_icd9_counts.png"></img>""")
    ])

quiz_unique_icd = FreeTextTest(answer="3846")

quiz_total_icd9 = FreeTextTest(answer="53486")

hint_pna_by_sex = QuizHint(hints=[widgets.HTML("The sex variable can be found in the table d_patients.")])

quiz_count_pna_by_sex = FreeTextTest(description="How many <strong>distinct</strong> female patients had a code for pneumonia?",
                                     answer="430")

def test_pna_codes_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. pna_codes should be a pandas DataFrame, not {type(actual)}")
        return
    if len(actual) != 36:
        print(f"Incorrect. pna_codes should have 36 rows. Your dataframe had {len(actual)}.")
        return
    if len(actual.columns) != 2 or {"code", "description"}.intersection(set(actual.columns)) != {"code", "description"}:
        print(
            f"Incorrect. pna_codes should have exactly 2 columns: 'code' and 'description'. Your dataframe has columns {list(actual.columns)}")
        return
    if {"486", "482.41"}.difference(set(actual["code"])):
        print(
            f"Incorrect. pna_codes should include codes '486' and '482.41'. Your dataframe has columns {list(actual.columns)}")
        return
    print("That is correct!")
test_pna_codes = ValueTest(validation_func=test_pna_codes_validation_func)

quiz_icd9_join_d_patients = SelectMultipleQuiz("<h4>TODO</h4>Which column(s)can be used to join icd9 with d_patients?",
                  answer=["subject_id"],
                  options=['subject_id', 'hadm_id', 'sequence', 'code', 'description'],
                                                       shuffle_answer=False)

quiz_icd9_join_demographic_detail = SelectMultipleQuiz("<h4>TODO</h4>Which column(s)can be used to join icd9 with demographic_detail?",
                  answer=["subject_id", "hadm_id"],
                  options=['subject_id', 'hadm_id', 'sequence', 'code', 'description'],
                                                       shuffle_answer=False)

quiz_count_distinct = MultipleChoiceQuiz("<h4>TODO</h4>How would you interpret the result of the previous query?",
                                        answer="1,087 patients have had a code for diabetes",
                                        options=["1,087 hospitalizations have had a code for diabetes",
                                                "There are 1,087 unique codes for diabetes",])

quiz_pna_cmrbd = MultipleChoiceQuiz("What is the most common co-morbidity for patients with pneumonia codes? How many patients have that code?",
                  answer="CONGESTIVE HEART FAILURE UNSPECIFIED; 377",
                  options=["ATRIAL FIBRILLATION; 303", "CONGESTIVE HEART FAILURE UNSPECIFIED; 359", "ACUTE RESPIRATORY FAILURE; 359"])

hint_pna_prop_cmrbd = QuizHint(
    hints=[
        widgets.HTML("""One way to do this is to get the count of patients with a pneumonia code and then divide the DataFrame column "n" by this number</br>
        <img src="./media/hint_pna_prop_cmrbd.png" width="50%"></img>""")
    ])

def test_labs_28766_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. labs_28766 should be a pandas DataFrame, not {type(actual)}")
        return
    if len(actual) != 134:
        print(f"Incorrect. labs_28766 should have 36 rows. Your dataframe had {len(actual)}.")
        return
    if {"value", "loinc_code"}.intersection(set(actual.columns)) != {"value", "loinc_code"}:
        print(
            f"Incorrect. labs_28766 should include columns labenets.value and d_labitems.loinc_code. Your dataframe has columns {list(actual.columns)}")
        return
    if set(actual["hadm_id"]) != {28766}:
        print(
            f"Incorrect. labs_28766 should only have a single hadm_id, not {set(actual['hadm_id'])}"
        )
        return
    print("That is correct!")
test_labs_28766 = ValueTest(validation_func=test_labs_28766_validation_func)

quiz_category_glucose = FreeTextTest("What is the value of the category column for the LOINC code '2345-7'?", answer="CHEMISTRY")

quiz_avg_glucose = MultipleChoiceQuiz("What is the average value of '2345-7'?",
                  answer="134.33",
                  options=["2516", "286.11", "101.11"])

hint_viz_glucose = QuizHint(hints=[
    widgets.HTML("""One option is a histogram using seaborn:</br>
    <img src="./media/hint_hist_glucose.png" width="35%">
    """)
])

hint_summary_glucose = QuizHint(hints=[
    widgets.HTML("""The values will differ based on your random sample, but your output could look something like this:</br>
    <img src="./media/hint_glucose_summary.png" width="35%">
    """)
])

hint_glucose_value_by_flag = QuizHint(hints=[
    widgets.HTML("""Your output could look something like this:</br>
    <img src="./media/hint_output_glucose_value_by_flag.png" width="50%">
    """)
])

quiz_none_glucose = MultipleChoiceQuiz(answer="The test was normal.", options=["The patient didn't have any glucose.", "The results weren't entered in correctly.",])

quiz_coalesce_helloworld = MultipleChoiceQuiz(answer="'hello'", options=["'hello'", "'world'", "NULL"])


def test_glucose_coalesce_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. glucose2 should be a pandas DataFrame, not {type(actual)}")
        return
    if set(actual["flag"]) != {"abnormal", "normal"}:
        print(
            f"Incorrect. The flag column should have two values: 'abnormal' and 'normal'. Yours has {set(actual['flag'])}")
        return
    print("That is correct!")


test_glucose_coalesce = ValueTest(validation_func=test_glucose_coalesce_validation_func)

quiz_label_455 = MultipleChoiceQuiz("<h4>TODO</h4> What is the label for the itemid 455?",
                  answer="NBP",
                  options=['ABP', 'Arterial BP', 'NBP', 'Arterial BP #2'])

hint_systolic_v_diastolic = QuizHint(hints=[
    widgets.HTML("We looked at a similar problem in notebook 2.3 when we compared height and weight."),
    widgets.HTML("""Your visualization should look something like this:.</br>
    <img src="./media/hint_systolic_v_diastolic.png" width="50%">"""),
])

quiz_missing_bp = MultipleChoiceQuiz(answer="The results weren't measured or entered correctly.", options=["The patient didn't have any blood pressure.",
"The blood pressure was normal.",
                                                           "The results weren't measured or entered correctly.",])


quiz_coalesce_helloworld = MultipleChoiceQuiz(answer="'hello'", options=["'hello'", "'world'", "NULL"])