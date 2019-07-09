const http = require('http')

const server = http.createServer()

const result = () => {
    const x = 5
    const list = []
    for (let i = 0; i < 10; i++) {
        list.push(i * 5)
    }
    return list
}

console.log(result())

server.listen(1996)
