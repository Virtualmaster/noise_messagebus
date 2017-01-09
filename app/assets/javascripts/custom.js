MessageBus.start(); // call once at startup

var maxNoise = 0

// how often do you want the callback to fire in ms
MessageBus.callbackInterval = 10;
MessageBus.enableChunkedEncoding = false;

MessageBus.subscribe("/noise_level", function(noiseLevel) {
  if (noiseLevel > maxNoise) {
    maxNoise = noiseLevel
  }

  $('#highcharts_container').highcharts().series[0].addPoint(noiseLevel,true,true,false)
  $('#highcharts_container').highcharts().series[1].addPoint(maxNoise,true,true,false)
})