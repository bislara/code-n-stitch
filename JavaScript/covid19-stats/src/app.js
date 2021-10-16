const getCovidStats = require('../index');

const run = async() => {
    let data = await getCovidStats();
    document.getElementById('country').innerText = data['Country'];
    document.getElementById('date').innerText = data['Date'];
    document.getElementById('case').innerText = 'Total Cases: ' + data['Confirmed'];
    document.getElementById('recov').innerText = 'Total Recovered: ' + data['Recovered'];
    document.getElementById('death').innerText = 'Total Deaths: ' + data['Deaths'];

    document.getElementById('submit').addEventListener(
        'click',
        async() => {
            let data = await getCovidStats(document.getElementById('input').value);
            document.getElementById('country').innerText = 'Country: ' + data['Country'];
            document.getElementById('date').innerText = data['Date'];
            document.getElementById('case').innerText = 'Total Cases: ' + data['Confirmed'];
            document.getElementById('recov').innerText = 'Total Recovered: ' + data['Recovered'];
            document.getElementById('death').innerText = 'Total Deaths: ' + data['Deaths'];
        }
    )
}

run();