//start of webpage make the selection map appear
function generateMap(){
    const canvas = document.getElementById("canvas")
    const ctx = canvas.getContext("2d")

    for(r = 0; r < 50; r++){
        ctx.moveTo(r*20, 0);
        ctx.lineTo(r*20, 500);
        ctx.stroke();
    }
    
    for(c = 0; c < 50; c++){
        ctx.moveTo(0, c*20);
        ctx.lineTo(500, c*20);
        ctx.stroke();
    }

    canvas.style.display = "none"
    document.getElementById("warning").style.display="block"
    document.getElementById("roverInfo").style.display="none"
}

function makeIcons(rdBttn){
   const canvas = document.getElementById("canvas")
   canvas.style.display = "block"
   document.getElementById("roverInfo").style.display="block"
   document.getElementById("warning").style.display="none"

    var radio = rdBttn.id

    if(radio === "roverSelection1"){
        //document.getElementById("test").innerHTML = "yes"
    } else if(radio === "roverSelection2"){
        //document.getElementById("test").innerHTML = "maybe"
    } 
    else{
        //document.getElementById("test").innerHTML = "no"
    }
}

function makePersonalIcons(rdBttn){
    const canvas = document.getElementById("canvas")
   canvas.style.display = "block"
   document.getElementById("warning").style.display="none"

   setTimeout(() => {personalError();}, 2000);
}

function personalError(){
    document.getElementById("sysWarn").style.display = "block"
    document.getElementById("canvas").style.display = "none"
}

var i = 0;
function move() {
    document.getElementById("position").style.display="none"
    document.getElementById("myProgress").style.display="block"
    if (i == 0) {
        i = 1;
        var elem = document.getElementById("myBar");
        var width = 10;
        var id = setInterval(frame, 20);
        function frame() {
          if (width >= 100) {
            clearInterval(id);
            i = 0;
            loadRoute()
          } else {
            width++;
            elem.style.width = width + "%";
            elem.innerHTML = width + "%";
          }
        }
      }
}

function makeCords(){
    document.getElementById("position").style.display="block"
    document.getElementById("myProgress").style.display="none"
    document.getElementById("currentRoute").style.display="none"
}

function loadRoute(){
    document.getElementById("myProgress").style.display="none"
    document.getElementById("currentRoute").style.display="block"
}