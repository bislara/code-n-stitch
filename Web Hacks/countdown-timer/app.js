const clock = document.getElementById('clock');
const hours = clock.querySelector('.hours');
const minutes = clock.querySelector('.minutes');
const seconds = clock.querySelector('.seconds');

const reset = document.getElementById('reset')
const pause = document.getElementById('pause')
const start = document.getElementById('start')

const time = document.getElementById('time')

time.onchange = function () {
    hours.innerHTML = time.value.split(':')[0];
    minutes.innerHTML = time.value.split(':')[1];
    seconds.innerHTML = time.value.split(':')[2];
}

let pausetog = false
let deadline = 0

start.onclick = function () {
    let times = time.value.split(':')
    deadline = times[0] * 3600000 + times[1] * 60000 + times[2] * 1000
    if (deadline) {
        startClock(new Date(Date.parse(new Date()) + deadline))
    } else {
        alert("Enter a valid time")
    }
}

console.log(clock.classList)

function remainingTime(endtime) {
    const total = Date.parse(endtime) - Date.parse(new Date());
    const seconds = Math.floor((total / 1000) % 60);
    const minutes = Math.floor((total / 1000 / 60) % 60);
    const hours = Math.floor((total / (1000 * 60 * 60)) % 24);

    return { total, hours, minutes, seconds };
}

function startClock(endtime) {
    if (document.getElementById('clock').classList.length) {
        document.getElementById('clock').classList.remove('blink')
    }
    time.disabled = true
    start.innerHTML = 'Start Over'
    function updateClock() {
        const t = remainingTime(endtime);

        hours.innerHTML = ('0' + t.hours).slice(-2);
        minutes.innerHTML = ('0' + t.minutes).slice(-2);
        seconds.innerHTML = ('0' + t.seconds).slice(-2);

        if (t.total <= 0) {
            clearInterval(timeinterval);
            document.getElementById('clock').className += ' blink'
            console.log(clock.classList.length)
        }

        start.onclick = function () {
            if (document.getElementById('clock').classList.length) {
                document.getElementById('clock').classList.remove('blink')
            }
            clearInterval(timeinterval)
            let times = time.value.split(':')
            hours.innerHTML = times[0];
            minutes.innerHTML = times[1];
            seconds.innerHTML = times[2];
            deadline = times[0] * 3600000 + times[1] * 60000 + times[2] * 1000
            if (deadline) {
                startClock(new Date(Date.parse(new Date()) + deadline))
            } else {
                alert("Enter a valid time")
                hours.innerHTML = '00'
                minutes.innerHTML = '00'
                seconds.innerHTML = '00'
            }
        }

        pause.onclick = function () {
            if (!pausetog) {
                pausetog = true
                pause.innerHTML = 'Resume'
                clearInterval(timeinterval);
            } else {
                pausetog = false
                pause.innerHTML = 'Pause'
                let present = hours.innerHTML * 3600000 + minutes.innerHTML * 60000 + seconds.innerHTML * 1000
                startClock(new Date(Date.parse(new Date()) + present))
            }
        }

        reset.onclick = function () {
            if (document.getElementById('clock').classList.length) {
                document.getElementById('clock').classList.remove('blink')
            }
            time.disabled = false
            time.value = '--:--:--'
            start.innerHTML = 'Start'
            hours.innerHTML = '00'
            minutes.innerHTML = '00'
            seconds.innerHTML = '00'
            clearInterval(timeinterval)
        }
    }

    updateClock();
    const timeinterval = setInterval(updateClock, 1000);

}