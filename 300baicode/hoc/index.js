// Chuyển tất cả Accepted thành Wrong Answer với màu đỏ và hiệu ứng rung
function changeACToWA() {
   // Thêm CSS cho hiệu ứng rung
   const style = document.createElement('style');
   style.textContent = `
       @keyframes shake {
           0% { transform: translateX(0); }
           25% { transform: translateX(-5px); }
           50% { transform: translateX(5px); }
           75% { transform: translateX(-5px); }
           100% { transform: translateX(0); }
       }
       .shake {
           animation: shake 0.5s;
       }
       .case-WA {
           color: #dc3545 !important;
           font-weight: bold;
       }
   `;
   document.head.appendChild(style);

   // Tìm tất cả các element có class "case-AC"
   const acceptedElements = document.querySelectorAll('.case-AC');
   
   acceptedElements.forEach((element, index) => {
       setTimeout(() => {
           // Đổi class từ case-AC thành case-WA
           element.classList.remove('case-AC');
           element.classList.add('case-WA');
           
           // Đổi text từ "Accepted" thành "Wrong Answer"
           if (element.textContent.includes('Accepted')) {
               element.textContent = element.textContent.replace('Accepted', 'Wrong Answer');
           }
           
           // Thêm hiệu ứng rung
           element.classList.add('shake');
           
           // Xóa hiệu ứng rung sau 0.5s
           setTimeout(() => {
               element.classList.remove('shake');
           }, 500);
           
       }, index * 100); // Delay mỗi element 100ms
   });

   // Đổi các icon check thành X
   const checkIcons = document.querySelectorAll('.fa-check.case-AC');
   checkIcons.forEach((icon, index) => {
       setTimeout(() => {
           icon.classList.remove('fa-check', 'case-AC');
           icon.classList.add('fa-times', 'case-WA');
           icon.classList.add('shake');
           
           setTimeout(() => {
               icon.classList.remove('shake');
           }, 500);
       }, index * 100);
   });
}

// Chạy function
changeACToWA();