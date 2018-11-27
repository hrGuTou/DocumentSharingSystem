function taboo(word, e){
            var textfield = document.getElementById(e);
            var regex = new RegExp(word,"g")

           if(textfield.value.search(regex) > -1) {
		        textfield.value = textfield.value.replace(regex, "UNK");
		        alert(word)
        }

}
