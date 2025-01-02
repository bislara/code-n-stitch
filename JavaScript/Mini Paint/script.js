const canvas = document.getElementById('paint-canvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth * 0.8;
canvas.height = window.innerHeight * 0.7;

let painting = false;
let currentColor = '#000000';
let brushSize = 5;
let isEraser = false;

// Start drawing
function startDrawing(e) {
  painting = true;
  draw(e);
}

// Stop drawing
function stopDrawing() {
  painting = false;
  ctx.beginPath();
}

// Draw on the canvas
function draw(e) {
  if (!painting) return;

  ctx.lineWidth = brushSize;
  ctx.lineCap = 'round';
  ctx.strokeStyle = isEraser ? '#FFFFFF' : currentColor;

  ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
}

// Clear canvas
document.getElementById('clear-board').addEventListener('click', () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
});

// Change color
document.getElementById('color-picker').addEventListener('input', (e) => {
  currentColor = e.target.value;
  isEraser = false;
  canvas.style.cursor = 'crosshair';
});

// Change brush size
document.getElementById('brush-size').addEventListener('input', (e) => {
  brushSize = e.target.value;
});

// Toggle eraser
document.getElementById('eraser').addEventListener('click', () => {
  isEraser = true;
  canvas.style.cursor = 'not-allowed';
});

//Added button to switch pencil function
//dynamic pencil button
const toolbar=document.querySelector('.toolbar');
const pencil=document.createElement('button');
pencil.id='pencil';
pencil.textContent='Pencil';
//Button is created
toolbar.appendChild(pencil);

document.getElementById('pencil').addEventListener('click', () => {
  isEraser = false;
  canvas.style.cursor = 'crosshair';
})

// Download as PNG
document.getElementById('download-png').addEventListener('click', () => {
  const link = document.createElement('a');
  link.download = 'drawing.png';
  link.href = canvas.toDataURL();
  link.click();
});

// Download as JPG
document.getElementById('download-jpg').addEventListener('click', () => {
  const link = document.createElement('a');
  link.download = 'drawing.jpg';
  link.href = canvas.toDataURL('image/jpeg');
  link.click();
});

// Event listeners for drawing
canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mousemove', draw);
