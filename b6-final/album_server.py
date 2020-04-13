from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request
import re


import album

def check_data(album_data):
    """
    Проверка данных на корректность. Тестовые данные проверям только на пустую строку, год проверяем чтоб был в диапазоне от 1900 до 2020
    """
    if (album_data["year"] and album_data["artist"] and album_data["album"] and album_data["album"]):
        if album_data["year"].isdigit():
            if (int(album_data["year"])>=1900 and int(album_data["year"])<=2020 and album_data["artist"]!="" and album_data["album"]!="" and album_data["genre"]!=""):
                return True
    else:
        return False
    

@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    albums_cnt = len(albums_list)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "Количество альбомов {}. Список альбомов {}: ".format(albums_cnt,artist)
        result += ", ".join(album_names)
    return result

@route("/albums", method="POST")
def album_new():
    album_data = {
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album"),
        "year": request.forms.get("year")
    }
    #Делаем запрос на корректность полученных данных. Если данные корректны, далее проверяем есть ли альбом с указанными данными, а если нет, то записываем альбом в БД
    if check_data(album_data):
        find_album = album.find_al(album_data)
        if find_album:
            message = "Альбом {} уже есть в БД".format(find_album.album)
            result = HTTPError(409, message)
        else:
            result = album.new_al(album_data)
    else:
        result = "Полученные данные не корректны. Альбом не записан в БД"
    return result
    
    
if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
