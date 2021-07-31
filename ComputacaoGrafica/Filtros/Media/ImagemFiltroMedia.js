var fileLoader = document.getElementById('fileLoader');
var image = document.getElementById('image');
var canvas = document.getElementById('image-canvas');
var context;

let loadFromFile = function(){
    fileLoader.click();
    fileLoader.addEventListener('input', ()=>{
        image.src = fileLoader.files[0].name;
    });
}

let load = function (){
    
    context = canvas.getContext('2d');
    canvas.width = image.width;
    canvas.height = image.height;
    context.drawImage(image, 0, 0);

}


let rotacionar180 = function(){
    let imageData = context.getImageData(0,0,  canvas.width, canvas.height);
    let imageData2 = context.getImageData(0,0, canvas.width, canvas.height);
    let copia = new MatrixImage(imageData2);
    let img = new MatrixImage(imageData);
    for (var i = 0; i<img.width; i++){
        for (var j = 0; j<img.height; j++){
            pixel = img.getPixel(i,j);
            copia.setPixel(copia.width-i,copia.height-j, new RGBColor(pixel.red,pixel.green, pixel.blue));
        }
    }
    context.putImageData(copia.imageData,0,0)
    

}


let rotacionar90 = function(){
    var altura = canvas.height;
    var largura = canvas.width;
    let imageData = context.getImageData(0,0, altura, largura);
    let imageData2 = context.getImageData(0,0, largura, altura);
    context.clearRect(0,0,canvas.width,canvas.height);
    let img = new MatrixImage(imageData);
    canvas.height = largura;
    canvas.width = altura;
    let copia = new MatrixImage(imageData2);
    for (var i = 0; i<canvas.width; i++){
        for (var j = 0; j<canvas.height; j++){
            pixel = img.getPixel(i,j);
            copia.setPixel(copia.height - j,i, new RGBColor(pixel.red,pixel.green, pixel.blue));
        }
    }  context.putImageData(copia.imageData,00,00)

}

    
   
    


let rotacionar270 = function(){
    var altura = canvas.height;
    var largura = canvas.width;
    let imageData = context.getImageData(0,0, altura, largura);
    let imageData2 = context.getImageData(0,0, largura, altura);
    context.clearRect(0,0, canvas.width, canvas.height)
    context.save();
    context.drawImage(image,largura,altura);
    let img = new MatrixImage(imageData);
    canvas.height = largura;
    canvas.width = altura;
    let copia = new MatrixImage(imageData2);
    console.log("Copia (larg, alt) =" ,copia.width, copia.height)
    console.log("Original =", img.width, img.height)
    for (var i = 0; i<img.width; i++){
        for (var j = 0; j<img.height; j++){
            pixel = img.getPixel(i,j);
            copia.setPixel(j,copia.height - i, new RGBColor(pixel.red,pixel.green, pixel.blue));
        }
    }  
    context.putImageData(copia.imageData,0,0)

}


let threshold = function(){

    let imageData = context.getImageData(0,0, canvas.width, canvas.height);
    let img = new MatrixImage(imageData);
    grayScale();
    let imageData2 = context.getImageData(0,0, canvas.width, canvas.height)
    let copia = new MatrixImage(imageData2)
    for (var i = 0; i<copia.width; i++){
        for (var j = 0; j<copia.height; j++){
            pixel = copia.getPixel(i,j);
            var valor = Math.log(pixel.blue)
            if (valor >=4.5){
                copia.setPixel(i,j, new RGBColor(255,255,255));
            }
            else{
                copia.setPixel(i,j, new RGBColor(0,0,0));
            }
        }
    }  
    context.putImageData(copia.imageData,0,0)


}

let espelhar = function(){

    let imageData = context.getImageData(0,0,  canvas.width, canvas.height);
    let imageData2 = context.getImageData(0,0, canvas.width, canvas.height);
    let copia = new MatrixImage(imageData2);
    let img = new MatrixImage(imageData);
    for (var i = 0; i<copia.width; i++){
        for (var j = 0; j<copia.height; j++){
            pixel = img.getPixel(i,j);
            //console.log ("Altura e Largura =", canvas.width, canvas.height," Valor i e j =",i, j)
            //console.log("Largura =",img.width-i," Altura =" ,img.height-j)
            copia.setPixel(img.width - i,j, new RGBColor(pixel.red,pixel.green, pixel.blue));
        }
    }

    context.putImageData(copia.imageData,0,0)


}


