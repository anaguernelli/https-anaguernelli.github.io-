from selenium.webdriver.common.by import By

from .base import RecipeBaseFunctionalTest

import pytest


@pytest.mark.functional_test
# para executar o marker
# pytest -m 'functional_test' -rP
# para executar tudo menos 'functional_test'
# pytest -m 'not functional_test'
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    def test_recipe_home_page_without_recipe_not_found_messages(self):
        # live_server_url vai apenas pegar nossa url sem precisarmo digitá-la
        self.browser.get(self.live_server_url)
        # encontre elemento por tag name no body do html
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No Recipes Found Here !!', body.text)
