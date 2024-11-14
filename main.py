from fastapi import FastAPI

app = FastAPI()
app.title ="Fastapi SENA" 
app.version= "2.0.0"

@app.get('/', tags=['home'])
def home ():
    return "hello fastapi"

@app.post('/', tags=['peliculas'])
def peliculas ():
    return "lalaland"

@app.put('/', tags=['Comida'])
def Comida ():
    return "hamburguesas"

@app.delete('/', tags=['libros'])
def libros ():
    return "almendra"




