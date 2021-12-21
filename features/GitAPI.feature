# Created by Umesh_Kumar at 12/6/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Validate the Git API
    Given I have the github Auth cedentails
    When I hit the gitRep API of GITHUB
    Then status code of response should be 200
