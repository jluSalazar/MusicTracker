# Historias de Usuario

## HU1: Agregar un Nuevo Álbum

**Como** usuario,  
**Quiero** poder agregar un nuevo álbum con su información básica (nombre, año de lanzamiento, disquera y artistas),  
**Para** mantener un registro de la música que escucho.

### Detalles Adicionales
- **Campos requeridos**: Nombre del álbum, Año de lanzamiento, Disquera, Artistas.
- **Validación**: El año de lanzamiento debe ser un año válido (ej. hasta 2024).

## HU2: Agregar Canciones a un Álbum Existente

**Como** usuario,  
**Quiero** poder agregar canciones a un álbum existente, proporcionando el título de la canción y su duración en minutos,  
**Para** mantener un registro completo de todas las canciones en un álbum.

### Detalles Adicionales
- **Campos requeridos**: Título de la canción, Duración en minutos.
- **Validación**: La duración debe ser un número positivo.

## HU3: Evitar Títulos de Canciones Repetidos

**Como** usuario,  
**Quiero** que el sistema evite que agregue canciones con títulos repetidos a un álbum,  
**Para** mantener la integridad de la información.

### Detalles Adicionales
- **Regla de negocio**: No se pueden agregar canciones con el mismo título dentro del mismo álbum.
- **Mensajes de error**: "Ya existe una canción con este título en el álbum."

## HU4: Ver la Lista de Canciones de un Álbum

**Como** usuario,  
**Quiero** poder ver la lista de canciones de un álbum específico, junto con su duración,  
**Para** conocer la composición del álbum.

### Detalles Adicionales
- **Información mostrada**: Título de la canción, Duración.
- **Formato de visualización**: Lista detallada.

## HU5: Buscar Álbumes por Año

**Como** usuario,  
**Quiero** poder buscar álbumes por el año,  
**Para** encontrar rápidamente la información que estoy buscando.

### Detalles Adicionales
- **Filtro de búsqueda**: Año.
- **Resultados**: Mostrar una lista de álbumes toda su información.
