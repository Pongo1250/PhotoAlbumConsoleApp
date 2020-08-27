#PhotoAlbumPresenter.py

#import statements
import requests

#call photos API and return json response
def callPhotosAPI():
    resp = requests.get('https://jsonplaceholder.typicode.com/photos')
    return resp.json()

#call albumId API and return json response
def callAlbumIdAPI(id):
    albumsUrl = "https://jsonplaceholder.typicode.com/photos?albumId={}".format(id)
    resp = requests.get(albumsUrl)
    return resp.json()

#get a set of albumIds from a collection of photos
def getAlbumIdsFromPhotos(photos):
    albumIds = []
    for photo in photos:
        albumIds.append(photo["albumId"])
    return set(albumIds)

#get a dictionary of photos from a set of albumIds
def getDictionaryOfAlbums(albumIds):
    albums = {}
    for id in albumIds:
        albums[id] = callAlbumIdAPI(id)
    return albums
        
#format a photo's id and title into a string
def formatIdAndTitle(photo):
    return "["+str(photo["id"]) + "] "+photo["title"]

#format header text for album from id
def getHeaderText(id):
    return "> photo album "+ str(id)

if __name__ == '__main__':
    print("Loading photos ...")
    photos = callPhotosAPI()
    albumIds = getAlbumIdsFromPhotos(photos)
    albums = getDictionaryOfAlbums(albumIds)
    for id in albumIds:
        print(getHeaderText(id))
        for photo in albums[id]:
            print(formatIdAndTitle(photo))
