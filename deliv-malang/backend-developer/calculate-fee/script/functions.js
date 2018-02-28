module.exports = {

	// <= 1 KM += 4000 # price
	//  > 1 KM += 2000 # price
	// 16 - 19 += 3000 # rush hour
	// 100k kelipatan 1 dari 50k += 2000 # kelipatan harga 50ribu
	// 26000/10% = 2600 # share
    fare: function(km, time, price) {
        var km = parseInt(km),
            km = km < 1 ? 1 : km,
            cost = km <= 1 ? 4000 : 2000,
            cost = cost * km,
            rush = time >= 16 && time <= 19 ? 3000 : 0,
            cost = cost + rush,
            cost = km > 1 ? cost += 4000 : cost,
            shop = this.shopCost(price),
            cost = cost + shop,
            share = this.tenPercent(cost)
        var result = {
            "cost": cost,
            "share": share
        }
        return result
    },

    isInt: function(value) {
        var x
        if (isNaN(value)) return false
        x = parseFloat(value)
        return (x | 0) === x
    },

    shopCost: function(price) {
        if (price <= 50001 || price <= 99999) return 0
        var total = 0
        for (var index = 0; index < price; index++) {
            if (this.isInt(index / 50000) && index != 0) total += 1
        }
        return 2000 * total
    },

    tenPercent: function(cost) {
        return (10 / 100) * cost;
    },

    // Harvesine Logic - Earth Radius = 6371 (KM)
    // https://stackoverflow.com/a/27943/9137919
    harvesine: function(latlon) {
        var lat1 = latlon.lat1,
            lon1 = latlon.lon1,
            lat2 = latlon.lat2,
            lon2 = latlon.lon2
        var earthr = 6371
        var dLat = this.deg2rad(lat2 - lat1)
        var dLon = this.deg2rad(lon2 - lon1)
        var a =
            Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(this.deg2rad(lat1)) * Math.cos(this.deg2rad(lat2)) *
            Math.sin(dLon / 2) * Math.sin(dLon / 2)
        var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
        var km = earthr * c
        return km
    },

    deg2rad: function(deg) {
        return deg * (Math.PI / 180)
    }

};