let div = document.createElement("div");

document.querySelector("nav.navbar").onclick = ()=>{
    if (window.screen.width <= 600) {
        setTimeout(() => {
            document.querySelector("a.logout").style.display = "block";
        }, 400);
    } else {
        document.querySelector("a.logout").style.display = "block";
    }
    show = document.querySelectorAll("nav.navbar > div.container > a.navigation");
    show[0].style.display = "block";
    show[1].style.display = "block";
    document.querySelector("nav.navbar > div.container > h1").style.display = "block";
    document.querySelector("nav.navbar").classList.add("navbar-clicked");
    div.className = "overlay";
    if (!(div.classList.contains("appear")))
        div.className += " appear";
    if (!(document.body.contains(div)))
        document.body.appendChild(div);
    document.querySelector("div.overlay").onclick = ()=>{
        if (window.screen.width <= 600) document.querySelector("a.logout").style.display = "none";
        setTimeout(() => {
            document.querySelector("a.logout").style.display = "none";
            document.querySelector("nav.navbar > div.container > h1").style.display = window.screen.width > 600 ? "none" : "block";
            show = document.querySelectorAll("nav.navbar > div.container > a.navigation");
            show[0].style.display = "none";
            show[1].style.display = "none";
        }, 400);
        document.querySelector("nav.navbar").classList.remove("navbar-clicked");
        document.querySelector("div.overlay").classList.add("disappear");
        setTimeout(() => {
            document.querySelector("div.overlay").remove();
        }, 410);
    }
}

for (const content of document.querySelectorAll("section#tabungan div.container a div.content")) {
    content.onmouseover = () => {
        if(content.firstElementChild.classList.contains("withdrawal")) {
            content.firstElementChild.style.display = "block";
            content.firstElementChild.classList.remove("disappear");
            content.firstElementChild.classList.add("appear");
        }
    }
    content.onmouseout = () => {
        if(content.firstElementChild.classList.contains("withdrawal")) {
            content.firstElementChild.classList.remove("appear");
            content.firstElementChild.classList.add("disappear");
            content.firstElementChild.onmouseout = () => {
                setTimeout(() => {
                    content.firstElementChild.style.display = "none";
                }, 400);
            }
        }
    }
}