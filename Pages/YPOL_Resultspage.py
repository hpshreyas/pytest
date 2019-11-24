

class ResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def ypol_search_results(self, phrase):
        # Check search result list
        # (A more comprehensive test would check results for matching phrases)
        # (Check the list before the search phrase for correct implicit waiting)
        links_div = self.driver.find_element_by_id('search-results-page')
        assert len(links_div.find_elements_by_xpath('//div')) > 0
        # Check search phrase
        search_input = self.driver.find_element_by_id('what')

        # assert search_input.get_attribute('value') == phrase
        print('test complete' 'value')
