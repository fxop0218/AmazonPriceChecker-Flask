import unittest
from amazon_scrapper import scrap_product, check_existence

URL1 = "https://www.amazon.com/-/es/Laptop-Apple-MacBook-2022-chip/dp/B0B3C5H787/ref=sr_1_1?keywords=macbook&qid=1668276484&sr=8-1&th=1 "
URL2 = "https://www.amazon.com/dp/B0B3C/"


class MyTestCase(unittest.TestCase):
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
        url1_prod_name = "Laptop Apple MacBook Air 2022 con chip M2: pantalla de retina líquida de 13.6 pulgadas, " \
                         "8 GB de RAM, almacenamiento SSD de 512 GB, teclado retroiluminado, cámara FaceTime HD de " \
                         "1080p. Funciona con iPhone y iPad; medianoche "
        product = scrap_product(URL1)
        print(f"Prod: {product}")
        name = product["title"]
        self.assertEqual(name, url1_prod_name)  # add assertion here

    def test_incorrect_url(self):
        print("Test 4")
        product = scrap_product(URL2)
        self.assertEqual(product, None)


if __name__ == '__main__':
    unittest.main()
