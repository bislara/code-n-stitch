const prompt = require('prompt');
const getCovidStats = require('./index');

const schema = {
    properties: {
        Country: {
            pattern: /^[a-zA-Z\s\-]+$/,
            message: 'Country is required, and must be a country name or country alpha-2 code',
            required: true
        },
    }
};

prompt.start();

prompt.get(schema, (err, res) => {
    if (err) { console.log(err); }
    getCovidStats(res.Country)
        .then(console.log)
        .catch(console.error);
})