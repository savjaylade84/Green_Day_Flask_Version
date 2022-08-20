
const nav_click_animation = () => {

    let nav_buttons = document.querySelectorAll('.nav-button');

        nav_buttons.forEach(nav_button => {

        nav_button.children[0].addEventListener('mouseenter',()=>{
    
                nav_button.style.backgroundColor = 'rgb(141, 15, 15)';
        });

        nav_button.children[0].addEventListener('mouseleave',()=>{
    
            nav_button.style.backgroundColor = 'rgb(34, 102, 43)';
        });


    })

};

const nav_mobile_animation = () => {

    let nav_menu = document.querySelector('.nav-menu');
    let dots = document.querySelector('.dots');


    dots.addEventListener('click',()=>{
        console.log('click nav')
        if(nav_menu.style.transform == 'translateX(100%)'){
            nav_menu.style.transform = 'translateX(0)';
        }
        else
            nav_menu.style.transform = 'translateX(100%)';
        

    });
    
    dots.addEventListener('mouseenter',()=>{
        if(nav_menu.style.transform == 'translateX(100%)'){
            nav_menu.style.transform = 'translateX(0)';
        }
        else
            nav_menu.style.transform = 'translateX(100%)';
        

    });

};


nav_mobile_animation()
nav_click_animation()