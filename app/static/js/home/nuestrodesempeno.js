const menuleft = document.querySelector('.left1');
const navegacion1 = document.querySelector('.ocultar1');
const menuright = document.querySelector('.right1');
const navegacion2 = document.querySelector('.navegacion2');

document.addEventListener('DOMContentLoaded', ()=>{
    eventos1();
})

const eventos1 =() =>{
    menuleft.addEventListener('click',desplegarleft);
    menuright.addEventListener('click',desplegarright)
}
const desplegarleft =()=>{
    navegacion1.classList.remove('ocultar1');
    botonCerrar1();
}
const desplegarright =()=>{
    navegacion2.classList.remove('ocultar2');
    botonCerrar2();
}

const botonCerrar1 = () =>{
    const btnCerrar1 = document.createElement('p');
    btnCerrar1.textContent = 'x';
    btnCerrar1.classList.add('btn-cerrar1');
    navegacion1.appendChild(btnCerrar1);
    cerrarMenu1(btnCerrar1);
}
const botonCerrar2 = () =>{
    const btnCerrar2 = document.createElement('p');
    btnCerrar2.textContent = 'x';
    btnCerrar2.classList.add('btn-cerrar2');
    navegacion2.appendChild(btnCerrar2);
    cerrarMenu2(btnCerrar2);
}
const cerrarMenu1 = (boton1) =>{
    boton1.addEventListener('click', ()=>{
        navegacion1.classList.add('ocultar1');
    })
}
const cerrarMenu2 = (boton2) =>{
    boton2.addEventListener('click', ()=>{
        navegacion2.classList.add('ocultar2');
    })
}