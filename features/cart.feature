Feature: Cart Functionality
  Verify that an item can be added to the cart on eBay.

  Scenario: Verify item can be added to Cart
    Given I open the eBay homepage
    When I search for "book"
    And I click on the first item in the search results
    And I add the item to the cart
    Then I verify the cart displays the correct number of items
