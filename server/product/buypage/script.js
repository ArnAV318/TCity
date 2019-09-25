
function trial(){
  x=screen.width;
  x=x*60/100;
  var els=document.getElementsByClassName("modal-content");
    [...els].forEach((element, index, array) => {
      element.style.width= String(x)+"px";
  });
  var rels=document.getElementsByClassName("modal-dialogue");
    [...els].forEach((element, index, array) => {
      element.style.right= "33.3%";
  });
}
trial();


$('#bologna-list row a').on('click', function (e) {
  e.preventDefault()
  $(this).tab('show')
})