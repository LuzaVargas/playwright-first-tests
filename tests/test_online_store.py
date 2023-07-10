from playwright.sync_api import Page, expect


FIRST_PRODUCT_HOVER = '.features_items > div:nth-child(3)'
MORE_DETAIL_BTN = 'div[class="choose"] a[href="/product_details/1"]'
QUANTITY_INPUT = '#quantity'
ADD_CART_BTN = 'button[class="btn btn-default cart"]'
ADDED_PRODUCT_MODAL = '.modal-content'
CONTINUE_SHOPPING_BTN = 'button[class="btn btn-success close-modal btn-block"]'


def test_add_product_to_cart(page: Page):
    # go to url https://automationexercise.com/products
    page.goto('https://automationexercise.com/products')

	# hover of the first product found
    page.locator(FIRST_PRODUCT_HOVER).hover()

	# click on More Detail of the first product
    page.locator(MORE_DETAIL_BTN).click()
    page.go_back()
    page.locator(MORE_DETAIL_BTN).click()
    expect(page).to_have_url('https://automationexercise.com/product_details/1')
	
    # change the quantity to 3
    page.locator(QUANTITY_INPUT).clear()
    page.locator(QUANTITY_INPUT).fill('3')
		
    # click the Add to Cart button
    page.locator(ADD_CART_BTN).click()
	
    # verify that the message "Product successfully added to your shopping cart" is visible
    expect(page.locator(ADDED_PRODUCT_MODAL)).to_be_visible()
    expect(page.locator(ADDED_PRODUCT_MODAL)).to_contain_text('Added!')
	
    # click the Continue Shopping button
    page.locator(CONTINUE_SHOPPING_BTN).click()
	
    # the modal should not be visible
    expect(page.locator(ADDED_PRODUCT_MODAL)).not_to_be_visible()
