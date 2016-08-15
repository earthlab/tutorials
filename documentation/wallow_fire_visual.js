/* 
Wallow fire time lapse
Author: Zach Schira
Date: 8/8/2016
This script uses FIRMS fire detection product to display the active fire 
every day during the Arizona Wallow fire. It also calculates and plots the 
active fire area by day, and the area change by day. 
*/

//Load data and filter to date range
var firms = ee.ImageCollection('FIRMS');
var wallowFire = firms
.filterDate('2011-05-29', '2011-07-08');
var point = ee.Geometry.Point(-109.281, 34.0049);
var collectionLength = wallowFire.size().getInfo();

// Get only pixels with a high confidence
var confidenceFunction = function(image) {
  var highValue = ee.Image(image).select(['confidence']).gt(50);
  highValue = highValue.set('system:time_start', image.get('system:time_start'));
  return highValue.updateMask(highValue);
};
var fireBand = wallowFire.map(confidenceFunction);

// create buffer of 50000 m radius around center of fire
var bufPoint = ee.Geometry.Point(-109.314, 33.7312);
var buffer = bufPoint.buffer(50000);
var getBuffer = function(image) {
  return image.clip(buffer);
};
fireBand = fireBand.map(getBuffer);
var fire = fireBand.toList(collectionLength);

// Calculate active fire area by day
var calcArea = function(image) {
  var area = image.divide(image);
  area = image.multiply(ee.Image.pixelArea());
  area = area.set('system:time_start', image.get('system:time_start'));
  return area;
};
var areaMap = fireBand.map(calcArea);

//calculate change in area/spread rate
var calcChange = function(image, list) {
  image = image.unmask(1);
  var prev = ee.Image(ee.List(list).get(0));
  var diff = image.subtract(prev);
  diff = diff.set('system:time_start', image.get('system:time_start'));
  var List = ee.List(list).add(diff);
  List = List.replace(prev, image);
  return List;
};
var first = ee.List([ee.Image(0)]);
var diffs = ee.List(areaMap.iterate(calcChange, first));
diffs = ee.ImageCollection(diffs.slice(1, collectionLength + 1));//removve first element


//Create chart of area by day
var areaChart = ui.Chart.image.series({
  imageCollection: areaMap,
  region: buffer,
  reducer: ee.Reducer.sum()
});
// set axis labels
areaChart.setOptions({
  title:'2011 Marrow Fire Daily Active Fire Area (starts 2011-05-29)',
  vAxis: {title: 'Area (m^2)'},
  hAxis: {title: 'Date'},
  legend: 'none'
});
print(areaChart);

//Create chart of area change by day
var deltaArea = ui.Chart.image.series({
  imageCollection: diffs,
  region: buffer,
  reducer: ee.Reducer.sum(),
});
// set axis labels
deltaArea.setOptions({
  title:'2011 Marrow Fire Daily Fire Spread (starts 2011-05-29)',
  vAxis: {title: 'Change in Area (m^2/day)'},
  hAxis: {title: 'Day'},
  legend: 'none'
});
print(deltaArea);

//create outline of max fire area
var maxArea = fireBand.filterDate('2011-06-08','2011-06-09');
maxArea = maxArea.toList(1);
maxArea = ee.Image(maxArea.get(0));
var edges = ee.Algorithms.CannyEdgeDetector(maxArea, 300);

// Helper function to display fire on any given day
var showMax = false;
var getFrame = function(index) {
  Map.layers().reset();
  var image = ee.Image(fire.get(index));
  Map.addLayer(image, {min: 0, max: 10, palette: 'FF0000'});
  var label = ui.Label({style: {position: 'top-center'}});
  image.date().format("YYYY-MM-dd").evaluate(function(date) {
    label.setValue('Date: ' + date);
  });
  Map.add(label);
  // Display max fire
  if(showMax) {
    Map.addLayer({
      eeObject: edges, 
      visParams: {min: 0, max: 1, palette: 'FFFF00'},
      opacity: 0.5    
    });
  }
};

// Create ui to allow user to step through fire
var label = ui.Label('Current Fire on Day (starts 2011-05-29)');
// Slider
var slider = ui.Slider({
  min: 0,
  max: collectionLength - 1,
  step: 1,
  onChange: getFrame,
  style: {stretch: 'horizontal'}
});
// Create button to display max fire area
// Helper function to change state of button
var showFire = function() {
  showMax ^= true;
  getFrame(slider.getValue());
};
var button = ui.Button('Show Maximum Fire Coverage');
button.onClick(showFire);
// Create panel for slider/button
var panel = ui.Panel({
  widgets: [label, slider, button],
  layout: ui.Panel.Layout.flow('vertical'),
  style: {
    position: 'top-left',
    padding: '7px'
  }
});

// Add everything to the map/set map options
Map.add(panel);
Map.setOptions('satellite');
slider.setValue(0);
Map.centerObject(point, 9);
getFrame(slider.getValue());