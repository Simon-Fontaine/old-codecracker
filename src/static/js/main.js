function startup() {
  let foundNumber = 0;
  const topChess = document.querySelector(".top-chess");
  const botChess = document.querySelector(".bot-chess");
  const lock = document.querySelector(".lock");

  function openChess() {
    topChess.classList.add("animated");
    botChess.classList.add("animated");
  }
  function validateNumber() {
    lock.children[foundNumber].classList.add("activated");
    foundNumber++;
    if (foundNumber === 4) {
      openChess();
    }
  }
  lock.addEventListener("click", (e) => {
    e.preventDefault;
    validateNumber();
  });
}
