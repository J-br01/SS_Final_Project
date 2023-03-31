var profile = []
var settings = []

function getPofileDetails(){
    var server = window.location.href;
    var http = new XMLHttpRequest();
    var txt = "", x;
    http.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            profile = JSON.parse(this.responseText);

            fillProfile();
        }
    };
    const  link = server = "+/getProfileData"
    http.open("Get", link, true);
    http.send();
}

function fillProfile(){

}