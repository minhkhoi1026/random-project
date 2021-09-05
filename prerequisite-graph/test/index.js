const express = require('express')
const cors = require('cors')
const http = require('http')

const app = express()
app.use(cors())

server = http.createServer(app)

app.get('/', (request, response) => {
    response.sendFile(`${__dirname}/index.html`);
})

app.get('/:filename', (request, response) => {
    response.sendFile(`${__dirname}/${request.params.filename}`);
})

const PORT = 3007
server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`)
})