let grayScale = function() {
    let imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    let img = new MatrixImage(imageData);
    for (var i = 0; i < img.width; i++) {
        for (var j = 0; j < img.height; j++) {
            var pixel = img.getPixel(i,j);
            var gray = (pixel.red + pixel.green + pixel.blue) / 3; 
            img.setPixel( i, j, new RGBColor(gray, gray, gray));
        }
    }
    context.putImageData(img.imageData, 0,0);
}

let grayScaleNTSC = function() {
    let imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    let img = new MatrixImage(imageData);
    for (var i = 0; i < img.width; i++) {
        for (var j = 0; j < img.height; j++) {
            var pixel = img.getPixel(i,j); 
            luma = pixel.red*0.299 + pixel.green*0.587 + pixel.blue*0.114;
            img.setPixel( i, j, new RGBColor(luma,luma,luma));
        }
    }
    context.putImageData(img.imageData, 0,0);
}


let zoom2 = function(){

    let imageData = context.getImageData(0,0,  canvas.width, canvas.height);
    let imageData2 = context.getImageData(0,0, canvas.width, canvas.height);
    let img = new MatrixImage(imageData);
    let copia = new MatrixImage(imageData2);
    canvas.width = canvas.width;
    canvas.height = canvas.height;

    for (var i = 0; i<img.width; i++){
        for (var j = 0; j<img.height; j++){
                pixel = img.getPixel(i,j);
                for (var k = 0; k<2; k++){
                    for (var l = 0; l<2; l++){
                copia.setPixel(i*2+k,j+l, new RGBColor(pixel.red,pixel.green, pixel.blue));
                 }
                }
            }
    }
    canvas.width = canvas.width*2;
    context.putImageData(copia.imageData,0,0)


}

let lesszoom2 = function(){

    let imageData = context.getImageData(0,0,  canvas.width, canvas.height);
    let imageData2 = context.getImageData(0,0, canvas.width/2, canvas.height/2);
    let img = new MatrixImage(imageData);
    let copia = new MatrixImage(imageData2);
    canvas.width = canvas.width/2;
    canvas.height = canvas.height/2;

    for (var i = 0; i<img.width; i++){
        for (var j = 0; j<img.height; j++){
            if (i%2==0 & j%2 == 0){    
                pixel = img.getPixel(i,j);
                copia.setPixel(i/2,j/2,new RGBColor (pixel.red,pixel.green, pixel.blue))        
            }
            
        }
    }
    context.putImageData(copia.imageData,0,0)


}

let lesszoom4 = function(){

    let imageData = context.getImageData(0,0,  canvas.width, canvas.height);
    let imageData2 = context.getImageData(0,0, canvas.width/4, canvas.height/4);
    let img = new MatrixImage(imageData);
    let copia = new MatrixImage(imageData2);
    canvas.width = canvas.width/4;
    canvas.height = canvas.height/4;

    for (var i = 0; i<img.width; i++){
        for (var j = 0; j<img.height; j++){
            if (i%4==0 & j%4 == 0){    
                pixel = img.getPixel(i,j);
                copia.setPixel(i/4,j/4,new RGBColor (pixel.red,pixel.green, pixel.blue))        
            }
            
        }
    }
    context.putImageData(copia.imageData,0,0)


}

let zoom4 = function(){

    let imageData = context.getImageData(0,0,  canvas.width, canvas.height);
    let imageData2 = context.getImageData(0,0, canvas.width*2, canvas.height*2);
    let img = new MatrixImage(imageData);
    let copia = new MatrixImage(imageData2);
    canvas.width = 4*canvas.width;
    canvas.height = 4*canvas.height;
    for (var i = 0; i<img.width; i++){
        for (var j = 0; j<img.height; j++){
                pixel = img.getPixel(i,j);

                for (var k = 0; k<4; k++){
                    for (var l = 0; l<4; l++){
                //console.log ("Altura e Largura =", canvas.width, canvas.height," Valor i e j =",i, j)
                //console.log("Largura =",img.width-i," Altura =" ,img.height-j)
                copia.setPixel(i*4+k,j+l, new RGBColor(pixel.red,pixel.green, pixel.blue));
                 }
                }
             }
    }

    context.putImageData(copia.imageData,0,0)


}

