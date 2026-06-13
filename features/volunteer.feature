Feature: Volunteer Registration

  As a charity coordinator
  I want to register volunteers
  So that I can manage volunteer participation

  Scenario: Successful volunteer registration

    Given a volunteer named "John" aged 25
    When the registration is submitted
    Then the volunteer should be registered successfully

  Scenario: Underage volunteer registration

    Given a volunteer named "Tom" aged 14
    When the registration is submitted
    Then the registration should be rejected

  Scenario: Calculate total volunteers

    Given volunteers "John" aged 25 and "Sarah" aged 30 are registered
    When the total volunteers are counted
    Then the total should be 2