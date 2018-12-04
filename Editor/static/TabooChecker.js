function taboo(e){
        var key = window.event.keyCode;
        if (key === 32 || key === 13){


           $.get("/taboo", function(data){
            var text = $.parseJSON(data);
            var regex = new RegExp(text.join("|"),"g")
            var textfield = document.getElementById(e);

              if(textfield.value.search(regex) > -1) {
                    alert("Taboo word found! Replaced by UNK")
                    textfield.value = textfield.value.replace(regex, "UNK");
                    $.post( "/postmethod", {
                        javascript_data: textfield.value
                        });
                    }


          });


      }
}
