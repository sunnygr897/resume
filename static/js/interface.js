
function showcpp() {

    document.getElementById("cpp").innerHTML = ""; //clear previous results

   
    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari

        xmlhttp = new XMLHttpRequest();

    } else {// code for IE6, IE5

        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");

    }

    xmlhttp.onreadystatechange = function () {

        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            document.getElementById("cpp").innerHTML = xmlhttp.responseText;
            document.getElementById("cpparia").ariaValueNow = xmlhttp.responseText;
        }

    }

    xmlhttp.open("GET", "./php/skills.php?name=cpp", true);

    xmlhttp.send();

    return;
}
function showhtml() {

    document.getElementById("html").innerHTML = ""; //clear previous results


    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari

        xmlhttp = new XMLHttpRequest();

    } else {// code for IE6, IE5

        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");

    }

    xmlhttp.onreadystatechange = function () {

        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            document.getElementById("html").innerHTML = xmlhttp.responseText;
            document.getElementById("htmlaria").ariaValueNow = xmlhttp.responseText;
        }

    }

    xmlhttp.open("GET", "./php/skills.php?name=html", true);

    xmlhttp.send();

    return;

} function showjava() {
    document.getElementById("java").innerHTML = ""; //clear previous results


    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari

        xmlhttp = new XMLHttpRequest();

    } else {// code for IE6, IE5

        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");

    }

    xmlhttp.onreadystatechange = function () {

        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            document.getElementById("java").innerHTML = xmlhttp.responseText;
            document.getElementById("javaaria").ariaValueNow = xmlhttp.responseText;
        }

    }

    xmlhttp.open("GET", "./php/skills.php?name=java", true);

    xmlhttp.send();

    return;
} function showphp() {
    document.getElementById("php").innerHTML = ""; //clear previous results

    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari

        xmlhttp = new XMLHttpRequest();

    } else {// code for IE6, IE5

        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");

    }

    xmlhttp.onreadystatechange = function () {

        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            document.getElementById("php").innerHTML = xmlhttp.responseText;
            document.getElementById("phparia").ariaValueNow = xmlhttp.responseText;
        }

    }

    xmlhttp.open("GET", "./php/skills.php?name=php", true);

    xmlhttp.send();

    return;

} function showpython() {
    document.getElementById("python").innerHTML = ""; //clear previous results


    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari

        xmlhttp = new XMLHttpRequest();

    } else {// code for IE6, IE5

        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");

    }

    xmlhttp.onreadystatechange = function () {

        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            document.getElementById("python").innerHTML = xmlhttp.responseText;
            document.getElementById("pythonaria").ariaValueNow = xmlhttp.responseText;
        }

    }

    xmlhttp.open("GET", "./php/skills.php?name=python", true);

    xmlhttp.send();

    return;
} function showandroid() {

    document.getElementById("android").innerHTML = ""; //clear previous results


    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari

        xmlhttp = new XMLHttpRequest();

    } else {// code for IE6, IE5

        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");

    }

    xmlhttp.onreadystatechange = function () {

        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            document.getElementById("android").innerHTML = xmlhttp.responseText;
            document.getElementById("androidaria").ariaValueNow = xmlhttp.responseText;
        }

    }

    xmlhttp.open("GET", "./php/skills.php?name=android", true);

    xmlhttp.send();

    return;
}
function loadvalues() {
    showcpp();
    showhtml();
    showjava();
    showphp();
    showpython();
    showandroid();

}