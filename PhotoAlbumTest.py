# photoAlbumTest.py

#import statements
import unittest
import PhotoAlbumPresenter

class photoAlbumTest(unittest.TestCase):
        #The api call for albums should return something
        def test_photosAPICallSuccessful(self):
                self.assertTrue(PhotoAlbumPresenter.callPhotosAPI())
                
        #The Api call for photos by albumId should return something
        def test_albumIdAPICallSuccesful(self):
                self.assertTrue(PhotoAlbumPresenter.callAlbumIdAPI(1))

        #I should get a set of albumId's from the album collection
        def test_getListFromAlbums(self):
                photos = PhotoAlbumPresenter.callPhotosAPI()
                albumIds = PhotoAlbumPresenter.getAlbumIdsFromPhotos(photos)
                self.assertTrue(albumIds)
                self.assertTrue(isinstance(albumIds, set))

        #list of albumId's produces dictionary of albums {albumId: list of photos}
        def test_getDictionaryOfPhotos(self):
                albumIds = [1,3]
                albums = PhotoAlbumPresenter.getDictionaryOfAlbums(albumIds)
                self.assertTrue(albums)
                self.assertTrue(isinstance(albums, dict))

        #I should get a formated string with [photoId] and title
        def test_formatIdAndTitle(self):
                photo = {}
                photo["id"] = 1
                photo["title"] = "lorem ipsum"
                self.assertEqual(PhotoAlbumPresenter.formatIdAndTitle(photo), "[1] lorem ipsum")

        #I should get header text for photo album by ID
        def test_getHeaderText(self):
                id = 3
                self.assertEqual(PhotoAlbumPresenter.getHeaderText(id), "> photo album 3")
        
if __name__ == '__main__':
    unittest.main()
