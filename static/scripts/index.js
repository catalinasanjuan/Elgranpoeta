document.addEventListener('DOMContentLoaded', function() {
    // Gráfico de barras
    var ctx1 = document.getElementById('chart1').getContext('2d');
    var chart1 = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: ['Producto 1', 'Producto 2', 'Producto 3'],
            datasets: [{
                label: 'Entradas',
                data: [12, 19, 3],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }, {
               label: 'Salidas',
                data: [5, 2, 3],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Gráfico de líneas
    var ctx2 = document.getElementById('chart2').getContext('2d');
    var chart2 = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
            datasets: [{
                label: '2024',
                data: [65, 59, 80, 81, 56],
                fill: false,
                borderColor: 'rgba(54, 162, 235, 1)',
                tension: 0.1
            }, {
                label: '2023',
                data: [28, 48, 40, 19, 86],
                fill: false,
                borderColor: 'rgba(255, 99, 132, 1)',
                tension: 0.1
            }]
        }
    });

    // Inicializar calendario (puedes usar una biblioteca de calendario o construir uno personalizado)
    var calendarEl = document.getElementById('calendar');
    calendarEl.innerHTML = '<p>Calendario va aquí</p>';
});
