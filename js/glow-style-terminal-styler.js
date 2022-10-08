// add "lonesome-link" class to untitled links
let links = document.body.getElementsByTagName("a");
for (let link of links) {
    if (link.innerText === "") {
        link.classList.add("lonesome-link");
    }
}

// auto-add anchor tag functionality
let headings = document.querySelectorAll("h1, h2, h3, h4, h5, h6");
for (let i = 0; i < headings.length; i++) {
    headings[i].id = headings[i].innerText;
    headings[i].addEventListener('click', function () {
        document.location.hash = headings[i].id;
    });
}

// dynamic shell setup [abs top left line dude]
// ex if page is: http://localhost:63342/blog/posts/unraid.html
if (window.location.pathname === "/") {
    document.getElementById('page-path').innerText = '~'
    document.getElementById('page-name').innerText = 'index.md'
} else {
    const pathname = window.location.pathname.split('/') // ex: [ "", "blog", "posts", "unraid.html" ]
    const name = pathname.pop().split('.')[0] + '.md' // "unraid.md"
    const path = pathname.join('/') // "/blog/posts"
    document.getElementById('page-path').innerText = '~' + path
    document.getElementById('page-name').innerText = name
}
const pageHosts = document.getElementsByClassName('page-host');
for (let i = 0; i < pageHosts.length; i++) {
    pageHosts[i].innerText = window.location.host
}

// set page title to that of first 'h1'
document.title = document.getElementsByTagName('h1')[0].innerText