module.exports = {

  calculate_ongkir: function (km, time, price) {
    var cost = km <= 1 ? 4000 : 2000
    , 	cost = cost * km
    ,	rush = time >= 16 && time <= 19 ? 3000 : 0
    ,	cost = cost + rush
    ,	shop = this.shopCost(price)
    ,	cost = cost + shop
    ,	share= this.tenPercent(cost)
    console.log(share)
  },

  isInt : function (value) {
	var x
	if (isNaN(value)) return false
	x = parseFloat(value)
	return (x | 0) === x
  },

  shopCost : function (price) {
  	if (price <= 50001 || price <= 99999) return 0
  	var total = 0
	for (var index = 0; index < price; index++) {
	  if (this.isInt(index / 50000) && index != 0) total += 1
	}
	return 2000 * total
  },

  tenPercent : function (cost) {
  	return (10 / 100) * cost;
  }

};