from behave import given, then, when

# memory to simulate user storage
VALID_USER = {
    "username": "demo_user",
    "password": "demo_pass"
}

@given("I am on the log in page")  # type: ignore
def step_on_login_page(context):
    context.page = "login"

@when("I enter valid credentials and submit the form")  # type: ignore
def step_enter_valid(context):
    context.entered_username = VALID_USER["username"]
    context.entered_password = VALID_USER["password"]
    context.authenticated = True

@when("I enter invalid credentials and submit the form")  # type: ignore
def step_enter_invalid(context):
    context.entered_username = "bad_user"
    context.entered_password = "wrong_pass"
    context.authenticated = False

@then("I should see my dashboard")  # type: ignore
def step_see_dashboard(context):
    assert context.authenticated is True
    context.page = "dashboard"

@then("I should see an error message indicating invalid login")  # type: ignore
def step_error_message(context):
    assert context.authenticated is False
    context.error = "Invalid login"
