from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import Test_Base


class Test_accuweather_test(Test_Base):

    i_understand_btn = (By.XPATH, "//*[text()='I Understand']")
    search_input = (By.CSS_SELECTOR, "input.search-input[name='query']")
    result_container = (By.XPATH, "//div[contains(@class, 'results-container')]")
    first_search_result = (By.XPATH, "//div[contains(@class, 'search-bar-result') and contains(@class, 'source-radar')]")
    location_header = (By.XPATH, "//h1[contains(@class, 'header-loc')]")
    location_to_search = "New York City"


    def test_webui_test(self):

        accept_btn = self.driver.find_element(*self.i_understand_btn)
        accept_btn.click()

        title = self.driver.title
        assert title == "Local, National, & Global Daily Weather Forecast | AccuWeather", "Title is not correct!"

        # Input " New York City into the search field"
        search_input_field = self.driver.find_element(*self.search_input)
        search_input_field.click()
        search_input_field.send_keys(self.location_to_search)

        # assertion to check the search list displayed
        result_container_element = self.wait.until(EC.visibility_of_element_located(self.result_container))
        assert result_container_element.is_displayed(), "Search results container is not displayed"

        # Click on the first search result.
        first_search_result_element = self.wait.until(EC.visibility_of_element_located(self.first_search_result))
        first_search_result_element.click()

        # Check the weather City weather page header contains city name from the search.
        city_weather_header = self.wait.until(EC.visibility_of_element_located(self.location_header))
        assert self.location_to_search in city_weather_header.text, f"City name in header does not match: Expected {self.location_to_search}, Actual {city_weather_header.text}"
