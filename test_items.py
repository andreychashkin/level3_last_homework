import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."


def test_presence_button_add_basket(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), "Кнопка Добавить в корзину не найдена"