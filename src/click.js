// 有错误的代码
function calculateTotal(prices) {
  var total;
  for (var price in prices) {
    total += price;
  }
  return total;
}

var myPrices = [100, 150, 200];
var result = calculateTotal(myPrices);
console.log('Total:', result);
