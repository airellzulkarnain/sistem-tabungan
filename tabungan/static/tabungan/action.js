let div = document.createElement("div");

document.querySelector("nav.navbar").onclick = ()=>{
    document.querySelector("a.logout").style.display = "block";
    document.querySelector("nav.navbar > div.container > h1").style.display = "block";
    document.querySelector("nav.navbar").style.width = "300px";
    div.className = "overlay";
    if (!(div.classList.contains("appear")))
        div.className += " appear";
    if (!(document.body.contains(div)))
        document.body.appendChild(div);
    document.querySelector("div.overlay").onclick = ()=>{
        setTimeout(() => {
            document.querySelector("a.logout").style.display = "none";
            document.querySelector("nav.navbar > div.container > h1").style.display = "none";
        }, 400);
        document.querySelector("nav.navbar").style.width = "100px";
        document.querySelector("div.overlay").classList.add("disappear");
        setTimeout(() => {
            document.querySelector("div.overlay").remove();
        }, 410);
    }
}

