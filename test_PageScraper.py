import unittest
from classes import PageScraper


class PageScraperTest(unittest.TestCase):

    def test_well_formed_url(self):
        # Check if URL validator can pass the well-formed string
        # and check the exception raised when an exception is thrown
        url = "http://www.google.com"
        ps = PageScraper.PageScraper(url)
        self.assertEqual(ps.validate_url(), bool(
            1), "Invalid URL (protocol, domain, optional port, etc.)")

        with self.assertRaises(SystemExit):
            ps.url = "My Cat"
            ps.validate_url()