let median = function() {
    let imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    let imageData2 = context.getImageData(0, 0, canvas.width, canvas.height);

    let img = new MatrixImage(imageData);
    let copia = new MatrixImage(imageData2) ;
    for (var i = 0; i < img.width; i++) {
        for (var j = 0; j < img.height; j++) {

            var pixel = img.getPixel(i,j);
            var pixelHsl;
            var arrayPixel = Array();

            for (var k = -1; k<2; k++){
                for (var l = -1; l<2; l++){
            //console.log ("Altura e Largura =", canvas.width, canvas.height," Valor i e j =",i, j)
            //console.log("Largura =",img.width-i," Altura =" ,img.height-j)
                pixel = img.getPixel(i+k,j+l);                   
                pixelHsl = img.rgbToHsl(pixel.red,pixel.green,pixel.blue);
                arrayPixel.push(pixelHsl); 
                }
            }          
            arrayPixel.sort()
           
            rgbFinal = img.hslToRgb(arrayPixel[4][0],arrayPixel[4][1], arrayPixel[4][2])
            copia.setPixel(i,j ,new RGBColor(rgbFinal[0], rgbFinal[1], rgbFinal[2]));
        
        }
    }
    context.putImageData(copia.imageData, 0, 0);
}


let gaussianblur = function() {//limpar depois
    let imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    let img = new MatrixImage(imageData);
    for (var i = 0; i < img.width; i++) {
        for (var j = 0; j < img.height; j++) {
            var pixel = img.getPixel(i,j);
            var pixel_sort_g = Array();
            var pixel_sort_r = Array();
            var pixel_sort_b = Array();


             
            for (var k = -1; k<2; k++){
                for (var l = -1; l<2; l++){
                    if((k==-1 && l==-1)||(k==1 && l==-1)||(k==1 && l==-1)||(k==1 && l==-1)){
                        pixel = img.getPixel(i+k,j+l);
                        pixel_sort_r.push(pixel.red);
                        pixel_sort_g.push(pixel.green);
                        pixel_sort_b.push(pixel.blue);
                    }                    
                        
                    else if(k==0 && l == 0) {
                        pixel = img.getPixel(i+k,j+l);                   
                        pixel_sort_r.push(pixel.red*4);
                        pixel_sort_g.push(pixel.green*4);
                        pixel_sort_b.push(pixel.blue*4);                    
                    }
                    else{
                        pixel = img.getPixel(i+k,j+l);                   
                        pixel_sort_r.push(pixel.red*2);
                        pixel_sort_g.push(pixel.green*2);
                        pixel_sort_b.push(pixel.blue*2); 
                        
                }
            }
        }    
  
            var media_r = media_b = media_g = 0;
            for(x = 0; x<9;x++){
                media_r += pixel_sort_r[x]
                media_b += pixel_sort_b[x]
                media_g += pixel_sort_g[x]
            }
            img.setPixel(i, j, new RGBColor((media_r/16),(media_g/16),(media_b/16)));
        }
    }
    context.putImageData(img.imageData, 0, 0);
    
}





 
let mean = function() {//limpar depois
    let imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    let img = new MatrixImage(imageData);
    for (var i = 0; i < img.width; i++) {
        for (var j = 0; j < img.height; j++) {
            var pixel = img.getPixel(i,j);
            var pixel_sort_g = Array();
            var pixel_sort_r = Array();
            var pixel_sort_b = Array();



            for (var k = -1; k<2; k++){
                for (var l = -1; l<2; l++){
                pixel = img.getPixel(i+k,j+l);   
                pixel_sort_r.push(pixel.red);
                pixel_sort_g.push(pixel.green);
                pixel_sort_b.push(pixel.blue);                
                }
            }      
  
            var media_r = media_b = media_g = 0;
            for(x = 0; x<9;x++){
                media_r += pixel_sort_r[x]
                media_b += pixel_sort_b[x]
                media_g += pixel_sort_g[x]
            }
            img.setPixel(i, j, new RGBColor(media_r/9,media_g/9,media_b/9));
        }
    }
    context.putImageData(img.imageData, 0, 0);
}





