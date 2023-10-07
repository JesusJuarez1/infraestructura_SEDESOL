function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

const btnToggle = document.querySelector('.toggle-btn');

btnToggle.addEventListener('click', function () {
  document.getElementById('sidebar').classList.toggle('active');
  console.log(document.getElementById('sidebar'))
});