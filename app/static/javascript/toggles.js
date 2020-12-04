function darkmode() {
    // remove coloring from background
    var body = document.body;
    var element = document.getElementById('cont')

    if (body.classList.contains('oranges')) {
        // removing all other classes and adding darkmode to body
        body.className = '';
        body.classList.add('darkmode');

        // adding darkmode to cont
        element.classList.add('darkmode');

    } else {
        body.className = '';
        body.classList.add('oranges');

        element.classList.remove('darkmode');
    }
}