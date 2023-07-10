import pytest
from playwright.sync_api import Page, expect


SEARCH_BTN = 'button[aria-label="Search"]'
SEARCH_INPUT = '#docsearch-input'
SEARCH_PLACE_HOLDER = 'Search docs'
CLEAR_BTN = 'Clear the query'
NO_RESULTS_TXT = '.DocSearch-NoResults p'
RESULTS_CONTAINER = '.DocSearch-Dropdown-Container section'


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    page.goto('https://playwright.dev/docs/intro')
    yield


def test_search_no_results(page: Page):
  page.locator(SEARCH_BTN).click()

  page.locator(SEARCH_INPUT).click()

  page.locator(SEARCH_INPUT).fill('hascontent')

  expect(page.locator(NO_RESULTS_TXT)).to_be_visible()

  expect(page.locator(NO_RESULTS_TXT)).to_have_text('No results for "hascontent"')


def test_clear_search_input(page: Page):
  page.locator(SEARCH_BTN).click()

  searchBox = page.get_by_placeholder(SEARCH_PLACE_HOLDER)

  searchBox.click()

  searchBox.fill('somerandomtext')

  expect(page.locator(SEARCH_INPUT)).to_have_attribute('value', 'somerandomtext')

  page.get_by_title(CLEAR_BTN).click()

  expect(page.locator(SEARCH_INPUT)).to_have_attribute('value', '')


def test_search_with_at_least_one_result(page: Page):
  page.locator(SEARCH_BTN).click()

  searchBox = page.get_by_placeholder(SEARCH_PLACE_HOLDER)

  searchBox.click();

  page.get_by_placeholder(SEARCH_PLACE_HOLDER).fill('havetext')

  expect(page.locator(SEARCH_INPUT)).to_have_attribute('value', 'havetext')

  # Verity there are sections in the results
  page.locator(RESULTS_CONTAINER).nth(1).wait_for()
  numberOfResults = page.locator(RESULTS_CONTAINER).count()
  assert numberOfResults > 0
