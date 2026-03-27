const { readFile } = require('fs').promises;
// noinspection JSUnusedGlobalSymbols


module.exports = {
    luckyNumber: () => {
        return 29;
    },

    nanosToMillis: (nanos) => {
        return nanos / 1000000;
    },

    readAndLogSomeRandomStuff: () => {
        readFile('./stuff-to-read.txt', 'utf8', (err, data) => {
            console.log(data)
        })
    }
}
