from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest
from .free_text_test import FreeTextTest
from .select_multiple_quiz import SelectMultipleQuiz
from .value_test import ValueTest
from .quiz_hint import QuizHint
from datetime import datetime
import ipywidgets as widgets

test_day_of_week = MultipleChoiceQuiz(description="What day of the week is it?",
                   answer=datetime.now().strftime('%A'),
                  options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                  show_answer=True)

test_state = FreeTextTest(description="What state are we in? (No abbreviations!)",
             answer="Utah")

prime_mc = SelectMultipleQuiz("Which of the following numbers are prime? (Select all that apply.)",
                   answer=[2, 3, 5],
                  options=[2, 3, 4, 5, 6],
                  shuffle_answer=False)

quiz1 = MultipleChoiceQuiz(
    description='<strong>1.</strong> What class is x? </br><p style="font-family:courier";>x = 3</p>',
    options=["int", "float", "str", "list"],
    answer="int"
)

quiz2 = MultipleChoiceQuiz(
    description='<strong>2.</strong> What class is x? </br><p style="font-family:courier";>x = 3.0</p>',
    options=["int", "float", "str", "list"],
    answer="float"
)

quiz_keyword_positional_args = SelectMultipleQuiz("Which of the following are valid calls to print_name? (ie., they won't throw an error)",
                     answer={
                         """print_name("Alec", "Chapman")""",
                         """print_name("Alec", last="Chapman", middle="B.")""",
                         """print_name(last="Alec", middle="Chapman", first="B.")""",

                     },
                     options={
                         """print_name(last="Chapman")""",
                         """print_name(first="Alec", "Chapman")""",
                     }

                     )

test_max = FunctionTest(args=([1,2,3],), expected=3)

test_x_equals_3 = ValueTest(3, show_answer=True)

test_square_2 = ValueTest(4, show_answer=True)

test_add_3_5 = ValueTest(8, show_answer=True)

test_square_add_3_5 = ValueTest(64, show_answer=True)


def test_add_validation_func(add_submitted):
    import random
    pairs = zip(random.sample(range(0, 100), 10), random.sample(range(0, 100), 10))
    for (x, y) in pairs:
        actual = add_submitted(x, y)
        expected = x + y
        if actual != expected:
            print(f"Incorrect value. Expected {x} + {y} = {expected}, got {actual}")
            return
    print("Correct!")

x_y_changing_var_quiz = MultipleChoiceQuiz(description='What is the value of: <p style="font-family:courier";>add(x,y)</p>',
                   options=[11, 12, 4, 9], answer=11)

test_r_equals_2 = ValueTest(2, True)
test_pi_equals = ValueTest(3.14, True)

quiz_data_type_2_pi_r = MultipleChoiceQuiz(description='What data type is: <p style="font-family:courier";>2*r*pi</p>', answer="float",
                  options=["int", "float", "variable", "other"])

quiz_2_pi_r_part2 = MultipleChoiceQuiz(description='How about: <p style="font-family:courier";>int(2*float(r)*int(pi))</p>',
                   answer="int",
                  options=["int", "float", "variable", "other"])

quiz_y_gt_z = FreeTextTest(description="What code would test whether y is greater than z?",
                          answer=["y>z", "z<y"],
                          preprocessor=lambda x:x.replace(" ", ""))

quiz_y_lte_z = FreeTextTest(description="What code would test whether z less than or equal to y?",
                          answer=["z<=y", "y>=z"],
                          preprocessor=lambda x:x.replace(" ", ""))

quiz_y_ne_z = FreeTextTest(description="What code would test whether z is not equal to y?",
                          answer=["z!=y", "y!=z"],
                          preprocessor=lambda x:x.replace(" ", ""))

test_add_function = FunctionTest(validation_func=test_add_validation_func)

test_random_list_smallest = ValueTest(expected=[10, 12, 13], show_answer=True)

test_random_list_largest = ValueTest(expected=[92, 97, 97], show_answer=True)

quiz_tup_append = MultipleChoiceQuiz(answer="An error will be raised.", options=["x_tup will equal (1,2,3,4)", "Nothing.", "A new tuple will be returned"])

quiz_set_tup_index = MultipleChoiceQuiz(answer="An error will be raised.", options=["x_tup will equal (1,'a', 3)", "Nothing.", "A new tuple will be returned"])

quiz_x_tup_4_5 = MultipleChoiceQuiz(answer="b", options=["a", "b", "c", "a and b", "All of the above", "None of the above"], shuffle_answer=False)

quiz_type_sorted_tup = MultipleChoiceQuiz(answer="list", options=["tuple", "list", "other"])

test_x_list = ValueTest(expected=[1, 2, 3])

quiz_test_x_list_equals_x = FreeTextTest(description="What code tests whether x_list equals x?", answer="x_list == x", preprocessor=lambda x:x.replace(" ",""))

