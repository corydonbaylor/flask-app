function change(id) {

    var x = document.getElementsByClassName("skill-icons");
    var i;
    for (i = 0; i < x.length; i++) {
        x[i].classList.remove("icons-active")
    }

    switch (id) {
        case 'r':
            text = '<p>I have been using R nearly every day for the past four years. I prefer tidyverse for data manipulation, ggplot2 for <a href="/viz">visualizations</a>, shiny for interactivity, and rmarkdown for report automations. I am confident that I can complete nearly any data related task thrown my way in R.</p>'
            break;
        case 'python':
            text = '<p>I am newer to python. However, the backend of this website is built in <a href="/webdev/hello_flask">flask</a>, and I have some experience with numpy, pandas, dash, and plotly.</p>'
            break;
        case 'js':
            text = '<p>I am not a web developer but feel comfortable enough reading and writing javascript to add finishing touches (like this skill section) using javascript.</p>'
            break;
        case 'html':
            text = '<p>Besides building this website, I have used HTML and CSS extensively while working on complex shiny applications and <a href= "static/analytics/xaringan/template.html#1">xarigan</a> presentations.</p>'
            break;
        case 'css':
            text = '<p>Most of the styling for my personal website is made using custom CSS. Through this, I have become comfortable with media queries and responsive webdesign.</p>'
            break;
        case 'svelte':
            text = '<p>Svelte is my favorite frontend framework to use when building a website. I built <a href="http://svelte-recipes.herokuapp.com/">a receipe website</a> using it.'
            break;
        case 'boot':
            text = '<p>The underlying CSS bones of this website are built using bootstrap. Check out my <a href="/webdev/bootstrap">tutorial on bootstrap</a> in the webdev section of this site.</p>'
            break;
        case 'sql':
            text = '<p>For a little over a year, I served as a deputy manager overseeing a data reporting unit where the day to day work consisted of writing queries. My current project involves injecting SQL code into r markdown to make fully automated reports! As an aside, I write my SQL code in lower case because I do not like my code yelling at me.</p>'
            break;
        case 'git':
            text = '<p>I use git to manage version control both for personal projects, where it is just me working, and at work, where the team can consist of a dozen different people. I currently maintain a package for an R API wrapper for wikipedia called <a href="/analytics/getwiki">getwiki</a> that can be found on my github.</p>'
            break;
        default:
            text = 'test of skills'
    }
    document.getElementById("skill-content").innerHTML = text

    var element = document.getElementById(id);
    element.classList.add("icons-active");
}