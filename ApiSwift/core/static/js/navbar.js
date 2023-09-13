const menu = document.getElementById('menu');
const closeMenu = document.getElementById('close_menu');
const navbar = document.querySelector('.navbar');

menu.addEventListener('click',() =>{
    navbar.style.display = 'block';
    closeMenu.style.display = 'block';
    menu.style.display = 'none';
})

closeMenu.addEventListener('click',() =>{
    navbar.style.display = 'none';
    closeMenu.style.display = 'none';
    menu.style.display = 'block';
})