// noinspection JSUnusedLocalSymbols
// noinspection ES6UnusedImports

const { readFile } = require('fs').promises;
const fxns = require('./fxns');
const express = require('express');

const app = express();

console.log('Hello, world!');

app.get('/', async (request, response) => {
    response.send(await readFile('./index.html', 'utf8'));
});

app.listen(process.env.PORT || 3001, () => {
    console.log('Server running on port ' + (process.env.PORT || 3001));
})
