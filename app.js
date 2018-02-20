const express = require('express')
const app = express()
const ejs = require('ejs')
const functions = require('./script/functions')

app.set('view engine', 'ejs')

// respond with "hello world" when a GET request is made to the homepage
app.get('/', function (req, res) {
  functions.calculate_ongkir(7, 17, 237240)
  res.render('index', { title: 'Hey', message: 'Hello there!' })
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))
