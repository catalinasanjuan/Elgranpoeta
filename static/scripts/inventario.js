function filtrarProductos() {
    const codigo = document.getElementById('codigo').value.toLowerCase();
    const descripcion = document.getElementById('descripcion').value.toLowerCase();
    const tipoProducto = document.getElementById('tipo_producto').value.toLowerCase();

    const filas = document.querySelectorAll('#product-list tr');

    filas.forEach(fila => {
        const nombreProducto = fila.children[0].innerText.toLowerCase();
        const descripcionProducto = fila.children[1].innerText.toLowerCase();
        const categoriaProducto = fila.children[4].innerText.toLowerCase();

        let mostrarFila = true;

        if (codigo && !nombreProducto.includes(codigo)) {
            mostrarFila = false;
        }
        if (descripcion && !descripcionProducto.includes(descripcion)) {
            mostrarFila = false;
        }
        if (tipoProducto && !categoriaProducto.includes(tipoProducto)) {
            mostrarFila = false;
        }

        if (mostrarFila) {
            fila.style.display = '';
        } else {
            fila.style.display = 'none';
        }
    });
}
