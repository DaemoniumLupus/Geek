const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();

const port = 3000;

let counts = require('./counts.json');

app.use((req, res, next) => {
    if (req.url == '/') {
        counts.main += 1;
    }else if (req.url == '/about'){
        counts.about += 1;
    }
    fs.writeFileSync('./counts.json', JSON.stringify(counts));
    next();
});

app.get('/', (req, res) => {
    res.send(`
        <h1>Welcome to website!</h1>
        <h2>Просмотров: ${counts.main}</h2>
        <h2><a href="/about">Link for About</a></h2>
        `)
});

app.get('/about', (req, res) => {
    res.send(`
        <h1>About</h1>
        <h2>Просмотров: ${counts.about}</h2>
        <h2><a href="/">Link for /</a></h2>
        `)
})

app.listen(port, () => {
    console.log(`Сервер запущен на порту ${port}`);
});