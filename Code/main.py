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
        album = self.buscarAlbumNombre(nombreAlbum)
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

###––––––––––– Clase Main ––––––––––––––

def mostrarMenu():
    print("\tMenu de Opciones")
    print("1. Agregar un nuevo Album")
    print("2. Agregar cancion a Album Existente")
    print("3. Ver Canciones de Album")
    print("4. Buscar Album por Anio")
    print("5. Salir")

def obtenerArtista():
    artistas = []
    while True:
        nombreArtista = input("Ingrese el nombre del artista (o 'fin' para terminar): ")
        if nombreArtista.lower() == 'fin':
            break
        paisOrigen = input(f"Ingrese el país de origen de {nombreArtista}: ")
        artistas.append(Artista(nombreArtista, paisOrigen))
    return artistas

def guardarDatos(musicTracker):
    with open("albumes_y_canciones.txt", "w") as file:
        for album in musicTracker.albumes:
            file.write(f"Álbum: {album.nombre}\n")
            file.write(f"Año de Lanzamiento: {album.anioLanzamiento}\n")
            file.write(f"Disquera: {album.disquera}\n")
            file.write(f"Artistas: {', '.join(artista.nombre for artista in album.artistas)}\n")
            file.write("Canciones:\n")
            for cancion in album.canciones:
                file.write(f"\t- {cancion.titulo} ({cancion.duracion} minutos)\n")
            file.write("\n")
    print("Datos guardados en 'albumes_y_canciones.txt'.")

def cargarDatos(nombre_archivo):
    musicTracker = MusicTracker()
    
    try:
        with open(nombre_archivo, "r") as file:
            lineas = file.readlines()
    except FileNotFoundError:
        return None
    
    album_actual = None
    for linea in lineas:
        linea = linea.strip()
        
        if linea.startswith("Álbum:"):
            nombre_album = linea[len("Álbum: "):]
            album_actual = Album(nombre_album, "", "", [])
            musicTracker.albumes.append(album_actual)
        
        elif linea.startswith("Año de Lanzamiento:"):
            anio_lanzamiento = linea[len("Año de Lanzamiento: "):]
            album_actual.anioLanzamiento = anio_lanzamiento
        
        elif linea.startswith("Disquera:"):
            disquera = linea[len("Disquera: "):]
            album_actual.disquera = disquera
        
        elif linea.startswith("Artistas:"):
            artistas_nombres = linea[len("Artistas: "):].split(", ")
            artistas = [Artista(nombre, "") for nombre in artistas_nombres]
            album_actual.artistas = artistas
        
        elif linea.startswith("- "):
            partes = linea[2:].split(" (")
            titulo_cancion = partes[0]
            duracion_cancion = partes[1].replace(" minutos)", "")
            nueva_cancion = Cancion(titulo_cancion, duracion_cancion)
            album_actual.canciones.append(nueva_cancion)
    
    if not musicTracker.albumes:  
        return None
    
    print("Datos cargados desde '{}'.".format(nombre_archivo))
    return musicTracker


musicTracker = cargarDatos("albumes_y_canciones.txt")
if musicTracker is None:
    musicTracker = MusicTracker()
flag = True
while flag:
    mostrarMenu()
    opc = input("Seleccione una opcion (numero): ")
    
    if not opc.isdigit():
        print("Por favor, ingrese un numero válido.")
        continue

    opc = int(opc)
    
    if opc == 1:
        nombre = input("Ingrese el nombre del album: ")
        anioLanzamiento = input("Ingrese el año de lanzamiento: ")
        disquera = input("Ingrese el nombre de la disquera: ")
        artistas = obtenerArtista()
        musicTracker.agregarAlbum(nombre, anioLanzamiento, disquera, artistas)
        print("Álbum agregado exitosamente.")
    
    elif opc == 2:
        nombreAlbum = input("Ingrese el nombre del album: ")
        tituloCancion = input("Ingrese el titulo de la cancion: ")
        duracion = input("Ingrese la duracion de la cancion (en minutos): ")
        try:
            musicTracker.agregarCancionAlbum(nombreAlbum, tituloCancion, duracion)
            print("Canción agregada exitosamente.")
        except ValueError as e:
            print(e)
    
    elif opc == 3:
        nombreAlbum = input("Ingrese el nombre del album: ")
        album = musicTracker.buscarAlbumNombre(nombreAlbum)
        if album:
            canciones = album.listarCanciones()
            print(f"Canciones en el álbum '{nombreAlbum}':")
            for titulo, duracion in canciones:
                print(f"- {titulo} ({duracion} minutos)")
        else:
            print("Álbum no encontrado.")
    
    elif opc == 4:
        anio = input("Ingrese el año de lanzamiento: ")
        albumes = musicTracker.buscarAlbumesAnio(anio)
        if albumes:
            print(f"Álbumes lanzados en {anio}:")
            for album in albumes:
                print(f"- {album.nombre} por {', '.join(artista.nombre for artista in album.artistas)}")
        else:
            print("No se encontraron álbumes para el año especificado.")
    
    elif opc == 5:
        guardarDatos(musicTracker)
        flag = False
        print("Saliendo del sistema...")
    
    else:
        print("Opción no válida, por favor intente de nuevo.")