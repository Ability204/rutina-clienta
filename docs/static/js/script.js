function preload(src) {
  return new Promise((resolve) => {
    const loader = new Image();
    loader.onload = () => resolve(true);
    loader.onerror = () => resolve(false);
    loader.src = src;
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const gifs = document.querySelectorAll(".ejercicio-gif");

  gifs.forEach(async (img) => {
    const img1 = img.dataset.img1;
    const img2 = img.dataset.img2;

    await Promise.all([preload(img1), preload(img2)]);

    let showingFirst = true;
    setInterval(() => {
      showingFirst = !showingFirst;
      img.src = showingFirst ? img1 : img2;
    }, 1200);
  });
});
