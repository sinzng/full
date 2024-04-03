const express = require('express')
const bodyParser = require('body-parser')
const XMLHttpRequest = require("xhr2");

const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.json())
app.use(express.urlencoded({ extended:true }))


app.get('/Hello', (req, res) => {
    res.send("Hello World")
})

// get data
app.get('/getData', async (req, res) => {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "http://localhost:5000/users")
    xhr.setRequestHeader("content-type", "application/json")
    xhr.send()

    xhr.onload = () => {
        if (xhr.status === 200) {
            const res = JSON.parse(xhr.response);
            console.log(res);
        } else {
            console.log(xhr.status, xhr.statusText);
        }
        res.send(xhr.response)
    }
})

// post data
app.post('/postData', async (req, res) => {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/users")
    xhr.setRequestHeader("content-type", "application/json;charset=UTF-8")
    const data = {id : req.body.id, name:req.body.name, }
    xhr.send(JSON.stringify(data)) // stringify : 

    xhr.onload = () => {
        if (xhr.status === 200) {
            const res = JSON.parse(xhr.response);
            console.log(res);
        } else {
            console.log(xhr.status, xhr.statusText);
        }
        res.send(xhr.response)
    }
})

// put data(update)
app.post('/putData', async (req, res) => {
    const xhr = new XMLHttpRequest();
    xhr.open("PUT", "http://localhost:5000/users/"+req.body.id)
    xhr.setRequestHeader("content-type", "application/json;charset=UTF-8")
    const data = {id : req.body.id, name:req.body.name, }
    xhr.send(JSON.stringify(data)) // stringify : 

    xhr.onload = () => {
        if (xhr.status === 200) {
            const res = JSON.parse(xhr.response);
            console.log(res);
        } else {
            console.log(xhr.status, xhr.statusText);
        }
        res.send(xhr.response)
    }
})

// delete data(update)
app.post('/deleteData', async (req, res) => {
    const xhr = new XMLHttpRequest();
    xhr.open("DELETE", "http://localhost:5000/users/"+ req.body.id)
    xhr.setRequestHeader("content-type", "application/json;charset=UTF-8")
    xhr.send()

    xhr.onload = () => {
        if (xhr.status === 200) {
            const res = JSON.parse(xhr.response);
            console.log(res);
        } else {
            console.log(xhr.status, xhr.statusText);
        }
        res.send(xhr.response)
    }
})

module.exports = app; 