
var currstate=false
function toggley() {
  if(currstate==false) {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    var els=document.getElementsByClassName("droppy");
    [...els].forEach((element, index, array) => {
      element.style.marginLeft= "20px";
  });
    currstate=true;
    document.getElementById("trial").innerHTML = "<";
  }
  else {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.getElementById("trial").innerHTML = ">";
    currstate=false;
  }
} 
console.log(document.getElementsByClassName("jumbotron"));
setInterval(function() {
  scrolleyy();
},800);
function scrolleyy() {
  if(window.scrollY>=60) {
    document.getElementById("mySidebar").style.top="0px";
    document.getElementsByClassName("openbtn")[0].style.top="0px";
    
  }
  else {
    document.getElementById("mySidebar").style.top="60px";
    document.getElementsByClassName("openbtn")[0].style.top="60px";
    
    
  }
  console.log(window.scrollY)
}