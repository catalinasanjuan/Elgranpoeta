function verBodega() {
    var nombreBodega = document.getElementById("nombre_bodega").value;
    fetch(`/bodegas/${nombreBodega}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                var bodegaList = document.getElementById("bodega-list");
                bodegaList.innerHTML = `
                <table>
                    <thead>
                        <tr>
                            <th>Nombre de la Bodega</th>
                            <th>Capacidad</th>
                            <th>Calle</th>
                            <th>Número</th>
                            <th>Ciudad</th>
                            <th>Región</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>${data.nombre_bodega}</td>
                            <td>${data.capacidad}</td>
                            <td>${data.calle}</td>
                            <td>${data.numero}</td>
                            <td>${data.ciudad}</td>
                            <td>${data.region}</td>
                            <td><button onclick="window.location.href='/bodegas/editar/${data.nombre_bodega}'">Modificar</button></td>
                        </tr>
                    </tbody>
                </table>`;
            }
        })
        .catch(error => console.error('Error:', error));
}


function agregarBodega() {
    var nombre = document.getElementById("nombreNuevaBodega").value;
    var capacidad = document.getElementById("capacidadNuevaBodega").value;
    var calle = document.getElementById("calleNuevaBodega").value;
    var numero = document.getElementById("numeroNuevaBodega").value;
    var ciudad = document.getElementById("ciudadNuevaBodega").value;
    var region = document.getElementById("regionNuevaBodega").value;

    var data = {
        nombre: nombre,
        capacidad: capacidad,
        calle: calle,
        numero: numero,
        ciudad: ciudad,
        region: region
    };

    fetch('/bodegas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        cerrarModal('agregarBodegaModal');
    })
    .catch(error => console.error('Error:', error));
}


function agregarProducto() {
    var nombre = document.getElementById("nombreNuevoProducto").value;
    var cantidad = document.getElementById("cantidadNuevoProducto").value;
    var ubicacion = document.getElementById("ubicacionNuevoProducto").value;
    var precio = document.getElementById("precioNuevoProducto").value;
    var descripcion = document.getElementById("descripcionNuevoProducto").value; // Nuevo campo de descripción

    var data = {
        nombre: nombre,
        cantidad: cantidad,
        ubicacion: ubicacion,
        precio: precio,
        descripcion: descripcion // Nuevo campo de descripción
    };

    fetch('/productos/agregar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            cerrarModal('agregarProductoModal');
        })
        .catch(error => console.error('Error:', error));
}

function modificarBodega() {
    var nombre = document.getElementById("nombreModificarBodega").value;
    var capacidad = document.getElementById("capacidadModificarBodega").value;
    var direccion = document.getElementById("direccionModificarBodega").value;

    var data = {
        nombre: nombre,
        capacidad: capacidad,
        direccion: direccion
    };

    fetch(`/bodegas/modificar/${nombre}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            cerrarModal('modificarBodegaModal');
        })
        .catch(error => console.error('Error:', error));
}

function abrirModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
}

function cerrarModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}
