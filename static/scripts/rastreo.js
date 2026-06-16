function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: {lat: -33.447487, lng: -70.673676}
    });

    var locations = [
        {lat: -33.393, lng: -70.684, title: 'Bodega Lampa'},
        {lat: -33.466, lng: -70.650, title: 'Bodega Renca'},
        {lat: -33.510, lng: -70.610, title: 'Bodega San Bernardo'}
    ];

    locations.forEach(function(location) {
        var marker = new google.maps.Marker({
            position: location,
            map: map,
            title: location.title
        });
    });
}

function moverProducto() {
    alert('Funcionalidad de mover producto.');
}

function actualizarProducto() {
    alert('Funcionalidad de actualizar producto.');
}

function guardarProducto() {
    alert('Funcionalidad de guardar producto.');
}

// Función para agregar filas a la tabla
document.addEventListener('DOMContentLoaded', function() {
    const productoSelect = document.getElementById('producto');
    productoSelect.addEventListener('change', function() {
        const productoList = document.getElementById('producto-list');
        productoList.innerHTML = '';  // Limpiar lista actual
        const selectedProducto = productoSelect.value;

        if (selectedProducto) {
            // Datos de ejemplo, reemplazar con datos reales
            const productos = [
                {nombre: 'Rayuela', cantidad: 80, ubicacion: 'Bodega San Bernardo', precio: '$5.800'},
                {nombre: 'Rayuela', cantidad: 40, ubicacion: 'Bodega Lampa', precio: '$5.800'}
            ];

            productos.forEach(function(producto) {
                if (producto.nombre === selectedProducto) {
                    const row = document.createElement('tr');
                    row.innerHTML = `<td>${producto.nombre}</td>
                                     <td>${producto.cantidad}</td>
                                     <td>${producto.ubicacion}</td>
                                     <td>${producto.precio}</td>`;
                    productoList.appendChild(row);
                }
            });
        }
    });
});
