document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('leaveCalendar');
    const dataEl = document.getElementById('leaves-data');

    if (!calendarEl || !dataEl) {
        console.error("Calendar element or leaves-data not found");
        return;
    }

    const rawLeaves = JSON.parse(dataEl.textContent);

    const events = rawLeaves.map(l => ({
        title: `${l.leave_type} (${l.status})`,
        start: l.start_date,
        // FullCalendar treats end date as exclusive, so add 1 day
        end: new Date(new Date(l.end_date).getTime() + 86400000)
            .toISOString()
            .slice(0, 10),
        allDay: true,
        backgroundColor: l.status === 'Approved' ? '#6366f1' : '#fbbf24',
        borderColor: 'transparent'
    }));

    window.calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: ''
        },
        height: 650,
        fixedWeekCount: false,
        dayMaxEventRows: 2,
        events: events
    });

    window.calendar.render();
});
