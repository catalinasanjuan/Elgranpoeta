
function generarReporte() {
    const reportType = document.getElementById('report-type').value;
    const reportes = document.querySelectorAll('.reporte');
    
    reportes.forEach(reporte => {
        if (reporte.id === reportType) {
            reporte.style.display = 'block';
        } else {
            reporte.style.display = 'none';
        }
    });
}

function imprimirReporte() {
    window.print();
}

// Inicializar los reportes para que estén ocultos al cargar la página
document.addEventListener('DOMContentLoaded', (event) => {
    const reportes = document.querySelectorAll('.reporte');
    reportes.forEach(reporte => {
        reporte.style.display = 'none';
    });
});
