var img;

function preload() {
  img = loadImage("/static/img/beach.jpg");
}

function setup() {
  createCanvas(500, 500);
  fill(245, 123, 158);
  textSize(50);
}

function draw(){
  background(200);
  image(img, 0, 0, 200, 200);
  text (key, 245, 245);
}