quiz_x_equals_x_list = MultipleChoiceQuiz(description="Are x and x_list equal?", options=["Yes", "No"], answer="Yes", shuffle_answer=False)

quiz_code_1_in_primes = FreeTextTest(description="What code would check whether 1 is in primes?", answer="1 in primes")

quiz_1_in_primes = MultipleChoiceQuiz(description="What is the value of the code from the answer above?",
                  answer=False,
                  options=[True, False], shuffle_answer=False)

quiz_evens0 = MultipleChoiceQuiz(answer="An error would be raised.", options=["2", "4", "{2,4,6,8,10}"])

test_even_primes = ValueTest(expected={2}, show_answer=True)

quiz_len_odds_evens = FreeTextTest(answer=0)

test_primes_not_odd = ValueTest(expected={2})

test_len_pno_ep = FreeTextTest(answer=0)

test_naturals_10 = ValueTest(expected={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, show_answer=True)

test_num_unq_cities = ValueTest(expected=5)

test_capital_pa = FreeTextTest(answer='state_capitals["Pennsylvania"]')

test_capital_idaho = ValueTest(expected="Boise")

quiz_state_capitals2_ny = MultipleChoiceQuiz(answer="'New York City'", options=["An error would be raised.", "'Albany'", "['Albany', 'New York City']"])

quiz_code_rachel_arrival = FreeTextTest("What code would give you the arrival time for Rachel?", answer='pt_arrivals["Rachel"]')

test_check_pt_name = FreeTextTest(description="What code would check if there is someone named 'Jacob' in our arrivals dictionary?",
            answer=["'Jacob' in pt_arrivals.keys()", "'Jacob' in pt_arrivals"])

quiz_jacob_in_dict = MultipleChoiceQuiz("What would the answer to the code above be?",
                   answer=False, options=[True, False], shuffle_answer=False)

test_check_pt_time = FreeTextTest(description="What code would check if someone arrived at 7:00?",
            answer="'7:00' in pt_arrivals.values()")

quiz_dict_data_types = MultipleChoiceQuiz("What are the data types of the keys and values in the code above?",
                  answer="str; set",
                  options=["str; str", "str; dict", "dict; dict"])

quiz_type_states_utah = MultipleChoiceQuiz('With the dictionary above, what is the data type of: <p style="font-family:courier";>states["Utah"]</p>',
                  answer="dict", options=["str", "int", "list"]
                  )

quiz_second_element_x = FreeTextTest(description="What code would give you the second element of `x`?", answer="x[1]")

quiz_data_types_z = MultipleChoiceQuiz(description="What are the data types of the three elements of `z`?",
                                       answer="int; str; list",
                                       options=[
                                           "int; str; list",
                                           "str; str; str",
                                           "Invalid: A list can't have different data types."

                                       ])

quiz_x3 = MultipleChoiceQuiz(answer="An error would be raised.", options=[
    "An error would be raised.",
    "3",
    "1 (indexing would start over)",
    "None"
])

quiz_largest_idx_x = FreeTextTest(answer="2")

quiz_second_to_last_x = MultipleChoiceQuiz(answer="All of the above.", options=[ "a)", "b)", "c)", "All of the above."])

quiz_values_of_2 = MultipleChoiceQuiz(answer="a), b), and d)", options=["a), b), and d)", "a) and c)", "b)", "c)", "All of them"])

test_x_sub1 = ValueTest(expected=[2, 3])

quiz_x_colon = MultipleChoiceQuiz(answer="[1,2,3]", options=["[2]", "[1, 2]", "An error will be raised."])

quiz_next_patient2 = MultipleChoiceQuiz(answer="Jim", options=["Jim", "Mary", "Chloe", "Rachel"])


def test_waiting_list_jacob_validation_func(waiting_list):
    if not isinstance(waiting_list, list):
        print(f"Incorrect data type for `waiting_list`. Expected list, got {type(waiting_list)}")
    if len(waiting_list) != 5:
        print(f"Incorrect number of elements. Got {len(waiting_list)} elements, expected 5.")
    if waiting_list[-1] != "Jacob":
        print(f"Expected last value to be 'Jacob', not {waiting_list[-1]}")
    print("That is correct!")

test_waiting_list_jacob = ValueTest(validation_func=test_waiting_list_jacob_validation_func)

test_next_patient3 = ValueTest("Jacob")

test_list_a_added_to_b = ValueTest(expected=["a", "b", "c", 1, 2, 3])

test_list_a_b_added_to_c = ValueTest(expected=[2, 4, '6', 1, 2, 3, 'a', 'b', 'c'])

quiz_min_max_waiting_list = MultipleChoiceQuiz(answer="'Chloe'; 'Rachel'", options=["An error would be raised.", "'Jim'; 'Jacob'"])

quiz_ca_population = FreeTextTest("What code would give you the population of California?", answer='states["California"]["population"]')

test_cities_ut_pa = ValueTest({'Erie',
 'Harrisburg',
 'Ogden',
 'Park City',
 'Philadelphia',
 'Pittsburgh',
 'Provo',
 'Salt Lake City'}, show_answer=True)

quiz_select_all_true = SelectMultipleQuiz(description="""
    Which of the following lines of code would evaluate as True?
    Use the values y = 10 and z = 5.
    """,
                                          answer=[
                                              "not (True & False)",
                                              "(not True) or (not False)",
                                              "True or False",
                                              "(y == 10) or (z < 5)",

                                          ],
                                          options=[
                                              "not ((y == 10) & (z >= 5))",
                                              "y == z"
                                          ]
                                          )



hint_2_2 = QuizHint(description="Visualization hints",
        hints=[
            widgets.HTML("""One option is a histogram:</br>
            <img src="./media/age_at_discharge_hist.png"></img>
            """),
            widgets.HTML("""One option is a histogram:</br>
            <img src="./media/age_at_discharge_boxplot.png"></img>
            """),
        ]
        )

hint_square_root = QuizHint(hints=[
    widgets.HTML("sqrt(x) is the same as raising x to the 1/2"),
    widgets.HTML("To raise a value to a power in Python, use two asterisks. For example: x squared = x**2")
])

test_my_mean = FunctionTest(args=([4, 0, 2, 2, 0, 10, 7, 8, 5, 0],), expected=3.8)


def test_sd_validation_func(sd_submitted):
    import math
    a = [4, 0, 2, 2, 0, 10, 7, 8, 5, 0]

    expected = np.std(a)
    actual = sd_submitted(a)
    if not math.isclose(actual, expected):
        print(f"Incorrect. Expected {expected:.4f}, got {actual:.4f}")
    print("Correct!")


import numpy as np

test_my_sd = FunctionTest(validation_func=test_sd_validation_func)


def validate_execute_commute(func):
    correct = True
    mappings = {"green": "Go!", "yellow": "Slow down.", "red": "Stop!"}
    for raining in (True, False):
        for color in ("green", "yellow", "red"):
            if raining is False:
                expected = (False, "walk")
            else:
                expected = (True, mappings[color])
            import io
            from contextlib import redirect_stdout

            f = io.StringIO()
            with redirect_stdout(f):
                actual = func(raining, color)

            if actual != expected:
                correct = False
                print(
                    f"Incorrect. When raining = {raining} and color = '{color}', expected {expected} but got {actual}")
    if correct:
        print("Correct!")


test_execute_commute = FunctionTest(validation_func=validate_execute_commute)

quiz_execute_commute_drive = MultipleChoiceQuiz(description="", answer="True; True; False", options=[
    "True; True; False",
    "True; False; True.",
    "False; True; True",
    "False; False; True"
])

hint_print_name = QuizHint(hints=[widgets.HTML("""If I ran this function without providing an argument for middle, it would print out 'My name is Alec Danger Chapman.'</br>
If I gave it my middle initial of 'B.', it would print out 'My name is Alec B. Chapman'""")])

hint_print_my_list = QuizHint(hints=[widgets.HTML("""The output should look like:</br><img src="./media/output_for_loop.png" width="50%" height="50%"></img>""")])

quiz_raining_false = MultipleChoiceQuiz(answer="'You should walk to work.'", options=[
    "'You should walk to work.'",
    "'You should drive to work.'",
    "Nothing will happen.",
    "An error will be raised."
])

def validate_decide_to_drive2(func):
    for a in (True, False):
        for b in (True, False):
            print(f"raining = {a}, hot = {b}")
            if a or b:
                expected = True
            else:
                expected = False
            actual = func(a, b)
            if actual != expected:
                print("That is incorrect.")
            else:
                print("That is correct!")
                print()
test_decide_to_drive2 = FunctionTest(validation_func=validate_decide_to_drive2)

def test_decide_to_bring_umbrella_validation_func(func):
    import inspect
    arg_spec = inspect.getfullargspec(func)
    if len(arg_spec.args) > 1:
        print(f"decide_to_drive should take one argument named 'raining'. Got {arg_spec.args}")
    import contextlib
    with contextlib.redirect_stdout(None):
        for val_in in (True, False):

            val_out = func(raining=val_in)
    try:
        assert val_in is val_out
    except AssertionError:
        print(f"Incorrect. When raining = {val_in}, return value should be {val_in}, not {val_out}")
        return False
    print("That is correct!")
    return True
test_decide_to_bring_umbrella = ValueTest(validation_func=test_decide_to_bring_umbrella_validation_func)

