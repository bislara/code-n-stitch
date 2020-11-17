// Taken from https://stackoverflow.com/a/57804949

var r_text = new Array();
r_text = [{
    msg: "I was just thinking about you!",
    link: "http://www.google.com"
  },
  {
    msg: "You are a great example for others.",
    link: "http://www.mylink.com"
  },
  {
    msg: "You have great ideas.",
    link: "http://www.yourlink.com"
  }, {
    msg: "When I grow up I want to be you!",
    link: "http://www.test.com"
  }, {
    msg: "I appreciate all of your opinions.",
    link: "http://www.facebook.com"
  }
];

var i = Math.floor(r_text.length * Math.random());

document.write(`<br /><br /><br /><br /><br /><br /><br /><center><FONT SIZE=72><FONT COLOR='#FFFFFF'><a href='${r_text[i].link}'>${r_text[i].msg}</a></FONT></center><br />`);

var bgcolorlist = new Array("#228B22", "#FFD700", "#ADFF2F", "#FF69B4", "#CD5C5C", "#4B0082", "#7CFC00", "#ADD8E6", "#E84643", "#ED0A07", "#EA2907", "#E5294B", "#E00D26", "#FF3030", "#FC7500", "#F95700", "#F43900", "#F95620")

document.body.style.background = bgcolorlist[Math.floor(Math.random() * bgcolorlist.length)];