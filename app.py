from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.usersrols import userrol
from routes.rutinas import rutina
from routes.ejercicios_rutinas import ejcrtn
from routes.progra_salud import progra_salud
from routes.instructors import instructor
from routes.ejercicio import ejercicio
from routes.evaluacion_serv import evaluaciones_serv_router
from routes.pedidos import pedido
from routes.promociones import promocion
from routes.Pregunta import pregunta_router
from routes.OpinionCliente import opinion_router
from routes.productos import producto



app = FastAPI()
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(rutina)
app.include_router(ejcrtn)
app.include_router(progra_salud)
app.include_router(instructor)
app.include_router(ejercicio)
app.include_router(evaluaciones_serv_router)
app.include_router(pedido)
app.include_router(promocion)
app.include_router(pregunta_router)
app.include_router(opinion_router)
app.include_router(producto)
