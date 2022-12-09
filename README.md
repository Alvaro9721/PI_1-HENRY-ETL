<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>
*Alvaro Enrique Beleño Contreras*

*Ingeniero Industrial*

*Data Sciencie(In progress)*
<p align="center">
<img src="https://cosasdedevs.com/media/sections/images/fastapi.png"height=180>
<img src="https://aulasoftwarelibre.github.io/taller-de-pas/Sesion-1/images/horizontal-logo-monochromatic-white.png"  height=180>
</p>



<hr>  


Este trabajo consiste realizar un proceso de ETL con diversos dataset, con la finalidad de entregar datos limpios que puedan ser consumidos por una API, la cual va estar trabajando en un entorno virtual dockerizado.

`Application Programming Interface` es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles y fundamentales para la creación de, por ejemplo, pipelines, ya que permiten mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy en día contamos con **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = 'https://sp-ao.shortpixel.ai/client/to_auto,q_glossy,ret_img,w_950,h_430/https://blog.finerioconnect.com/wp-content/uploads/2020/04/como-funciona-una-api.jpg' height=250><p>

<hr>

## **Tecnologías**

Para la elboración de este proyecto se utilizaron las siguiente tecnologias:

* Fastapi
* Docker desktop
* Visual studio code
* Jupyter
* Python
* Pandas
* Uvicorn
<hr>

## **Pasos para la elaboracion del proyecto**


<p align=center>
<img src = 'https://lemon.digital/wp-content/uploads/2018/08/Marketing-Automation-2-400x270.png' height=250><p>

**1.** **EDA** 

Se realiza un analisis exploratorio con el objetivo de verificar el estado los datos de entrada logardo detallar que esten cargados correctamente, lo cual permite poder tomar decisiones en la limpieza de estos, los archivos orginales fueron provistos como *csv* o *json*, estos se cargaron de la siguiente manera:

Para visualizar la limpieza completa se pueden remitir a [Limpieza](https://github.com/Alvaro9721/PI_1-HENRY-ETL/blob/main/PI01_DATA05-main/lab_1.ipynb).
```python

df_Amazon = pd.read_csv("https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/amazon_prime_titles.csv")
df_Disney = pd.read_csv("https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/disney_plus_titles.csv")
df_Hulu = pd.read_csv("https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/hulu_titles.csv")
df_Netflix= pd.read_json("https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/netflix_titles.json")

```


**2.** **Creación de la API**

Para crear la API se utilizo el framework [FasAPI](https://fastapi.tiangolo.com/) que ayuda de forma rapida a tener una API trabajando.

La API llamanda **Consultas de plataformas striming** permite conocer diferentes datos de las platafromas Amazon, Hulu, Diney, Netflix, esta se trabajo en un archivo llamado **main.py** y se inicializó de la siguiente manera:

Para ver el codigo completo donde estan todas las funciones que de la API se pueden remitir a [main.py](https://github.com/Alvaro9721/PI_1-HENRY-ETL/blob/main/PI01_DATA05-main/main.py).

```python 
app=FastAPI(title="Consultas de plataformas striming ",
description="Esta API nos permite conocer diferentes datos de las platafromas Amazon, Hulu, Diney, Netflix, para filtar las plataformas se debe inicializar los nombre de estas con mayuscula.",
verion="1.0.0.0.1")
```

**2.1** **Ejecutar la API**

Para ejecutar la API se tienen que ejecutar la siguiente linea de comandos:


1. Cargar la api
```python
uvicorn main:app --reload
```
2. Entrar a nuestro navegador
```python
localhost:8000/docs
```



**3. Dockerizar la API**

Al momento de dokerizar un API lo primero que tenemos que tener es el docker especifico para nuestra maquina, este se pude descargar en la [pagina_oficial](https://www.docker.com/), para este caso en especifico se utilizo Docker desktop.


**3.1 Crear la imagen**
Para crear la imagen de nuestra API en docker se tiene que crear un archivo **Dockerfile** en el cual se especifica la ruta donde se guardara la imagen, el servidor y lo que tiene que instalar dentro de ella, posteriormente se crea un archivo **requiremensts.txt** donde va las librerias a utilizar en la imagen y sus versiones correspondientes.

* Datos para el Dockerfile:

```Python
FROM python:3.11.1
COPY . /carp1/carp2
WORKDIR /carp1/carp2
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0"]
```

* Datos para requiremensts.txt :
```Python
fastapi==0.88.0
uvicorn==0.20.0
pandas==1.4.4
pydantic==1.10.2
numpy==1.23.3
psycopg2==2.9.5
```

**3.2 Comandos para conectar con Docker desktop**


Los comando a usar para cargar la imagen y el docker son los siguientes:

1. Crear la imagen.
```python
docker build -t pim_app . 
```
2. Encender el docker.
```python
docker run -it -p 8000:8000 -v cd:/carp1/carp2 prim_app
```
Una vez encendido el docker ya podemos utilizar nuestra API introduciendo en nuestro buscador **localhost:8000/docs**.




<p align=center>
<img src = 'https://blog.soyhenry.com/content/images/2021/05/PRESENTACION-3.jpg' height=250><p>

