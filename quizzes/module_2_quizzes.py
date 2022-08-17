from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest
from .free_text_test import FreeTextTest
from .select_multiple_quiz import SelectMultipleQuiz
from .value_test import ValueTest
from .quiz_hint import QuizHint
from datetime import datetime
import ipywidgets as widgets

quiz_helpers_code = FreeTextTest(answer="from quizzes.module_2_quizzes import *")
quiz_helpers_code_mc = MultipleChoiceQuiz(answer="Imports a the contents of module_2_quizzes", options=["Imports a module called module_2_quizzes",
                                                                                "It is there for decoration."])

def validate_np_sd(func):
    import numpy
    try:
        assert func is numpy.std
        print("That is correct!")
    except AssertionError:
        print("That is incorrect. Check your sd function.")
test_np_sd = FunctionTest(validation_func=validate_np_sd)

quiz_shape_matrix = MultipleChoiceQuiz(answer="(2, 10)", options=["(10, 2)", "(2,)"])

quiz_data_type_matrix = MultipleChoiceQuiz(answer="numpy.ndarray", options=["numpy.matrix", "list", "tuple"])

quiz_shape_matrix_t = MultipleChoiceQuiz(answer="(10, 2)", options=["(2, 10)", "(10,)"])

test_matrix_first_row_all_cols = SelectMultipleQuiz(answer=["matrix[0 , :]", "matrix[0, 0: ]"], options=["matrix[0][:]", "matrix[0, 0: ]", "matrix[0:]"], shuffle_answer=False)


def test_severity_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.Series):
        print(f"Incorrect. Expected an object with type pd.Series, not {type(actual)}")
        return
    if actual.name != "severity":
        print(f"Incorrect. The column should be named 'severity', not '{actual.name}'")
        return
    expected_values = [40, 10, 20, 15, 50]
    if list(actual.values) != expected_values:
        print(f"Incorrect values. Expected {expected_values}, got {list(actual.values)}")
        return
    print("That is correct!")


test_severity = ValueTest(validation_func=test_severity_validation_func)

hint_severity_below_30= QuizHint(
    hints=[
        widgets.HTML("""Your output should look like this:</br>
        <img src="./media/output_filtered_severity.png" width="45%"></img>"""),
    ]
)

hint_change_plt_kwargs = QuizHint(
    hints=[
        widgets.HTML("""Your plot should look like this:</br>
        <img src="./media/output_plt_kwargs.png" width="45%"></img>"""),
    ]
)

hint_non_parallel_lines = QuizHint(
    hints=[
        widgets.HTML("""Your plot should look something like this:</br>
        <img src="./media/output_non_parallel_lines.png" width="45%"></img>"""),
    ]
)

hint_non_parallel_lines_seaborn = QuizHint(
    hints=[
        widgets.HTML("""Your plot should look something like this:</br>
        <img src="./media/output_non_parallel_lines_seaborn.png" width="45%"></img>"""),
    ]
)

hint_distplot = QuizHint(
    hints=[
        widgets.HTML("""Your plot should look something like this:</br>
        <img src="./media/output_distplot.png" width="45%"></img>"""),
    ]
)

hint_pois_barh = QuizHint(
    hints=[
        widgets.HTML("""Your plot should look something like this:</br>
        <img src="./media/output_pois_barh.png" width="45%"></img>"""),
    ]
)

hint_severity_plot = QuizHint(
    hints=[
        widgets.HTML("""Your plot should look something like this:</br>
        <img src="./media/output_pd_severity_plot.png" width="45%"></img>"""),
    ]
)

# 2.3
quiz_categorical = SelectMultipleQuiz(answer=("Gender", "Index"),
                   options=("Gender", "Height", "Weight", "Index"),
                   shuffle_answer=False)

quiz_index_0_3 = MultipleChoiceQuiz(description="How many subjects have an Index of 0, 3, and 5, respectively?",
                   answer="13, 68, 198",
                  options=["13, 68, 198", "68, 13, 198", "13, 22, 130"])

