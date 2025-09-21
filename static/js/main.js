async function getJSON(url) {
  const res = await fetch(url);
  return res.json();
}

document.addEventListener("DOMContentLoaded", () => {
  const adviceBtn = document.getElementById("getAdvice");
  const dogBtn = document.getElementById("getDog");
  const adviceBox = document.getElementById("adviceBox");
  const dogImg = document.getElementById("dogImg");

  if (adviceBtn) {
    adviceBtn.addEventListener("click", async () => {
      adviceBox.textContent = "Loading advice…";
      try {
        const data = await getJSON("/api/advice");
        adviceBox.textContent = data.advice;
      } catch {
        adviceBox.textContent = "Error fetching advice.";
      }
    });
  }

  if (dogBtn) {
    dogBtn.addEventListener("click", async () => {
      dogImg.alt = "Loading...";
      try {
        const data = await getJSON("/api/dog");
        dogImg.src = data.image;
        dogImg.alt = "Random dog";
      } catch {
        dogImg.alt = "Error fetching dog.";
      }
    });
  }
});
