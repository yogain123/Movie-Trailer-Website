import media
import fresh_tomatoes

dangal = media.movies("DANGAL","https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg","https://www.youtube.com/watch?v=x_7YlGv9u1g")
sultan = media.movies("SULTAN","http://www.indicine.com/img/2016/05/Sultan-New-Poster-Salman-Khan-Anushka-Sharma.jpg","https://www.youtube.com/watch?v=wPxqcq6Byq0")
idiot3 = media.movies("3 IDIOT","http://c.saavncdn.com/246/3-Idiots-2009-500x500.jpg","https://www.youtube.com/watch?v=xvszmNXdM4w")
tamasha = media.movies("TAMASHA","http://www.cinebucket.com/wp-content/uploads/2015/09/maxresdefault6.jpg","https://www.youtube.com/watch?v=o-e5eWVCzx8")
gajni = media.movies("GAJNI","https://upload.wikimedia.org/wikipedia/en/9/97/Ghajini_Hindi.jpg","https://www.youtube.com/watch?v=X3twRPht7N0")
aedilhaimushkil = media.movies("AI DIL HAI MUSHKIL","http://downloadming.tv/uploads/Ae-Dil-Hai-Mushkil-2016-5-300x300.jpg","https://www.youtube.com/watch?v=Z_PODraXg4E")
airlift = media.movies("AIRLIFT","http://c.saavncdn.com/451/Airlift-Hindi-2015-500x500.jpg","https://www.youtube.com/watch?v=-doSs6cjHDc")
rustom = media.movies("RUSTOM","https://upload.wikimedia.org/wikipedia/en/9/96/Akshay_Kumar's-Rustom_poster.jpg","https://www.youtube.com/watch?v=L83qMnbJ198")
holiday = media.movies("HOIDAY","https://s-media-cache-ak0.pinimg.com/originals/a0/03/17/a003174941b2ab3777976df98c1c7c9e.jpg","https://www.youtube.com/watch?v=VQMsEX22f04")

list_of_movies = [dangal,sultan,idiot3,tamasha,gajni,aedilhaimushkil,airlift,rustom,holiday]    
fresh_tomatoes.open_movies_page(list_of_movies)

