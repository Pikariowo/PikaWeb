const http = require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/AJAX.html' && req.method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello, World!');
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
});

server.listen(54567, () => {
    console.log('Server running at http://127.0.0.1:54567/');
});
