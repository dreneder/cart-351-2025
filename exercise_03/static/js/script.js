/**
 * 
 * THIS IS ALL PART OF EXERCISE 3 PART 3, BUT I WILL MAINTAIN ALL OF MY OLD CODE
 * 
 * 
 * Est dies in nox
 * André Neder
 * 
 * The objective of my exercise is to compose a canvas with a city skyline and a
 * day and night animation are controlled by mouse left to right movements, a sun object and a moon object will
 * do an alternate rotation movement and the background color shifts from dar to light blue
 * low to high mouse movements control the moon phase (ellipse size)

 * Day n Nite
 * André
 * 
 * The objective of my exercise is to compose a small city skyline where the sun and moon move
 */

"use strict";

/**
 * I guess this is not being used at the moment :)
*/
function preload() {
}

let hour;
let moonPhase;
let ampm;

let bg = {
    r: 0,
    g: 0,
    b: 227
};


let sun = {
    x: 0,
    y: 0,
    size: 90, 
};

let moon = {
    x: 0,
    y: 0,
    size: 90
};
// naming the moon phases as earth just because eclipse is too hard to type

let earthMove= {
    w: 0,
    e: 0
};

let earth = {
    w: -45,
    n: -48,
    e: 45,
    s: 48
};
let day = {
    x1: 0,
    y1: 0,
    x2: 0,
    y2: -373
};

let night = {
    x1: 0,
    y1: 0,
    x2: 0,
    y2: 373
};

let angle = 0;

/**
 * Just setting up the canvas
*/
function setup() {
    let canvas = createCanvas(600, 450);
    canvas.parent("p5Container"); // Attach the canvas to the div with id 'p5Container'
    angleMode(DEGREES);
}


/**
 * Description of draw() = where the magic happens
 * I tried to change one of my map functions to constrain to fit the exercise
 * description but the code worked nicely the way it is
*/
function draw() {

// r values: day = 0; night = 68
// g values: day = 178; night = 0


mouseX = constrain(mouseX,0,width)
mouseY = constrain(mouseY,0,height)

angle = map(mouseX, 0,width, -180, 180);

if (angle >= 0) {
bg.r = map(angle, 0, 180, 0, 68);
bg.g = map(angle, 0, 180, 178, 0);
}
else {
    bg.r = map(-angle, 0, 180, 0, 68);
    bg.g = map(-angle, 0, 180, 178, 0);
}

background(bg.r, bg.g, bg.b);


 // setting up the sun
 sun.x = day.x + -300;
 sun.y = day.y + -450; 
 


 // sun rotation is based on a line shape (day)
 push();
 translate(300, 450);
 rotate(angle);
 noStroke();
 line(day.x1, day.y1, day.x2, day.y2);
 
 sun.x = day.x2;
 sun.y = day.y2;
 noStroke(); 
 fill(255, 166, 0);
 ellipse(sun.x, sun.y, sun.size);
 pop();
 
 // the moon movement is the same as the sun, based on the opposed value
 moon.x = day.x + -300;
 moon.y = day.y + -450;
 
 
 push();
 translate(300, 450);
 rotate(angle);
 noStroke();
 line(night.x1, night.y1, night.x2, night.y2);
 
 moon.x = night.x2;
 moon.y = night.y2;
 noStroke(); 
 fill(255);
 ellipse(moon.x, moon.y, moon.size);
 fill(255,0,0);
 
 // this is the moon phase movement
 earth.w = map(mouseY, 225, height, 45, -45, true);
 earth.e = map(mouseY, 0, 225, 45, -45, true)
 
 push();
 ellipseMode(CORNERS);
 fill(bg.r, bg.g, bg.b);
 
 ellipse(moon.x+earth.e, moon.y+earth.s, moon.x+earth.w, moon.y+earth.n);
 pop();
 
 pop();


 
 
    
    //drawing the skyline, I listened to a podcast and actually had fun doing this, please don't judge me
    push();
    translate(0, 0);

    noStroke();
    fill(50);
    beginShape();
    vertex(0, 450);
    vertex(0, 225);
    vertex(42, 276);
    vertex(27, 276);
    vertex(27, 373);
    vertex(66, 373);
    vertex(66, 360);
    vertex(78, 360);
    vertex(78, 302);
    vertex(90, 302);
    vertex(90, 251);
    vertex(102, 251);
    vertex(102, 186);
    vertex(114, 186);
    vertex(114, 161);
    vertex(123, 161);
    vertex(123, 129);
    vertex(142, 129);
    vertex(142, 161);
    vertex(150, 161);
    vertex(150, 186);
    vertex(170, 186);
    vertex(170, 251);
    vertex(188, 251);
    vertex(188, 302);
    vertex(197, 302);
    vertex(197, 360);
    vertex(186, 360);
    vertex(186, 373);
    vertex(186, 373);
    vertex(186, 212);
    vertex(234, 129);
    vertex(234, 369);
    vertex(249, 354);
    vertex(264, 369);
    vertex(264, 328);
    vertex(279, 328);
    vertex(279, 307);
    vertex(294, 307);
    vertex(294, 193);
    vertex(325, 141);
    vertex(342, 141);
    vertex(372, 193);
    vertex(372, 368);
    vertex(390, 368);
    vertex(390, 257);
    vertex(414, 257);
    vertex(414, 315);
    vertex(444, 283);
    vertex(474, 315);
    vertex(474, 257);
    vertex(498, 257);
    vertex(498, 373);
    vertex(516, 373);
    vertex(516, 347);
    vertex(534, 347);
    vertex(534, 289);
    vertex(552, 289);
    vertex(552, 193);
    vertex(570, 193);
    vertex(570, 129);
    vertex(600, 129);
    vertex(600, 450);
    endShape(CLOSE);
    

   
    

     pop();
 
// addidng parameters to hour and moon phase
hour = map(mouseX, 0, width, 0, 24);
if (hour >= 24) {
    hour -= 24;
}
if (hour >= 12) {
    ampm = "PM";
    if (hour > 13){
        hour -= 12;
        }
    if (hour === 0) {
        hour = 12;
    }
} else {
  ampm = "AM";
  if (hour < 1){
    hour = 12;}
}

if (mouseY <= height/2) {
  moonPhase = map(mouseY, 0, height/2, 100, 0);
} 
else if (mouseY <= height/4*3) {
  moonPhase = map(mouseY, height/2, height/4*3, 0, 50);
} 
else {
  moonPhase = map(mouseY, height/4*3, height, 50, 0);
}
}

function mouseReleased() {
    sendData({ hour: floor(hour)+' '+ampm, moon: 'Moon at '+floor(moonPhase)+'%'});
    fetchLatestData();
    // text(`${floor(moonPhase)}% - ${floor(hour)},${ampm}`,width/2,height-20); 
}

/* function to send data to server, copied from the tutorial */
async function sendData(params) {
    const formData = new FormData();
    formData.append("hour", params.hour);
    formData.append("moon", params.moon);

    try {
        let res = await fetch("/postDataFetch", {
            method: "POST",
            body: formData
        });
        let resJSON = await res.json();
        console.log(resJSON);
        gameState = 'end';
    } catch (err) {
        console.log(err);
    }
}

async function fetchLatestData() {
    try {
        const res = await fetch("/latestHour");
        const data = await res.json();
        document.getElementById("lastHour").textContent = `${data.hour} — ${data.moon}`;
    } catch (err) {
        console.error(err);
    }
}

window.addEventListener("DOMContentLoaded", () => {
  fetchLatestData(); //
});
