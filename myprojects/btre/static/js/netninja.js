let colourChanger = document.querySelector('header');
let colours = [];
let image = document.querySelectorAll('img');
let counter = 0;

function changeColor(){

    if (counter >= colours.length){
        counter = 0;
    }
    colourChanger.style.backgroundImage =colours[counter];
    counter++;
}

setInterval(changeColor,3000);