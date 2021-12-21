# Created by Umesh_Kumar at 11/29/2021
Feature: Verify if the Books are added and deleted
  # Enter feature description here
  @library
  Scenario: Verify AddBook API functionality
  Given The books details which needs to be added
  When We execute the AddBook PostAPI method
  Then Book is successfully Added
  Then status code of response should be 200

    # Enter steps here
  @library
  Scenario Outline: Verify AddBook API functionality
  Given The books details which needs to be added
  When We execute the AddBook PostAPI with <isbn> and <aisle>
  Then Book is successfully Added
    Then status code of response should be 200
    Examples:

      |isbn  |aisle|
      |13001edv      |1509888339d9123|