


// Once you have installed Node, let's try building our first web server. Create a file named "app.js", and paste the following code:

const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hi pi loves John and john loves my cakes. we could make cupcakes?\n');
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});