
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
    const classes = ['darkmode', 'ninties', 'test'];
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

function toggle_content(id) {
    // the toggle you clicked
    var element = document.getElementById(id)
    // the div for inner html 
    var content = document.getElementById('toggle_content')

    var default_content = `<p>
                                Darkmode is pretty trendy in UI/UX right now&mdash;and for good reason! I oftentimes am working on this
                                website into the wee hours of the morning, and while I love my bright colors, it can feel like staring into
                                the sun when the lights are off.
                            </p>
                            <p>
                                So I guess this one page will be a refugee for my eyes at night.
                            </p>
                            <p>
                                It got me thinking, "what other toggles would be useful for a website?"
                            </p>
                            `
    switch (id) {
        case 'ninties':
            text = `
                    <div class = 'row'>
                        <div class = 'col'>
                            <p> welcome to the ninties. <p>
                        </div>
                        <div class = 'col'>
                            <img src = "{{url_for('static', filename='images/webdev/toggle/dancing_baby.gif')}}">
                        </div>
                    </div>
                    `
            break;
        case 'darkmode':
            text = '<p>darkmode on</p>'
            break;
        case 'test':
            text = '<p>I am not a web developer but feel comfortable enough reading and writing javascript to add finishing touches (like this skill section) using javascript.</p>'
            break;
        default:
            text = default_content
    }

    if (element.classList.contains('active')) {
        // replace content with default content if not active
        content.innerHTML = default_content
    } else {
        content.innerHTML = text
    }
}