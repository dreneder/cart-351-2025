// effect adapted from: https://www.w3schools.com/howto/howto_js_typewriter.asp
const clasTxt = 'CART 351';
const usernameTxt = 'André Neder';
const passwordTxt = '*******';
const descriptionTxt = 'This is my website for CART-351. Hope you have fun with what you find!';

// typewriter helper used for any *_fill target
function typeWriter(txt, field, speed = 50) {
  return new Promise((resolve) => {
    let i = 0;
    function step() {
      if (i < txt.length) {
        field.textContent += txt.charAt(i);
        i++;
        setTimeout(step, speed);
      } else {
        resolve();
      }
    }
    step();
  });
}

window.onload = async function () {
  const clas = document.getElementById("class");
  const classFill = document.getElementById("class_fill");
  const username = document.getElementById("username");
  const usernameFill = document.getElementById("username_fill");
  const password = document.getElementById("password");
  const passwordFill = document.getElementById("password_fill");
  const access = document.getElementById("access");
  const description = document.getElementById("description");
  const descriptionFill = document.getElementById("description_fill");
  const navWrapper = document.querySelector(".nav-wrapper");
  const systemLoad = document.getElementById("system_load");

  // keep these hidden until you need them
  if (clas) clas.style.display = "none";
  if (username) username.style.display = "none";
  if (password) password.style.display = "none";
  if (description) description.style.display = "none";
  if (access) access.style.display = "none";
  if (navWrapper) navWrapper.style.display = "none";

  // sequence of elements to reveal/type in order
  const sequence = [
    { element: clas, fill: classFill, text: clasTxt },
    { element: username, fill: usernameFill, text: usernameTxt },
    { element: password, fill: passwordFill, text: passwordTxt },
    { element: access }, // no fill/text, just show
    { element: description, fill: descriptionFill, text: descriptionTxt },
  ];

  async function runSequence() {
    for (const item of sequence) {
      if (!item.element) continue;
      item.element.style.display = "";
      if (item.fill && item.text !== undefined) {
        item.fill.textContent = "";
        await typeWriter(item.text, item.fill);
      }
      // slight pause between elements
      await new Promise((res) => setTimeout(res, 250));
    }
    if (navWrapper) navWrapper.style.display = "flex";
  }

  // hide the loading overlay after 3 seconds, then start typing
  if (systemLoad) {
    setTimeout(() => {
      systemLoad.style.display = "none";
      runSequence();
    }, 2500);
  } else {
    runSequence();
  }
};
