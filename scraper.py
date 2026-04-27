from playwright.sync_api import sync_playwright

def get_product_price(product_name: str):
	with sync_playwright() as p:
		browser = p.chromium.launch(headless=True)
		page = browser.new_page()
	    
		try:
			page.goto("https://www.saucedemo.com/")

			page.fill("#user-name", "standard_user")
			page.fill("#password", "secret_sauce")
			page.click("#login-button")

			page.wait_for_selector(".inventory_list", timeout=5000)

			items = page.query_selector_all(".inventory_item")

			for item in items:
				name = item.query_selector(".inventory_item_name").inner_text()
				if product_name.lower() in name.lower():
					price = item.query_selector(".inventory_item_price").inner_text()
					browser.close()
					return {"product": name, "price": price}

			browser.close()
			return None
		except Exception:
			browser.close()
			return None
