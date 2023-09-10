const botForm = document.querySelector('.form_bot');
const closeBot = document.querySelector('.closeBot');
const newBot = document.querySelector('.new_bot');

newBot.addEventListener('click',() =>{
    botForm.style.display = 'block';
})
closeBot.addEventListener('click',() =>{
    botForm.style.display = 'none';
})