@web @yellowpages

Feature: YellowPages Web Search
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  Background:
    Given the YellowPages home page is displayed

  Scenario: Basic YellowPages Search
    When the user searches for "Plumbers & Gas Fitters"
    Then results are shown for "Plumbers & Gas Fitters"

  Scenario: Search available lawyers
      When the user clicks on "Lawyer" icon
      Then results are shown for "Lawyer"

  Scenario: Check for advertisers that are open now
      When the user clicks on "Lawyer" icon
      When user checks on now open
      Then display the advertisers that are open now
