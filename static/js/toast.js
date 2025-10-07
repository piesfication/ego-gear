// function showToast(title, message, type = 'normal', duration = 3000) {
//     const toastComponent = document.getElementById('toast-component');
//     const toastTitle = document.getElementById('toast-title');
//     const toastMessage = document.getElementById('toast-message');
    
//     if (!toastComponent) return;

//     // Remove all type classes first
//     toastComponent.classList.remove(
//         'bg-red-50', 'border-red-500', 'text-red-600',
//         'bg-green-50', 'border-green-500', 'text-green-600',
//         'bg-white', 'border-gray-300', 'text-gray-800'
//     );

//     // Set type styles and icon
//     if (type === 'success') {
//         toastComponent.classList.add('bg-green-50', 'border-green-500', 'text-green-600');
//         toastComponent.style.border = '1px solid #22c55e';
//     } else if (type === 'error') {
//         toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
//         toastComponent.style.border = '1px solid #ef4444';
//     } else {
//         toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-800');
//         toastComponent.style.border = '1px solid #d1d5db';
//     }

//     toastTitle.textContent = title;
//     toastMessage.textContent = message;

//     toastComponent.classList.remove('opacity-0', 'translate-y-64');
//     toastComponent.classList.add('opacity-100', 'translate-y-0');

//     setTimeout(() => {
//         toastComponent.classList.remove('opacity-100', 'translate-y-0');
//         toastComponent.classList.add('opacity-0', 'translate-y-64');
//     }, duration);
// }

function showToast(title, message, type = 'info', duration = 3000) {
  const toast = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');
  const indicator = document.getElementById('toast-indicator');

  console.log("showToast called:", title, message, type);


  if (!toast || !indicator) return; // <--- kalau null, hentikan

  if (!toast) return;

  toastTitle.textContent = title;
  toastMessage.textContent = message;

  // Reset animasi indikator
  indicator.style.transition = 'none';
  indicator.style.width = '100%';

  // Set warna indikator berdasarkan tipe
    if (type === 'success') {
    indicator.style.backgroundColor = '#22c55e'; // hijau Tailwind green-500
    console.log("Toast type: success, warna hijau");
    } else if (type === 'error') {
    indicator.style.backgroundColor = '#ef4444'; // merah Tailwind red-500
    console.log("Toast type: error, warna merah");
    } else {
    indicator.style.backgroundColor = '#3b82f6'; // biru Tailwind blue-500
    console.log("Toast type: default, warna biru");
    }
    
  console.log("Type:", type);
  console.log("Indicator element:", indicator);
  console.log("Color applied:", indicator.style.backgroundColor);


  // Munculkan toast
  toast.classList.remove('opacity-0', 'translate-y-10');
  toast.classList.add('opacity-100', 'translate-y-0');

  // Jalankan animasi bar
  setTimeout(() => {
    indicator.style.transition = `width ${duration}ms linear`;
    indicator.style.width = '0%';
  }, 100);

  // Hilangkan toast setelah durasi
  setTimeout(() => {
    toast.classList.remove('opacity-100', 'translate-y-0');
    toast.classList.add('opacity-0', 'translate-y-10');
  }, duration + 500);
}

// tombol close manual
document.getElementById("toast-close")?.addEventListener("click", () => {
  const toast = document.getElementById("toast-component");
  toast.classList.remove("opacity-100", "translate-y-0");
  toast.classList.add("opacity-0", "translate-y-10");
});
