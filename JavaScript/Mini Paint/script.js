const canvas = document.getElementById('paint-canvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth * 0.8;
canvas.height = window.innerHeight * 0.7;

let painting = false;
let currentColor = '#000000';
let brushSize = 5;
let isEraser = false;
//fill mode toggler
let isFillMode=false;

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
  if (!painting || isFillMode) return;//prevent drawing when fill mode is on

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
const firstButton = toolbar.querySelector('button');
toolbar.insertBefore(pencil, firstButton);

document.getElementById('pencil').addEventListener('click', () => {
  isEraser = false;
  canvas.style.cursor = 'crosshair';
})

//Fill color feature
const fillButton = document.getElementById('fill-color');
fillButton.addEventListener('click',()=>{
  isFillMode=true;
  canvas.style.cursor='pointer';
})

//fill color applies, when clicked on canvas
canvas.addEventListener('click',(e)=>{
  if(isFillMode){
    fillColor(e);
  }
})


// Flood Fill logic
function fillColor(e) {
  const x = e.clientX - canvas.offsetLeft;
  const y = e.clientY - canvas.offsetTop;

  const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
  const targetColor = getPixelColor(imageData, x, y);
  const fillColor = hexToRgb(currentColor);

  // Only perform flood fill if the color is different
  if (!colorsMatch(targetColor, fillColor)) {
    floodFill(imageData, x, y, targetColor, fillColor);
    ctx.putImageData(imageData, 0, 0);
  }

  isFillMode = false; // Reset fill mode after filling
}

// Helper functions for the Flood Fill

function getPixelColor(imageData, x, y) {
  const index = (y * imageData.width + x) * 4;
  const data = imageData.data;
  return [data[index], data[index + 1], data[index + 2], data[index + 3]];
}

function setPixelColor(imageData, x, y, color) {
  const index = (y * imageData.width + x) * 4;
  const data = imageData.data;
  data[index] = color[0];     // R
  data[index + 1] = color[1]; // G
  data[index + 2] = color[2]; // B
  data[index + 3] = 255;      // A
}

function colorsMatch(color1, color2) {
  return color1[0] === color2[0] &&
         color1[1] === color2[1] &&
         color1[2] === color2[2] &&
         color1[3] === color2[3];
}

function floodFill(imageData, x, y, targetColor, fillColor) {
  const stack = [[x, y]];

  while (stack.length > 0) {
    const [currentX, currentY] = stack.pop();
    const currentColor = getPixelColor(imageData, currentX, currentY);

    if (colorsMatch(currentColor, targetColor)) {
      setPixelColor(imageData, currentX, currentY, fillColor);

      // Add neighboring pixels
      if (currentX > 0) stack.push([currentX - 1, currentY]); // Left
      if (currentX < imageData.width - 1) stack.push([currentX + 1, currentY]); // Right
      if (currentY > 0) stack.push([currentX, currentY - 1]); // Top
      if (currentY < imageData.height - 1) stack.push([currentX, currentY + 1]); // Bottom
    }
  }
}

function hexToRgb(hex) {
  const bigint = parseInt(hex.slice(1), 16);
  return [(bigint >> 16) & 255, (bigint >> 8) & 255, bigint & 255];
}

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
