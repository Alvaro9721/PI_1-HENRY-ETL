from fastapi import FastAPI, Path, UploadFile, File
import pandas as pd
import numpy as np

app=FastAPI(title="Consultas de plataformas striming ",
description="Esta API nos permite conocer diferentes datos de las platafromas Amazon, Hulu, Diney, Netflix, para filtar las plataformas se debe inicializar los nombre de estas con mayuscula.",
verion="1.0.0.0.1")

df_actores=pd.read_csv("actores.csv")
df_genero=pd.read_csv("Genero_p.csv")
df_general=pd.read_csv("Informacion_general.csv")

@app.get("/Máxima duración según tipo de film (película/serie), por plataforma y por año.")
async def get_max_duration(Año:int,Plataform:str,Tipo_Film:str):
    message=f"Maximo de {Plataform} es"
    return {message:df_general[(df_general["Año_Rodaje"]==Año)&
    (df_general["Plataforma"]==Plataform)&(df_general["Tipo (min-Seasons)"]==Tipo_Film)]["Duracion"].max().tolist()}

@app.get("/Cantidad de películas y series por plataforma.")
async def get_count_plataform(plataform:str):
    return{f"Cantidad de peliculas en {plataform} es":df_general[(df_general["Plataforma"]==plataform)&(df_general["Tipo_Film"]=="movie")]["Tipo_Film"].count().tolist(),
    f"Cantidad de series en {plataform} es":df_general[(df_general["Plataforma"]==plataform)&(df_general["Tipo_Film"]=="tv show")]["Tipo_Film"].count().tolist()}

@app.get("/Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.")
async def get_listedin(genero:str):
    genero={(df_genero[(df_genero["Genero"]==genero)]["Plataforma"].value_counts().idxmax()):
    (df_genero[(df_genero["Genero"]==genero)]["Plataforma"].value_counts().max().tolist())}
    #lista=list(genero)
    return genero


@app.get("/Actor que más se repite según plataforma y año")
async def get_actor(pltaform:str,año:int):
    data=df_actores[(df_actores["Año_Rodaje"]==año)&(df_actores["Plataforma"]==pltaform)]["Actor"]
    if data.value_counts().index[0]=="sin dato":
        return {data.value_counts().index[0]:data.value_counts()[0].tolist()}
    elif data.value_counts().index[0] != "sin dato":
        return {data.value_counts().index[0]:data.value_counts()[0].tolist()}