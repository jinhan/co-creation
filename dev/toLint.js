"use strict"

var last_time; // for keeping track of drawing speed
var screen_width, screen_height, temperature_slider;
function clear_screen() {
  // console.log("CLEAR")
  fill(255);
  noStroke();
  // rect(0, 0, screen_width, screen_height-41);
  rect(0, 0, screen_width, screen_height);
  stroke(0);
};

function get_window_width() {
  // return windowWidth;
  return window.innerWidth;
}

function get_window_height() {
  // return windowHeight;
  return window.innerHeight;
}

function setup () {
  canvas = createCanvas(screen_width, screen_height);
  frameRate(30);
  clear_screen();
  last_time = +new Date();
}
/*
function draw_sketch(s) {
  var pen_down = false;
  var cur_x = 0;
  var cur_y = 0;
  // ellipse(0, 0, 10);
  noFill();
  for (var i=0; i<s.length; i++) {
    p = s[i];
    next_x = cur_x + p[0];
    next_y = cur_y + p[1];
    if(pen_down) {
      if(i == curSeg) {
        stroke(0, 0, 220);
        strokeWeight(2);
        ellipse(cur_x, cur_y, 5);
        ellipse(next_x, next_y, 5);
      }
      else {
        strokeWeight(1);
        stroke(0);
      }
      line(cur_x, cur_y, next_x, next_y);
    }
    cur_x = next_x;
    cur_y = next_y;
    pen_down = (p[2] == 0);
  }
}
*/
function draw () {
  screen_width = get_window_width();
  screen_height = get_window_height();
  console.log(screen_width, screen_height);
}
/*
function keyTyped() {
  if (key == '!') {
    saveBlocksImages();
  }
  else if (key == '@') {
    saveBlocksImages(true);
  }
}

function keyPressed() {
  if (keyCode == LEFT_ARROW) {
  }
  else if (keyCode == RIGHT_ARROW) {
  }
}
*/
