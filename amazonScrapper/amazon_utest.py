import unittest
from amazon_scrapper import scrap_product, check_existence

URL1 = "https://www.amazon.es/Amazfit-T-Rex-SmartWatch-Multideporte-Navegaci%C3%B3n/dp/B09ZYLLXGW/?_encoding=UTF8&pd_rd_w=Gj4fU&content-id=amzn1.sym.e938e71b-2a18-43eb-855b-f4edce2ba725&pf_rd_p=e938e71b-2a18-43eb-855b-f4edce2ba725&pf_rd_r=8ACMTYE9ANS1016J482N&pd_rd_wg=hfvlJ&pd_rd_r=6b881070-377a-4551-97bd-1286cda51cbc&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
URL2 = "https://www.amazon.com/dp/B0B3C/"


class amazon_test(unittest.TestCase):
    def test_url_exists(self):
        print("Test 1")
        existence = check_existence(URL1)
        print(f"Ex1: {existence}")
        self.assertEqual(existence, True)

    def test_url_not_exists(self):
        print("Test 2")
        existence = check_existence(URL2)
        print(f"Ex2: {existence}")
        self.assertEqual(existence, False)

    def test_correct_url(self):
        print("Test 3")
        first_price = "199,00"
        product = scrap_product(URL1)
        print(f"Prod: {product}")
        name = product["price"]
        self.assertEqual(name, first_price)  # add assertion here

    def test_incorrect_url(self):
        print("Test 4")
        product = scrap_product(URL2)
        self.assertEqual(product, None)


if __name__ == '__main__':
    unittest.main()
    amazon_test.close()
