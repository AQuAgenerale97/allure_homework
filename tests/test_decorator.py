import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s
from selene.support.conditions.have import exact_text
from selene.support.shared import browser


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'slinkov')
@allure.title('allure autotest with decorators')
@allure.feature('Таба issue')
@allure.story('Наименование issue')
@allure.link('https://github.com', name='Testing')
def test_github_issue():
    open_page()
    open_tab()
    should_have_exact_issue()


@allure.step('Открываем страницу пользовательского проекта на GitHub')
def open_page():
    browser.open("https://github.com/AQuAgenerale97/qa_java")


@allure.step('Переходим на табу Issues')
def open_tab():
    s("#issues-tab").click()


@allure.step('Проверяем, что Issue с описанием "Sprint_2 finalProject" есть среди Issues')
def should_have_exact_issue():
    s('#issue_3_link').should(exact_text('Sprint_2 finalProject'))
