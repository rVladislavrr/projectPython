
function showSection() {
  let selectedSection = document.getElementById("sectionSelect").value;
  let sections = document.getElementsByTagName("section");
  for (let i = 0; i < sections.length; i++) {
    sections[i].style.display = "none";
  }
  if (selectedSection === 'all'){
        for (let i = 0; i < sections.length; i++) {
           sections[i].style.display = "block";
        }
     }
  document.getElementById(selectedSection).style.display = "block";
}
