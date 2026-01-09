Feature: User login

gherkin
Feature: User login and dashboard access
  As a user
  I want to be able to log in with valid credentials
  So that I can view my dashboard

  Scenario: Successful user login and dashboard access
    Given I am on the log in page
    When I enter valid credentials and submit the form
    Then I should see my dashboard

  Scenario: Invalid user login attempt
    Given I am on the log in page
    When I enter invalid credentials and submit the form
    Then I should see an error message indicating invalid login
