import psycopg2
from fastapi import FastAPI

conexion = psycopg2.connect(host="localhost", database="fastapi", user="user_fastapi", password="root")

# Creamos el cursor con el objeto conexion
cur = conexion.cursor()

app = FastAPI()
@app.get("/")
def index():
    return [{"PROYECTO":"DATA ENGINEER CREACION DE APIS","Estudiante":"RIVAS CHAVEZ GIAN",
    "GMAIL":"gianrivaschavez@gmail.com","cohorte":"data06","github":"https://github.com/GianArthas"}]

#Cantidad de veces que aparece una palabra clave en el título de peliculas/series, por plataforma
@app.get("/cant_words_title")
def get_count_words(platform:str, word:str):
    
    # Ejecutamos una consulta
    query = "SELECT count(*) FROM public."+platform+ " WHERE title like '%"+word+"%';"
    
    cur.execute(query)
    respuesta = cur.fetchone()
    return [{"word":word,"plaform":platform,"cantidad de repeticiones":respuesta}]


#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/cant_movie_platform")
def get_count_words(platform:str, score_greater_than:int, year:int):
    
    # Ejecutamos una consulta
    query = "SELECT count(*) FROM public."+platform+" WHERE tipo='movie' and score>"+ str(score_greater_than)+" and release_year="+ str(year)+";"
    cur.execute(query)
    respuesta = cur.fetchone()
    return [{"plaform":platform,"score grather than":score_greater_than, "year":year, "cantidad de peliculas":respuesta}]


#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/cant_movie_platform")
def get_count_words(platform:str, score_greater_than:int, year:int):
    
    # Ejecutamos una consulta
    query = "SELECT count(*) FROM public."+platform+" WHERE tipo='movie' and score>"+ str(score_greater_than)+" and release_year="+ str(year)+";"
    cur.execute(query)
    respuesta = cur.fetchone()
    return [{"plaform":platform,"score grather than":score_greater_than, "year":year, "cantidad de peliculas":respuesta}]

#La segunda película con mayor partitura para una plataforma determinada, según el orden alfabético de los títulos.
@app.get("/partitura")
def get_count_words(platform:str, score_greater_than:int, year:int):
    
    # Ejecutamos una consulta
    query = "SELECT count(*) FROM public."+platform+" WHERE tipo='movie' and score>"+ str(score_greater_than)+" and release_year="+ str(year)+";"
    cur.execute(query)
    respuesta = cur.fetchone()
    return [{"plaform":platform,"score grather than":score_greater_than, "year":year, "cantidad de peliculas":respuesta}]

#Película que más apareció según año, plataforma y tipo de duración
@app.get("/movie_more_repeat")
def get_count_words(platform:str, year:int, duration_type:str):
    
    # Ejecutamos una consulta
    query = "select title, count(title) as rep_pelicula from public."+platform+" where release_year ="+str(year) +" and duration_type = '"+duration_type+"'  group by title order by rep_pelicula desc, title asc limit 1;"
    cur.execute(query)
    respuesta = cur.fetchone()
    return [{"plaform":platform,"year":year, "duration_type":duration_type, "Película que más apareció":respuesta[0]}]


#Cantidad de series y películas por rating
@app.get("/series_movies_for_rating")
def get_count_words(rating:str):
    
    # Ejecutamos una consulta
    query = "select rating, count(tipo) as cant_series_movies from  public.alltable where rating = '"+rating+"' group by rating;"
    cur.execute(query)
    respuesta = cur.fetchone()
    return [{"rating":rating,"cantidad de series peliculas":respuesta[1]}]




















