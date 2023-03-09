function startup() {
  let foundNumber = 0;
  const timer = document.querySelector(".time");
  const topChess = document.querySelector(".top-chess");
  const botChess = document.querySelector(".bot-chess");
  const lock = document.querySelector(".lock");
  function openChess() {
    topChess.classList.add("animated");
    botChess.classList.add("animated");
    clearInterval(intervalTimer);
  }
  function validateNumber() {
    lock.children[foundNumber].classList.add("activated");
    foundNumber++;
    if (foundNumber === 4) {
      openChess();
    }
  }
  let Mesuredtime = 0;
  function myTimer() {
    Mesuredtime += 1;
    timer.innerText = `${Math.floor(Mesuredtime / 10)}:${Mesuredtime % 10}`;
  }
  let intervalTimer = setInterval(myTimer, 100);
  lock.addEventListener("click", (e) => {
    e.preventDefault;
    validateNumber();
  });
}
