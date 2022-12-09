
    
function textAppear() {
    var fullWidth = window.innerWidth - 300;
    var fullHeight = window.innerHeight - 300;
    var texts = ['I just can\'t cope', 'I can\'t stop thinking about them', 
            'I want them back', 'Make the thoughts stop', 'I\'m not good enough',
            'I just want it to end', 'I\'m a bad person', 'Why am I even here?',
            'Why me?']
    const section = document.getElementById("fog")

    var elem = document.createElement("p");
    elem.setAttribute('id','text')
    elem.style.position = "absolute";
    elem.style.left = Math.round(Math.random() * fullWidth)+ "px";
    elem.style.top = Math.round(Math.random() * fullHeight )+ "px";
    elem.style.color = "#ececec";
    elem.style.zIndex = 8;
    elem.style.fontSize = Math.round(Math.random() * 3)+"rem";
    elem.style.textTransform = "lowercase";
    elem.style.letterSpacing = 1;
    elem.style.padding = "2% 2%";
    elem.style.animation = "fadein 2s ease-in both, fadeout 10s"
    var node = document.createTextNode(texts[Math.floor(Math.random()*texts.length)]);
    elem.appendChild(node);
    section.appendChild(elem);
    setTimeout(textAppear, 2000);
}

document.addEventListener('readystatechange', e => {
    if (document.readyState === "complete") {
        textAppear();
    }
})