const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

ctx.beginPath();
ctx.moveTo(60,20);


ctx.fillStyle = 'blue';
ctx.fillRect(50,20,10,10);
ctx.fillStyle = 'green';
ctx.fillRect(50,100,10,10);
ctx.fillStyle = 'red';
ctx.fillRect(250,20,10,10);
ctx.fillStyle = 'yellow';
ctx.fillRect(250,100,10,10);


ctx.quadraticCurveTo(230,30,60,100)
ctx.quadraticCurveTo(230,30,260,100);
ctx.quadraticCurveTo(260,40,60,20);
ctx.quadraticCurveTo(60,110,260,20);
ctx.quadraticCurveTo(260,110,260,110);



ctx.stroke();




