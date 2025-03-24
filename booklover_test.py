import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        b1test=BookLover("MaryJane", "maryjane1@gmail.com", "scifi")
        b1test.add_book("Dune Messiah", 4)
        self.assertTrue("Dune Messiah" in b1test.book_list["book_name"].values)
        
    def test_2_add_book(self):
        b2test=BookLover("SusyJane", "susyjane1@gmail.com", "mystery")
        b2test.add_book("Death on the Nile", 3)
        b2test.add_book("Death on the Nile", 4)
        self.assertEqual(len[b2test.book_list["book_name"]=="Death on the Nile"], 1)
                                              
    def test_3_has_read(self):
        b3test=BookLover("BobbiJane", "bobbijane1@gmail.com", "biography")
        b3test.add_book("Wild Swans", 5)
        self.assertTrue(b3test.has_read("Wild Swans"))
                                              
    def test_4_has_read(self):
        b4test=BookLover("LolaJane", "lolajane1@gmail.com", "scifi")
        self.assertFalse(b4test.has_read("Foundation"))
                                              
    def test_5_has_read(self):
        b5test=BookLover("SaraJane", "sarajane1@gmail.com", "mystery")
        b5test.add_book("The Crooked House", 3)
        b5test.add_book("The ABC Murders", 5)
        b5test.add_book("Murder on the Orient Express", 4)
        self.assertEqual(b5test_num_books_read(), 3)                                      
    
    def test_6_fav_books(self):
        b6test=BookLover("CatSmith", "mycatsmith1@gmail.com", "fantasy")
        b6test.add_book("The Simarillion", 5)
        b6test.add_book("The Hobbit", 4)
        b6test.add_book("A Wrinkle in Time", 5)
        b6test.add_book("A Swiftly Tilting Planet", 4)
        b6test.add_book("Grapes of Wrath", 1)
        b6test.add_book("Emma", 2)
        self.assertTrue(all(favs["book_rating"]>3)) 
                                              
if __name__=='__main__':
    unittest.main(verbosity=3)                                         