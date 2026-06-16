$(document).ready(function() {
    $('#calendar').fullCalendar({
        height: 400,  // Ajusta la altura del calendario según tus necesidades
        width: 300,   // Ajusta el ancho del calendario según tus necesidades
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month'
        },
        defaultView: 'month',
        editable: false,
        events: [
            {
                title: 'Evento 1',
                start: '2024-06-01'
            },
            {
                title: 'Evento 2',
                start: '2024-06-15'
            }
        ]
    });
});
