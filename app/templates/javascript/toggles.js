
function toggle(id, theme) {
    // DEFINING VARS
    // element will be button
    var element = document.getElementById(id)
    // this is the container
    var container = document.getElementById("cont")
    // this is the navbar
    var navbar = document.getElementById("navbar")
    // body
    var body = document.body;

    // ninties and gary requires a different theme
    switch (theme) {
        case 'ninties':
            theme_bg = 'ninties_bg'
            break;
        case 'gary':
            theme_bg = 'gary_bg'
            break;
        default:
            theme_bg = theme
    }
    // other classes and toggles 
    const classes = ['darkmode', 'ninties', 'hacker', 'gary'];
    const result = classes.filter(f => f != theme);

    // if the button is active, switch it off
    if (element.classList.contains('active')) {
        // take out all the body themes
        body.className = '';
        body.classList.add('greys');
        // take out the container theme
        container.classList.remove(theme)
        navbar.classList.remove(theme)


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
        navbar.classList.remove(...result) // "..." allows us to remove an array

        // add class
        body.classList.add(theme_bg);
        container.classList.add(theme)
        navbar.classList.add(theme)

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
                                We've come to expect darkmode from websites. But I believe us web designers are capable of so much more!
                            </p>
                            <p>
                                So I would like to purpose a few more potential toggles that I think many will come to see as a necessity.
                            </p>
                            `
    switch (id) {
        case 'ninties':
            text = `
                    <div class = 'row'>
                        <marquee style = 'font-size:30px; color:lime; font-family:'comic sans ms'; width: 100%> welcome to the ninties!! </marquee>
                        <div class = 'col-8'>
                        <p> 
                            Now this is a front end trend I could get behind! Remember when websites had almost no CSS but definitely had a marquee scrolling somewhere? I do. 
                        </p>    
                        <p>
                            This is back in the 
                            day when all caps was an aesthetic choice, not the work of a psycho. This is back when GREEN DAY was putting out bangers, NEOPETS was 
                            <span style = 'color:red'>fire</span>, and yahoo was my homepage. 
                        </p>
                        </div>
                        <div class = 'col-4'>
                            <img src = "{{url_for('static', filename='images/coding/toggle/dancing_baby.gif')}}">
                        </div>
                    </div>
                    `
            break;
        case 'darkmode':
            text = `<p>
                        Ah the sweet release of dark mode. I could stare at this page until late into the night and early into the morning. What wonderful beauty these shades of grey
                        are. Darkmode is sunglasses for my computer. And this website has nice sunglasses, ray-bans even.
                    </p>
                    <p>
                        Are ray-bans still cool?
                    </p>
                    <p>
                        I wouldn't know. I never wear sunglasses. I feel like a poser whenever I do. Like I am trying to be cool. Well guess what, I'm just trying not to squint.
                        Not a problem here though, not with this sweet dark mode. 
                    </p>
                    `

            break;
        case 'hacker':
            text = `<p>
                        Oh wow! Are we in the matrix? Or in a Fallout 3 terminal? You know honestly, this isn't a good way to design a website. Like yes, its readable (kinda). But it clashes
                        so strongly with any modern web element. I mean just <span style='font-style:italic;'>look </span> at those toggles. I didn't know that DOS could run iOS apps.
                        Gottem.  
                    </p>
                    <p>
                        Alright, let's go ahead and switch this one off. This toggle is not a winner. 
                    </p>
            `
            break;
        case 'gary':
            text = `<p>
                        How can we intergrate Gary Busey into modern web design? 
                        
                    </p>
                    <p>    
                        I always try and stay at the forefront of web design &mdash; in that I follow what Apple is doing 
                        and then do whatever that is. And nothing says "cutting edge" like doing what hasn't been done before, and I have never seen the "Point Break" villain Gary Busey
                        as a tiled background on someone's webpage.    
                    </p>
                    <p>
                        And hey. It's a mode. It's <span style= "font-style: italic">optional</span>. I'm not forcing Gary Busey on anyone. If the user doesn't want it they can 
                        turn it off. And let's say they do want it, and we didn't have it.
                    </p>
                    <p>
                        And no. No one said they wanted this. But whats that famous Henry Ford quote, "If I asked what people wanted, I would have built a faster horse."
                    </p>
                `
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