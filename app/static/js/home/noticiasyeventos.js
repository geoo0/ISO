function openModalWithPDF(pdfUrl) {
  var modal = document.getElementById("myModal");
  var pdfViewer = document.getElementById("pdfViewer");
   pdfViewer.src = pdfUrl;
  modal.style.display = "block";
}
  
function closeModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}

function openModalWithPDF(pdfUrl) {
  var modal = document.getElementById("myModal");
  var pdfViewer = document.getElementById("pdfViewer");
  pdfViewer.src = pdfUrl;
  modal.style.display = "block";
}

function closeModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}
