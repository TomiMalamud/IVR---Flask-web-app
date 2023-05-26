class RespuestaDeCliente:
    def __init__(self, fechaEncuesta, respuestaSeleccionada):
        self.fechaEncuesta = fechaEncuesta
        self.respuestaSeleccionada = respuestaSeleccionada

    def getRespuestaPosible(self):
        return self.respuestaSeleccionada

    def getDescripcionRta(self):
        return self.respuestaSeleccionada.descripcion

class Llamada:
    def __init__(
        self,
        descripcionOperador,
        detalleAccionRequerida,
        duracion,
        encuestaEnviada,
        observacionAuditor,
        cliente,
        cambioEstado,
        respuestasDeEncuesta,
    ):
        self.descripcionOperador = descripcionOperador
        self.detalleAccionRequerida = detalleAccionRequerida
        self.duracion = duracion
        self.encuestaEnviada = encuestaEnviada
        self.observacionAuditor = observacionAuditor
        self.cambioEstado = cambioEstado
        self.respuestasDeEncuesta = respuestasDeEncuesta
        self.cliente = cliente

    def calcularDuracion(self):
        return self.duracion

    def determinarEstadoInicial(self):
        return self.cambioEstado.estadoInicial

    def determinarUltimoEstado(self):
        return self.cambioEstado.estadoFinal

    def esDePeriodo(self, fechaInicio):
        fechaMenor = 0
        for i in self.cambioEstado:
            if i.esFechaMenor(fechaInicio):
                fechaMenor = i.getFechaHoraInicio()
        return fechaMenor

    def getDuracion(self):
        return self.duracion

    def getNombreClienteDeLlamada(self):
        return self.cliente.nombre

    def getRespuestas(self):
        return self.respuestasDeEncuesta

    def new():
        pass

    def setDescripcionOperador(self, descripcionOperador):
        self.descripcionOperador = descripcionOperador

    def setDuracion(self, duracion):
        self.duracion = duracion

    def setEstadoActual(self, estadoActual):
        self.estadoActual = estadoActual

    def tieneRespuestas(self):
        return len(self.respuestasDeEncuesta) > 0

class Cliente:
    def __init__(self, dni, nombreCompleto, nroCelular):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular

    def esCliente(self, dni):
        return self.dni == dni

    def getNombre(self):
        return self.nombreCompleto

class Estado:
    def __init__(self, nombre):
        self.nombre = nombre

    def esFinalizada(self):
        return self.nombre == "Finalizada"

    def esIniciada(self):
        return self.nombre == "Iniciada"

    def getNombre(self):
        return self.nombre

class CambioEstado:
    def __init__(self, fechaHoraInicio, estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def getNombreEstado(self):
        return self.estadoInicial.getNombre()

    def new():
        pass

    def esFechaMenor(self, fecha):
        return self.fechaHoraInicio < fecha

class RespuestaPosible:
    def __init__(self, descripcion, valor):
        self.descripcion = descripcion

    def getDescripcionRta(self):
        return self.descripcion

class Pregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta

    def getDescripcion(self):
        return self.pregunta

    def listarRespuestasPosibles(self):
        return self.respuestasPosibles

class Encuesta:
    def __init__(self, fechaFinVigencia, descripcion, pregunta):
        self.fechaFinVigencia = fechaFinVigencia
        self.descripcion = descripcion
        self.pregunta = pregunta

    def armarEncuesta(self):
        pass

    def esEncuestaEnPeriodo():
        pass

    def esVigente():
        pass

    def getDescripcionEncuesta(self):
        return self.descripcion

    def getEncuestaPregunta(self):
        return self.pregunta

# Assuming you have the necessary data for object initialization
descripcion_operador = "Operator description"
detalle_accion_requerida = "Action required details"
duracion = 120
encuesta_enviada = True
observacion_auditor = "Auditor observation"
cliente = Cliente("123456789", "John Doe", "987654321")
cambio_estado = [CambioEstado("2023-05-25 10:00:00", Estado("Iniciada")), CambioEstado("2023-05-25 11:00:00", Estado("Finalizada"))]
respuestas_encuesta = [RespuestaDeCliente("2023-05-25", RespuestaPosible("Yes", 1))]

# Instantiate the object of the Llamada class
llamada = Llamada(
    descripcion_operador,
    detalle_accion_requerida,
    duracion,
    encuesta_enviada,
    observacion_auditor,
    cliente,
    cambio_estado,
    respuestas_encuesta
)

# You can now use the created object as per your requirements
# For example, you can access its attributes or call its methods
print(llamada.duracion)

esDePeriodo = llamada.esDePeriodo("2023-05-25 9:30:00")

print(esDePeriodo)
