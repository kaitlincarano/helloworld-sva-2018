// Declare a "SerialPort" object
var serial;
var latestData = "waiting for data"; // you'll use this to write incoming data to the canvas
function setup() {
createCanvas(500, 500);
serial = new p5.SerialPort();
serial.open("/dev/cu.usbserial-DN051BT1");
serial.onData(gotData);
}
// Ok here comes data!
function gotData() {
// Step 4a: read the data
var currentString = serial.readLine(); // read the incoming string
if (!currentString) return; // if the string is empty, do no more
latestData = Number(currentString); // save it for the draw method
}
function draw() {
background(255, 255, 255);
var data = map(latestData, 0, 1023, 0, height);
fill(0, data, 196);
// Step 4b: use the data
ellipse(250, 250, data);
text(data, 10, 10);
text("happy wednesday", 25, data);

var location = map(latestData, 0,1023, 0, width);
text("what's up", location, data);

}
