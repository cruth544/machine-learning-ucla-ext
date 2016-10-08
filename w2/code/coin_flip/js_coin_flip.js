
function randInt( n ) {
  return Math.floor( Math.random() * n );
}

function getMinIn( arr ) {
  var min = arr[0];
  for (var i = 0; i < arr.length; i++) {
    min = Math.min( min, arr[i] );
  }
  return min;
}

function runExperiment( numFlips, numCoins, numExperiments ) {
  var results = [];
  for (var i = 0; i < numExperiments; i++) {
    // console.log( "experiment #", i)
    //experiment
    var headCountCoins = [];
    for (var j = 0; j < numCoins; j++) {
      // console.log( "  coin #", j)
      // coin
      var headCount = 0;
      for (var k = 0; k < numFlips; k++) {
        // console.log( "    flip #", k)
        // flip
        headCount += randInt( 2 );
      }

      headCountCoins.push( headCount );
    }

    results.push({
      v1: headCountCoins[0],
      vRand: headCountCoins[randInt( headCountCoins.length )],
      vMin: getMinIn( headCountCoins )
    })
    headCountCoins = [];
  }
  return results.length;
}



console.log( runExperiment( 10, 1000, 1000 ));
