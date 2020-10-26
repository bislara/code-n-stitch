const card = document.querySelector('.card');
const container = document.querySelector('.container');
const title = document.querySelector('.title');
const sneaker = document.querySelector('.sneaker img');
const purchase = document.querySelector('.purchase button');
const desc = document.querySelector('.info h3');
const sizes = document.querySelector('.sizes');


container.addEventListener('mousemove', (e) => {
    let xAxis = (window.innerWidth / 2 - e.pageX) / 20;
    let yAxis = (window.innerHeight / 2 - e.pageY) / 20;
    card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
})


//animate in
container.addEventListener('mouseenter', e=> {
    card.style.transition = 'none';
    title.style.transform = 'translateZ(150px)'
    sneaker.style.transform = 'translateZ(250px) rotateZ(-45deg)'
    desc.style.transform = 'translateZ(125px)'
    sizes.style.transform = 'translateZ(100px)'
    purchase.style.transform = 'translateZ(75px)'
})


//animate out
container.addEventListener('mouseleave', e => {
    card.style.transition = 'all 0.5s ease';
    card.style.transform = `rotateY(0deg) rotateX(0deg)`
    title.style.transform = 'translateZ(0px)'
    sneaker.style.transform = 'translateZ(0px) rotateZ(0deg)'
    desc.style.transform = 'translateZ(0px)'
    sizes.style.transform = 'translateZ(0px)'
    purchase.style.transform = 'translateZ(0px)'
})
