import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'slinkov')
@allure.feature('Задачи в репозитории №1')
@allure.story('Пользователь делает поиск в github')
@allure.link('https://github.com', name='Testing')
def test_selene(open_browser):
    browser.open("https://github.com/Nastya-Leto/HW_allure_10")

    s("#issues-tab").click()

    s('#issue_1_link').should(exact_text('Enjoy autumn'))
