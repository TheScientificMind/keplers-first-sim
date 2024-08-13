const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

let angle = 0;
let previousTime = performance.now();

let a = parseFloat(document.getElementById("a-slider").value); // semi-major axis
let b = parseFloat(document.getElementById("b-slider").value); // semi-minor axis

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    draw();
}

function draw() {
    const currentTime = performance.now();
    const dt = (currentTime - previousTime) / 1000;

    // Update angle based on time
    angle += (2 * Math.PI / 10) * dt;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw sun
    ctx.fillStyle = "#e43f0d";
    ctx.beginPath();
    ctx.arc(window.innerWidth / 2, window.innerHeight / 2, 50, 0, 2 * Math.PI);
    ctx.fill();

    // Draw planet
    ctx.save();

    ctx.translate(canvas.width / 2, canvas.height / 2);

    // Kepler's 1st law
    let eccentricity = Math.sqrt(1 - (b / a) ** 2);
    let radius = (a * (1 - eccentricity ** 2)) / (1 + eccentricity * Math.cos(angle));

    // Correct translation using only radius
    ctx.translate(100*radius * Math.cos(angle), 100*radius * Math.sin(angle));
    
    ctx.fillStyle = "#dad9d9";
    ctx.beginPath();
    ctx.arc(0, 0, 25, 0, 2 * Math.PI);
    ctx.fill();

    ctx.restore();

    previousTime = currentTime;
    window.requestAnimationFrame(draw);
}

function updateA() {
    a = parseFloat(document.getElementById("a-slider").value);
    document.getElementById("a-value").textContent = a;
}

function updateB() {
    b = parseFloat(document.getElementById("b-slider").value);
    document.getElementById("b-value").textContent = b;
}

document.getElementById("a-slider").addEventListener("input", updateA);
document.getElementById("b-slider").addEventListener("input", updateB);

resizeCanvas();

window.addEventListener("resize", resizeCanvas);
