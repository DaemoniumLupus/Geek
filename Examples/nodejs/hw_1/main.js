const http = require('http');

const server = http.createServer((req, res) => {
    console.log("Запрос получен");

    if (req.url === '/'){
        main += 1;
        res.writeHead(200, {
            'Content-Type':'html:charset=UTF-8',
        });
        res.end(`
            <h1>Welcome to website!</h1>
            <h2><a href="/about">About</a></h2>
            `);
    }else if (req.url === '/about'){
        about += 1;
        res.writeHead(200, {
            'Content-Type': 'html:charset=UTF-8',
        });
        res.end(`
            <h1>About</h1>
            <h2><a href="/">Main Page</a></h2>
            `);
    }else {
        res.writeHead(404, {
            'Content-Type':'html:charset=UTF-8',
        });
        res.end('<h1>Page not found</h1>');
    }
});

const port = 3000;

server.listen(port, () => {
    console.log(`сервер запущен на порту ${port}`);
});