function saveText(e){
      var textfield = document.getElementById(e).value;
      $.post( "/postmethod", {
    javascript_data: textfield
});
}

