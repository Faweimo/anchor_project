let counter =1;
setInterval(function(){
    document.querySelector('#radio' + counter).checked = true;
    counter++;
    if(counter > 4){
    counter = 1;
        
    }

}, 5000)
// let staff = document.querySelector('#nav-conts #arrow');
// let drops = document.querySelector('.drops-content');

// staff.addEventListener('click',display,false);

// function display(e) {
//     e.preventDefault();
//     for ( let i = 0; i<drops.length; i++) {
//         drops[i].classList.remove('drops-display')
//     }
//     function(e){
//         if (!e.target.matches('')) {
            
//         }
//     }
// }
