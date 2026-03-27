// noinspection JSUnusedLocalSymbols
const { readFile, readFileSync } = require('fs')

readFile('./stuff-to-read.txt', 'utf8', (err, data) => {
    console.log(data)
})

console.log('Hello, world!')
