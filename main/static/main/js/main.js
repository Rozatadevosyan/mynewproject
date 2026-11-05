
function navigate(url) {
    window.location.href = url;
}

document.getElementById("home").addEventListener("click", () => navigate("http://127.0.0.1:8000/"));
document.getElementById("about").addEventListener("click", () => navigate("http://127.0.0.1:8000/about"));
document.getElementById("gallery").addEventListener("click", () => navigate("http://127.0.0.1:8000/gallery"));
document.getElementById("contact").addEventListener("click", () => navigate("http://127.0.0.1:8000/contact"));


document.getElementById("conect").addEventListener("click", () => {
    console.log("Second Contact button clicked");
    navigate("http://127.0.0.1:8000/contact");
});
