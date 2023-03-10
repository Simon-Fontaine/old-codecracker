function bootup() {
  let score = [];
  if (localStorage.getItem("score")) {
    score = localStorage.getItem("score");
    score = JSON.parse(score);
  }
  let foundNumber = 0;
  let intervalId;
  let tempsAnimation = 2000;
  let flagAnimation = false;
  const timer = document.querySelector(".time");
  const topChest = document.querySelector(".top-chest");
  const botChest = document.querySelector(".bot-chest");
  const lock = document.querySelector(".lock");
  const button = document.querySelector(".open");
  const record = document.querySelector(".record");
  const placement = document.querySelector(".placement");
  const restartButton = document.querySelector(".restart");
  const resetButton = document.querySelector(".reset");
  const texteReset = document.querySelector(".texte-reset");
  const tableData = document.querySelector(".table-data");
  function openChest() {
    topChest.classList.remove("restart");
    botChest.classList.remove("restart");
    topChest.classList.add("opening");
    botChest.classList.add("opening");
    timer.innerText = `${Math.floor(mesuredtime / 100)}:${mesuredtime % 100}`;
    restartButton.removeAttribute("disabled");
    resetButton.removeAttribute("disabled");
    score.push(mesuredtime);
    localStorage.setItem("score", JSON.stringify(score));
    clearInterval(intervalId);
    let meilleurScore = score.sort(function (a, b) {
      return a > b;
    })[0];
    let placementActuel =
      score
        .sort(function (a, b) {
          return a > b;
        })
        .findIndex((e) => e === mesuredtime) + 1;
    placement.innerText = placementActuel;
    record.innerText = `${Math.floor(meilleurScore / 100)}:${
      meilleurScore % 100
    } s`;
    buildTable(
      score.sort(function (a, b) {
        return a > b;
      })
    );
  }
  function buildTable(data) {
    tableData.innerHTML = "";
    for (let index = 0; index < 10; index++) {
      tableData.innerHTML += `${
        data[index]
          ? `<tr><td>${index + 1}</td><td>${Math.floor(data[index] / 100)}:${
              data[index] % 100
            } s</td></tr`
          : ""
      }`;
    }
  }
  function validateNumber() {
    if (foundNumber < 4) {
      lock.children[foundNumber].classList.add("activated");
      foundNumber++;
      if (foundNumber === 4) {
        openChest();
      }
    }
  }
  let mesuredtime = 0;
  function myTimer() {
    mesuredtime += 1;
  }
  function start() {
    intervalId = setInterval(myTimer, 10);
    for (const child of lock.children) {
      child.classList.remove("activated");
    }
  }
  function restart() {
    foundNumber = 0;
    mesuredtime = 0;
    restartButton.setAttribute("disabled", "");
    resetButton.setAttribute("disabled", "");
    topChest.classList.remove("opening");
    botChest.classList.remove("opening");
    topChest.classList.add("restart");
    botChest.classList.add("restart");
    flagAnimation = true;
    setTimeout(() => {
      intervalId = setInterval(myTimer, 10);
      flagAnimation = false;
    }, tempsAnimation);
    for (const child of lock.children) {
      child.classList.remove("activated");
    }
  }
  function reset() {
    score = [];
    localStorage.clear("score");
    texteReset.classList.remove("hidden");
    tableData.innerHTML = "";
    setTimeout(() => {
      texteReset.classList.add("hidden");
    }, 3000);
  }
  lock.addEventListener("click", (e) => {
    e.preventDefault();
    if (flagAnimation === false) {
      validateNumber();
    }
  });
  restartButton.addEventListener("click", (e) => {
    console.log("restart");
    e.preventDefault();
    restart();
  });
  resetButton.addEventListener("click", (e) => {
    e.preventDefault();
    reset();
  });
  start();
}
