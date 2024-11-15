import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s
from selene.support.conditions.have import exact_text
from selene.support.shared import browser


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'slinkov')
@allure.title('allure autotest with selene only')
@allure.feature('Таба issue')
@allure.story('Наименование issue')
@allure.link('https://github.com', name='Testing')
def test_github_issue():
    browser.open("https://github.com/AQuAgenerale97/qa_java")

    s("#issues-tab").click()
    s('#issue_3_link').should(exact_text('Sprint_2 finalProject'))
