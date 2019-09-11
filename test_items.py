link = 'http://selenium1py.pythonanywhere.com/es/catalogue/hackers-painters_185/'
link2 = 'http://selenium1py.pythonanywhere.com/es/catalogue/hacking-exposed-non-fifth-edition_188/'
def test_check_button_add_basket(browser):
        browser.get(link)
        button = browser.find_element_by_css_selector("#add_to_basket_form> .btn-add-to-basket")
        assert button