quiz_mean_height_index3 = MultipleChoiceQuiz(description="What is the mean height for subjects with an Index of 3?",
                  answer=175.99,
                  options=(173.88, 13.5,173.87))

quiz_median_weight_index5 = MultipleChoiceQuiz(description="What is the median height for subjects with an Index of 5?",
                  answer=159.5,
                  options=(190.0, 187.54,160.98))

quiz_max_height_f0 = MultipleChoiceQuiz(description="What is the max height for a female subject with an index of 0?",
                  answer=196,
                  options=(195, 197, 140))

hint_hist_index = QuizHint(hints=[
    widgets.HTML(
        """Your plot should look something like:</br>
        <img src="media/hint_output_index_hist.png" width="45%"></img>
        """)
    ])

hint_output_hw_scatter = QuizHint(hints=[
    widgets.HTML(
        """Your 3 plots should look something like these:</br>
        <img src="media/hint_output_hw_scatter.png"></img>
        """),
    widgets.HTML("""
    One way of filtering a dataset is using df.query("..."). Refer back to the previous notebooks for now to use this method.
    """)
    ])

def test_df_height_sqrd_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. Was expecting a pandas DataFrame, not {type(actual)}")
        return
    if "height_sqrd" not in actual.columns:
        print(f"Incorrect. df should have a column called 'height_sqrd'. Your dataframe has columns {list(df.columns)}")
        return
    if ((actual["Height"] ** 2) != (actual["height_sqrd"])).sum() > 0:
        print(f"'Height' and 'height_sqrd' do not always correspond. Check how you squared the 'Height' column.")
    print("That is correct!")
test_df_height_sqrd = FunctionTest(validation_func=test_df_height_sqrd_validation_func)

def test_bmi_validation_func(actual):
    import pandas as pd
    import numpy as np
    if not isinstance(actual, pd.Series):
        print(f"Check the datatype of bmi. Expected a pandas Series, got {type(actual)}")
    if len(actual) != 500:
        print(f"Expected 500 rows, got {len(actual)}")
    expected_values = np.array([31.70828379, 24.35542118, 32.14024836, 27.35042735, 27.47623981])
    if not all(np.round(expected_values, 5) == np.round(actual.values[:len(expected_values)], 5)):
        print(f"The first 5 rows of bmi don't match. \nExpected {expected[:5]}. \nGot {actual.iloc[:5].values}")
    print("That is correct!")

test_bmi = ValueTest(validation_func = test_bmi_validation_func)

# 2.4

ethnicity_descr_hint = QuizHint(hints=[
    widgets.HTML(
        """Your plot should look something like:</br>
        <img src="media/ethnicity_descr_counts.png"></img>
        """
    )
])

age_at_discharge_mc_quiz = MultipleChoiceQuiz("What are the mean and median ages at discharge?",
                                              answer="70.29; 73.41",
                                              options=["73.41; 70.29", "61.14; 105.42"],
                                              )

ethnicity_descr_hint = QuizHint(hints=[


    widgets.HTML(
        """Your plot should look something like:</br>
        <img src="media/ethnicity_descr_counts.png"></img>
        """
    )
])

age_at_discharge_mc = MultipleChoiceQuiz("What are the mean and median ages at discharge?",
                                         answer="70.29; 73.41",
                                         options=["73.41; 70.29", "61.14; 105.42"],

                                         )

age_at_discharge_viz_hint = QuizHint(description="Visualization hints",
        hints=[
            widgets.HTML("""One option is a histogram:</br>
            <img src="./media/age_at_discharge_hist.png"></img>
            """),
            widgets.HTML("""One option is a histogram:</br>
            <img src="./media/age_at_discharge_boxplot.png"></img>
            """),
        ]
        )

prop_pt_mortality_quiz = MultipleChoiceQuiz(description="What proportion of patients died in the hospital?",
            answer=0.33, options=[0.66, 0.43, 0.1])

