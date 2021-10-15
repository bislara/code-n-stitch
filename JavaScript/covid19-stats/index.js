const axios = require('axios');

class CovidStats {
    constructor(payload) {
        const {
            Country,
            TotalConfirmed,
            TotalDeaths,
            TotalRecovered,
            Date,
        } = payload;

        this.Country = Country;
        this.Date = Date;
        this.Confirmed = TotalConfirmed;
        this.Deaths = TotalDeaths;
        this.Recovered = TotalRecovered;

    }
}

const getCovidStats = async(country = 'Global') => {
    const response = await axios.get('https://api.covid19api.com/summary')

    if (country.toLowerCase() === 'global') {
        return new CovidStats({ Country: 'Global', ...response['data']['Global'] });
    }

    for (data of response['data']['Countries']) {
        if (country.length = 2) {
            if (country.toLowerCase() === data['CountryCode'].toLowerCase()) {
                return new CovidStats({...data })
            }
        }

        if (country.length > 2) {
            if (country.toLowerCase() === data['Slug']) {
                return new CovidStats({...data })
            }
        }
    }
}

module.exports = getCovidStats;