class RGBColor {
    constructor(r, g, b) {
      this.red = r;
      this.green = g; 
      this.blue = b;
    }
}

class MatrixImage {
    constructor(imageData) {
      this.imageData = imageData;
      this.height = imageData.height; 
      this.width = imageData.width;
    }

    getPixel(x, y) {
        let position = ((y * (this.width * 4)) + (x * 4));

        return new RGBColor(
             this.imageData.data[position],   //red
             this.imageData.data[position+1], //green
             this.imageData.data[position+2], //blue
        );
    }
    getPixelR(x, y) {
        let position = ((y * (this.width * 4)) + (x * 4));

        return this.imageData.data[position]   //red
             
    }
    getPixelG(x, y) {
        let position = ((y * (this.width * 4)) + (x * 4));

        return this.imageData.data[position+1]   //red
             
    }
    getPixelB(x, y) {
        let position = ((y * (this.width * 4)) + (x * 4));

        return  this.imageData.data[position+2]   //red
             
    }
    


    setPixel(x, y, color) {
        let position = ((y * (this.width * 4)) + (x * 4));
        this.imageData.data[position] = color.red;
        this.imageData.data[position+1] = color.green;
        this.imageData.data[position+2] = color.blue;
    }
    
    rgbToHsl (r, g, b){
        r /= 255, g /= 255, b /= 255;
        var max = Math.max(r, g, b), min = Math.min(r, g, b);
        var h, s, l = (max + min) / 2;
    
        if(max == min){
            h = s = 0; // achromatic
        }else{
            var d = max - min;
            s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
            switch(max){
                case r: h = (g - b) / d + (g < b ? 6 : 0); break;
                case g: h = (b - r) / d + 2; break;
                case b: h = (r - g) / d + 4; break;
            }
            h /= 6;
        }
        return [h, s, l];
    }
    hslToRgb(h, s, l){
        var r, g, b;
    
        if(s == 0){
            r = g = b = l; // achromatic
        }else{
            var hue2rgb = function hue2rgb(p, q, t){
                if(t < 0) t += 1;
                if(t > 1) t -= 1;
                if(t < 1/6) return p + (q - p) * 6 * t;
                if(t < 1/2) return q;
                if(t < 2/3) return p + (q - p) * (2/3 - t) * 6;
                return p;
            }
    
            var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
            var p = 2 * l - q;
            r = hue2rgb(p, q, h + 1/3);
            g = hue2rgb(p, q, h);
            b = hue2rgb(p, q, h - 1/3);
        }
    
        return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
    }

    


}

document.getElementById('btnLoad').addEventListener('click', load);
document.getElementById('btnGray').addEventListener('click', grayScale);
document.getElementById('btnGrayNTSC').addEventListener('click', grayScaleNTSC);
document.getElementById('btnRotacionar180').addEventListener('click', rotacionar180);
document.getElementById('btnMedian').addEventListener('click', median);
document.getElementById('btnMean').addEventListener('click', mean);
document.getElementById('btnThreshold').addEventListener('click', threshold);
document.getElementById('btnRotacionar90').addEventListener('click', rotacionar90);
document.getElementById('btnRotacionar270').addEventListener('click', rotacionar270);
document.getElementById('btnZoom2').addEventListener('click', zoom2);
document.getElementById('btnLessZoom2').addEventListener('click', lesszoom2);
document.getElementById('btnLessZoom4').addEventListener('click', lesszoom4);
document.getElementById('btnZoom4').addEventListener('click', zoom4);
document.getElementById('btngBlur').addEventListener('click', gaussianblur);
document.getElementById('btnMirror').addEventListener('click', espelhar);