import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s
from selene.support.conditions.have import exact_text
from selene.support.shared import browser


def test_github_issue():
    allure.dynamic.tag('web')
    allure.dynamic.title('allure autotest with allure steps')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'slinkov')
    allure.dynamic.feature('Таба issue')
    allure.dynamic.story('Наименование issue')
    allure.dynamic.link('https://github.com', name='Testing')

    with allure.step("Открываем страницу пользовательского проекта на GitHub"):
        browser.open("https://github.com/AQuAgenerale97/qa_java")

    with allure.step("Переходим на табу Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем, что Issue с описанием 'Sprint_2 finalProject' есть среди Issues"):
        s('#issue_3_link').should(exact_text('Sprint_2 finalProject'))
