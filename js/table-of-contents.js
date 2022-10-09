// Code By Webdevtrick ( https://webdevtrick.com )
// Adapted by RVRX
let tocId = "heading-listing";

let headings_list;
let headingIds = [];
let headingIntersectionData = {};


function getProperListSection(heading, previousHeading, currentListElement) {
  let listSection = currentListElement;
  if (previousHeading) {
    if (heading.tagName.slice(-1) > previousHeading.tagName.slice(-1)) {
      let nextSection = document.createElement("ul");
      listSection.appendChild(nextSection);
      return nextSection;
    } else if (heading.tagName.slice(-1) < previousHeading.tagName.slice(-1)) {
      let indentationDiff =
        parseInt(previousHeading.tagName.slice(-1)) -
        parseInt(heading.tagName.slice(-1));
      while (indentationDiff > 0) {
        listSection = listSection.parentElement;
        indentationDiff--;
      }
    }
  }
  return listSection;
}

function setIdFromContent(element, appendedId) {
  if (!element.id) {
    element.id = `${element.innerHTML
      .replace(/:/g, "")
      .trim()
      .toLowerCase()
      .split(" ")
      .join("-")}-${appendedId}`;
  }
}

function addNavigationLinkForHeading(heading, currentSectionList) {
  let listItem = document.createElement("li");
  let anchor = document.createElement("a");
  // anchor.innerHTML = heading.innerHTML;
  anchor.classList.add('lonesome-link');
  anchor.id = `${heading.id}-link`;
  anchor.href = `#${heading.id}`;
  listItem.appendChild(anchor);
  currentSectionList.appendChild(listItem);
}

function buildTableOfContentsFromHeadings() {
  const tocElement = document.querySelector(`#${tocId}`);
  const main = document.querySelector("main");
  if (!main) {
    throw Error("A `main` tag section is required to query headings from.");
  }
  headings_list = main.querySelectorAll("h1, h2, h3, h4, h5, h6");
  let previousHeading;
  let currentSectionList = document.createElement("ul");
  tocElement.appendChild(currentSectionList);

  headings_list.forEach((heading, index) => {
    currentSectionList = getProperListSection(
      heading,
      previousHeading,
      currentSectionList
    );
    setIdFromContent(heading, index);
    addNavigationLinkForHeading(heading, currentSectionList);

    headingIds.push(heading.id);
    headingIntersectionData[heading.id] = {
      y: 0
    };
    previousHeading = heading;
  });
}

window.addEventListener("load", (event) => {
  buildTableOfContentsFromHeadings();
  const foo = document.getElementById('heading-listing-paragraph');
  foo.innerText = "Contents:"
  foo.removeAttribute('id');
});