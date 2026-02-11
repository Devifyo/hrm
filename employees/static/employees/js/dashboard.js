
        $(document).ready(function() {
            // Clock
            const updateTime = () => {
                const now = new Date();
                $('#liveClock').text(now.toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit' }));
                $('#liveDate').text(now.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' }));
            };
            setInterval(updateTime, 1000); updateTime();

            // Timer Logic
            let isClockedIn = false, timerInt, totalSecs = 0;
            const format = s => new Date(s * 1000).toISOString().substr(11, 8);
            $('#clockBtn').click(function() {
                if(!isClockedIn) {
                    isClockedIn = true;
                    $(this).removeClass('bg-gray-900 hover:bg-indigo-600').addClass('bg-red-500 hover:bg-red-600');
                    $('#btnText').text('Clock Out'); $('#timerDisplay').addClass('timer-active text-gray-800').removeClass('text-gray-400');
                    timerInt = setInterval(() => $('#timerDisplay').text(format(++totalSecs)), 1000);
                } else {
                    isClockedIn = false; clearInterval(timerInt);
                    $(this).removeClass('bg-red-500 hover:bg-red-600').addClass('bg-gray-900 hover:bg-indigo-600');
                    $('#btnText').text('Clock In'); $('#timerDisplay').removeClass('timer-active text-gray-800').addClass('text-gray-400');
                    alert(`Worked: ${format(totalSecs)}`);
                }
            });
        });