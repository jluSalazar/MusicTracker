# ––––––––– Clase Album –––––––––––
class Album:
    def __init__(self, nombre, anio_lanzamiento, disquera, artistas):
        self.nombre = nombre
        self.anio_lanzamiento = anio_lanzamiento
        self.disquera = disquera
        self.artistas = artistas  # Lista de objetos Artista
        self.canciones = []  # Lista de objetos Cancion

    def agregar_cancion(self, cancion):
        if not self.verificar_titulo_repetido(cancion.titulo):
            self.canciones.append(cancion)
        else:
            raise ValueError("La canción con el título '{}' ya existe en el álbum.".format(cancion.titulo))

    def verificar_titulo_repetido(self, titulo):
        return any(cancion.titulo == titulo for cancion in self.canciones)

    def listar_canciones(self):
        return [(cancion.titulo, cancion.duracion) for cancion in self.canciones]

# ––––––––––– Clase Cancion ––––––––––
class Cancion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

# –––––––––– Clase Artista –––––––––––
class Artista:
    def __init__(self, nombre, pais_origen):
        self.nombre = nombre
        self.pais_origen = pais_origen

# ––––––––– Clase MusicTracker –––––––––––––––
class MusicTracker:
    def __init__(self):
        self.albumes = []  # Lista de objetos Album

    def agregar_album(self, nombre, anio_lanzamiento, disquera, artistas):
        nuevo_album = Album(nombre, anio_lanzamiento, disquera, artistas)
        self.albumes.append(nuevo_album)
        return nuevo_album

    def agregar_cancion_album(self, nombre_album, titulo_cancion, duracion):
        album = self.buscar_album_nombre(nombre_album)
        if album:
            nueva_cancion = Cancion(titulo_cancion, duracion)
            album.agregar_cancion(nueva_cancion)
        else:
            raise ValueError("Álbum no encontrado.")

    def buscar_album_nombre(self, nombre):
        for album in self.albumes:
            if album.nombre == nombre:
                return album
        return None

    def buscar_albumes_anio(self, anio):
        return [album for album in self.albumes if album.anio_lanzamiento == anio]

# ––––––––––– Clase Main ––––––––––––––
class Main:
    @staticmethod
    def mostrar_menu():
        print("\tMenú de Opciones")
        print("1. Agregar un nuevo Álbum")
        print("2. Agregar canción a Álbum Existente")
        print("3. Ver Canciones de Álbum")
        print("4. Buscar Álbum por Año")
        print("5. Salir")

    @staticmethod
    def obtener_artistas():
        artistas = []
        while True:
            nombre_artista = input("Ingrese el nombre del artista (o 'fin' para terminar): ")
            if nombre_artista.lower() == 'fin':
                break
            pais_origen = input(f"Ingrese el país de origen de {nombre_artista}: ")
            artistas.append(Artista(nombre_artista, pais_origen))
        return artistas

    @staticmethod
    def guardar_datos(music_tracker):
        with open("albumes_y_canciones.txt", "w") as file:
            for album in music_tracker.albumes:
                file.write(f"Álbum: {album.nombre}\n")
                file.write(f"Año de Lanzamiento: {album.anio_lanzamiento}\n")
                file.write(f"Disquera: {album.disquera}\n")
                file.write(f"Artistas: {', '.join(artista.nombre for artista in album.artistas)}\n")
                file.write("Canciones:\n")
                for cancion in album.canciones:
                    file.write(f"\t- {cancion.titulo} ({cancion.duracion} minutos)\n")
                file.write("\n")
        print("Datos guardados en 'albumes_y_canciones.txt'.")

    @staticmethod
    def cargar_datos(nombre_archivo):
        music_tracker = MusicTracker()
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
                music_tracker.albumes.append(album_actual)
            elif linea.startswith("Año de Lanzamiento:"):
                anio_lanzamiento = linea[len("Año de Lanzamiento: "):]
                album_actual.anio_lanzamiento = anio_lanzamiento
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
        if not music_tracker.albumes:
            return None
        print("Datos cargados desde '{}'.".format(nombre_archivo))
        return music_tracker

    def __init__(self):
        self.music_tracker = self.cargar_datos("albumes_y_canciones.txt")
        if self.music_tracker is None:
            self.music_tracker = MusicTracker()

    def ejecutar(self):
        flag = True
        while flag:
            self.mostrar_menu()
            opc = input("Seleccione una opción (número): ")
            if not opc.isdigit():
                print("Por favor, ingrese un número válido.")
                continue
            opc = int(opc)
            if opc == 1:
                self.opcion_agregar_album()
            elif opc == 2:
                self.opcion_agregar_cancion_album()
            elif opc == 3:
                self.opcion_ver_canciones_album()
            elif opc == 4:
                self.opcion_buscar_album_anio()
            elif opc == 5:
                self.guardar_datos(self.music_tracker)
                flag = False
                print("Saliendo del sistema...")
            else:
                print("Opción no válida, por favor intente de nuevo.")

    def opcion_agregar_album(self):
        nombre = input("Ingrese el nombre del álbum: ")
        anio_lanzamiento = input("Ingrese el año de lanzamiento: ")
        disquera = input("Ingrese el nombre de la disquera: ")
        artistas = self.obtener_artistas()
        self.music_tracker.agregar_album(nombre, anio_lanzamiento, disquera, artistas)
        print("Álbum agregado exitosamente.")

    def opcion_agregar_cancion_album(self):
        nombre_album = input("Ingrese el nombre del álbum: ")
        titulo_cancion = input("Ingrese el título de la canción: ")
        duracion = input("Ingrese la duración de la canción (en minutos): ")
        try:
            self.music_tracker.agregar_cancion_album(nombre_album, titulo_cancion, duracion)
            print("Canción agregada exitosamente.")
        except ValueError as e:
            print(e)

    def opcion_ver_canciones_album(self):
        nombre_album = input("Ingrese el nombre del álbum: ")
        album = self.music_tracker.buscar_album_nombre(nombre_album)
        if album:
            canciones = album.listar_canciones()
            print(f"Canciones en el álbum '{nombre_album}':")
            for titulo, duracion in canciones:
                print(f"- {titulo} ({duracion} minutos)")
        else:
            print("Álbum no encontrado.")

    def opcion_buscar_album_anio(self):
        anio = input("Ingrese el año de lanzamiento: ")
        albumes = self.music_tracker.buscar_albumes_anio(anio)
        if albumes:
            print(f"Álbumes lanzados en {anio}:")
            for album in albumes:
                print(f"- {album.nombre} por {', '.join(artista.nombre for artista in album.artistas)}")
        else:
            print("No se encontraron álbumes para el año especificado.")

if __name__ == "__main__":
    main = Main()
    main.ejecutar()
