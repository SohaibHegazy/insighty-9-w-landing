document.addEventListener("DOMContentLoaded", function() {
  const graphButton = document.getElementById("graph-btn");
  const convertButton = document.getElementById("convert-btn");

  if (graphButton) {
      graphButton.addEventListener("click", function() {
          window.location.href = "/graph/";
      });
  }

  if (convertButton) {
      convertButton.addEventListener("click", function() {
          window.location.href = "/convert/";
      });
  }
});