age_at_discharge_mortality_hint = QuizHint(description="Visualization hints",
        hints=[
            widgets.HTML("""Your plot should look something like:</br>
            <img src="./media/age_at_discharge_proportions.png"></img>
            """)
        ]
        )

mortality_cols_quiz = SelectMultipleQuiz(answer=("time_discharge_to_death", "disch_dt", "dod"),
                  options=('subject_id', 'hadm_id', 'disch_dt', 'dod', 'sex', 'ethnicity_descr',
       'age_at_discharge', 'age_at_discharge_binned', 'pna',
       'time_discharge_to_death', 'mortality_30_day'), shuffle_answer=False)

in_hospital_mortality_hint = QuizHint(
    hints=[
        widgets.HTML("You could either represent this variable as an integer (0 or 1) or a boolean (True or False)."),
        widgets.HTML("If you have a Series and run `series1 == value`, you'll get back a Series of booleans indicating whether that row has that value."),
    ]
)

def test_in_hospital_mortality_validation_func(actual_df):
    import pandas as pd
    import numpy as np
    # Check that it's a Series
    if not isinstance(actual_df, pd.DataFrame):
        print(f"Incorrect value passed in. Data type should be pd.DataFrame, got {type(actual_df)}")
        return

    # Check that it has a column
    try:
        actual = actual_df["in_hospital_mortality"]
    except KeyError:
        print("Your DataFrame doesn't have a column named 'in_hospital_mortality'")
        return

    # Check that the column contains an acceptable datatype
    if actual.dtype not in ("int64", "float64", "bool"):
        print(f"Incorrect. 'in_hospital_mortality' should contain int, float, or bool, not {str(actual.dtype)}")
        return

    if len(actual_df) != 5074:
        print(f"Expected 5074 rows, got {len(actual_df)}")
        return

    # Check that the mean value is expected
    actual_mean = np.round(actual.mean(), 4)
    if actual_mean != 0.3285:
        print(f"Mean value of 'in_hospital_mortality' wasn't what was expected. Expected 0.3285, got {actual_mean}")
        return

    print("That is correct!")


age_at_discharge_mortality_quiz = SelectMultipleQuiz("What are the two age groups wwith the highest proportion of in-hospital mortality?",
                   answer=("<18", "91+"),
                   options=('<18', '18-35', '36-65', '66-90', '91+',),
                   shuffle_answer=False
                  )

test_in_hospital_mortality = ValueTest(validation_func=test_in_hospital_mortality_validation_func)

pna_prop = MultipleChoiceQuiz("What is the proportion of patients had pneumonia?",
            answer=0.2, options=[0.8, 0.33, 0.66])

time_to_death_viz_hint = QuizHint(description="Some hints for visualizing time to death.",
    hints=[
        widgets.HTML("""One option is a boxplot</br>:
    <img src="./media/time_discharge_to_death_boxplot.png"></img>
    """),
        widgets.HTML("""Another option is a histogram:</br>:
    <img src="./media/time_to_death_hist.png"></img>
    """)
          ]
)

time_to_death_mean_quiz = MultipleChoiceQuiz("What are the mean number of days from discharge to death for pneumonia positive and negative patients?",
             answer="254.1; 398.9",
             options=["398.9; 254.1", "35.0; 113.5", "113.5; 35.0"]
            )

in_hospital_mortality_rr_quiz = FreeTextTest(
    "What is the relative risk of in-hospital mortality for pneumonia positive vs pneumonia negative patients?</br>Round to 2 decimals.",
    answer=1.27

)

in_hospital_mortality_rr_interpretation_quiz = MultipleChoiceQuiz("The interpretation of the relative risk is:</br>Patients with pneumonia are ___ ___ than patients without pneumonia to die in the hospital.",
                   answer=" 1.27 times more likely",
                   options=["1.27 times less likely", "Similarly likely"]
                  )

