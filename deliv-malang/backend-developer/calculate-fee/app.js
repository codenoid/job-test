const express = require('express')
const app = express()
const ejs = require('ejs')
const functions = require('./script/functions')

app.set('view engine', 'ejs')
app.use(express.static('public'))

app.get('/', function (req, res) { res.render('index') })

app.get('/calculate', function (req, res) {
	res.setHeader('Content-Type', 'application/json');
	var la1   = req.query.lat1
	,	lo1   = req.query.lon1
	,	la2   = req.query.lat2
	,	lo2   = req.query.lon2
	,	date  = req.query.h
	,	price = req.query.price
	var km   = functions.harvesine({lat1: la1, lon1: lo1, lat2: la2, lon2: lo2})
	var kms  = '' + km;
	var rkm  = kms[0] + "." + kms[2]
	var fare = functions.fare(km, date, price);
	var ret  = {"distance": rkm, "cost": fare.cost, "share": fare.share}
    res.send(JSON.stringify(ret));
})

app.listen(3000, () => console.log('Node App Running on port 3000!'))
