
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

function toggle(id, theme) {
    // DEFINING VARS
    // element will be button
    var element = document.getElementById(id)
    // this is the container
    var container = document.getElementById("cont")
    // body
    var body = document.body;

    // ninties requires a different theme
    if (theme == 'ninties') {
        theme_bg = 'ninties_bg'
    } else {
        theme_bg = theme
    }

    // other classes and toggles 
    const classes = ['darkmode', 'ninties'];
    const result = classes.filter(f => f != theme);

    // if the button is active, switch it off
    if (element.classList.contains('active')) {
        // take out all the body themes
        body.className = '';
        body.classList.add('oranges');
        // take out the container theme
        container.classList.remove(theme)

        // otherwise turn it on
    } else {
        // turn off other toggles
        // for each toggle id in result, remove the active class and the aria-pressed
        var i;
        for (i = 0; i < result.length; i++) {
            document.getElementById(result[i]).classList.remove("active")
            document.getElementById(result[i]).setAttribute("aria-pressed", "false");
        }

        // remove other classes
        body.className = '';
        container.classList.remove(...result) // "..." allows us to remove an array

        // add class
        body.classList.add(theme_bg);
        container.classList.add(theme)
    }
}