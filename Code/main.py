#––––––––– Clase Album –––––––––––
class Album:
    def __init__(self, nombre, anioLanzamiento, disquera, artistas):
        self.nombre = nombre
        self.anioLanzamiento = anioLanzamiento
        self.disquera = disquera
        self.artistas = artistas  # Lista de objetos Artista
        self.canciones = []  # Lista de objetos Cancion

    def agregarCancion(self, cancion):
        if not self.verificarTituloRepetido(cancion.titulo):
            self.canciones.append(cancion)
        else:
            raise ValueError("La cancion con el titulo '{}' ya existe en el album.".format(cancion.titulo))

    def verificarTituloRepetido(self, titulo):
        return any(cancion.titulo == titulo for cancion in self.canciones)

    def listarCanciones(self):
        return [(cancion.titulo, cancion.duracion) for cancion in self.canciones]

###––––––––––– Clase Cancion ––––––––––
class Cancion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion


###–––––––––– Clase Artista –––––––––––
class Artista:
    def __init__(self, nombre, paisOrigen):
        self.nombre = nombre
        self.paisOrigen = paisOrigen

###––––––––– Clase MusicTracker –––––––––––––––
class MusicTracker:
    def __init__(self):
        self.albumes = []  # Lista de objetos Album

    def agregarAlbum(self, nombre, anioLanzamiento, disquera, artistas):
        nuevoAlbum = Album(nombre, anioLanzamiento, disquera, artistas)
        self.albumes.append(nuevoAlbum)
        return nuevoAlbum

    def agregarCancionAlbum(self, nombreAlbum, tituloCancion, duracion):
        album = self.buscar_album_por_nombre(nombreAlbum)
        if album:
            nuevaCancion = Cancion(tituloCancion, duracion)
            album.agregarCancion(nuevaCancion)
        else:
            raise ValueError("album no encontrado.")

    def buscarAlbumNombre(self, nombre):
        for album in self.albumes:
            if album.nombre == nombre:
                return album
        return None

    def buscarAlbumesAnio(self, año):
        return [album for album in self.albumes if album.anioLanzamiento == año]

###–––––––––––– Clase Main ––––––––––––––
musicTracker = MusicTracker()
flag = True
while flag :
    print("\t Menu de Opciones")
    print("1. Agregar un nuevo Album")
    print("2. Agregar cancion a Album Existente")
    print("3. Ver Canciones de Album")
    print("4. Buscar Album por Anio")
    opc = input("Seleccione una opcion (numero): ")
    if not(isinstance(opc, int)):
        raise ValueError("Ingrese un numero")