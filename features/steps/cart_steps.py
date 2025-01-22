from behave import given, when, then
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.item_page import ItemPage

@given("I open the eBay homepage")
def step_open_ebay_homepage(context):
    context.home_page = HomePage(context.browser)
    context.home_page.open()

@when('I search for "{item}"')
def step_search_item(context, item):
    context.home_page.search_for_item(item)
    context.search_results_page = SearchResultsPage(context.browser)

@when("I click on the first item in the search results")
def step_click_first_item(context):
    context.search_results_page.click_first_item()
    context.item_page = ItemPage(context.browser)

@when("I add the item to the cart")
def step_add_item_to_cart(context):
    context.item_page.add_to_cart()

@then("I verify the cart displays the correct number of items")
def step_verify_cart(context):
    assert context.item_page.get_cart_count() == 1, "Cart count is incorrect!"
