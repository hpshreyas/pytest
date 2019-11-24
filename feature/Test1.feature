@web @yellowpages

Feature: YellowPages Web Search
  Scenario: Basic YellowPages Search
    Given the YellowPages home page is displayed
    When the user searches for "Plumbers & Gas Fitters"
    Then results are shown for "Plumbers & Gas Fitters"
