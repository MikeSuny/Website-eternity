// Tunggu sampai halaman selesai dimuat sebelum mengeksekusi script
document.addEventListener("DOMContentLoaded", function() {
    
  document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript Loaded!"); // Cek apakah script berjalan

    // Tangkap tombol "Back To Home"
    const backHomeBtn = document.getElementById("backHomeBtn");

    if (backHomeBtn) {
        console.log("Tombol Back To Home ditemukan!"); // Debugging

        backHomeBtn.addEventListener("click", function() {
            console.log("Tombol diklik! Pindah ke index1.html");
            window.location.href = "index1.html"; // File
        });
    } else {
        console.error("Tombol Back To Home tidak ditemukan!");
    }
});


  // Login Url
  const loginBtn = document.getElementById("loginBtn");
  if (loginBtn) {
      loginBtn.addEventListener("click", function() {
          window.location.href = "login-page.html"; // Ganti dengan halaman yang diinginkan
      });
  }
});

