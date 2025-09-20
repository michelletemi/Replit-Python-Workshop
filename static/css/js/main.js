document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("getAdvice");
  const box = document.getElementById("adviceBox");

  if (btn) {
    btn.addEventListener("click", async () => {
      box.textContent = "Loading...";
      try {
        const res = await fetch("/api/advice");
        const data = await res.json();
        box.textContent = data.advice;
      } catch {
        box.textContent = "Error fetching advice.";
      }
    });
  }
});
