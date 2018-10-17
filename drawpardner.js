function setup() {
  createCanvas(500, 500);
  strokeWeight(20)
  background(255);
}

function mouseDragged() {
  // drag to draw a line from previouse mouse position
  // to current mouse position
  line(mouseX, mouseY, pmouseX, pmouseY);
  if (keyIsPressed === true) {
    strokeWeight(40);
    stroke(150,255,169);
  } else {
    strokeWeight(20);
    stroke(random(255),random(255),random(255));
  }
}
