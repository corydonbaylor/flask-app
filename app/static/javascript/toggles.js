function darkmode() {

    // remove coloring from background
    var body = document.body;
    var element = document.getElementById('cont')

    if (document.getElementById('darkmode').classList.contains('active')) {
        body.className = '';
        body.classList.add('oranges');

        element.classList.remove('darkmode');

    } else {

        // turning off other toggles
        // https://stackoverflow.com/questions/14408891/getelementbyid-multiple-ids for doing this in a for loop
        document.getElementById("ninties").setAttribute("aria-pressed", "false");
        document.getElementById("ninties").classList.remove("active")
        element.classList.remove('ninties');

        // removing all other classes and adding darkmode to body
        body.className = '';
        body.classList.add('darkmode');

        // adding darkmode to cont
        element.classList.add('darkmode');

    }
}

function ninties() {

    // remove coloring from background
    var body = document.body;
    var element = document.getElementById('cont')

    if (document.getElementById('ninties').classList.contains('active')) {
        body.className = '';
        body.classList.add('oranges');

        element.classList.remove('ninties');

    } else {

        // turning off other toggles
        // https://stackoverflow.com/questions/14408891/getelementbyid-multiple-ids for doing this in a for loop
        document.getElementById("darkmode").setAttribute("aria-pressed", "false");
        document.getElementById("darkmode").classList.remove("active")

        // removing all other classes and adding darkmode to body
        body.className = '';
        body.classList.add('ninties_bg');

        // adding darkmode to cont
        element.classList.add('ninties');

    }
}