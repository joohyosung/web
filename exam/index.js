// 압축메뉴 버튼을 클릭하면 서브메뉴 보여주기
const toggler = document.querySelector(".navbar-toggler");
const subMenu = document.querySelector(".list-group");
const modal = document.querySelector(".black-bg");
toggler.addEventListener("click", () => {
  // 클래스 부착 show
  // toggle() : 있으면 remove, 없으면 add
  subMenu.classList.toggle("show");
});

// 로그인을 클릭하면 모달 보여주기
function modalShow() {
  modal.classList.add("show-modal");
  // 서브 메뉴가 열려 있다면 서브 메뉴 안 보이게 하기
  subMenu.classList.remove("show");
}
document.querySelector("ul.navbar-nav a").addEventListener("click", modalShow);
document.querySelector("div.list-group a").addEventListener("click", modalShow);

// 로그인 창에서 x 버튼, 검정배경 클릭 시 모달 숨겨주기
const span = document.querySelector(".close");
modal.addEventListener("click", (e) => {
  // 이벤트 버블링 현상 해결(이벤트가 어디서 왔는지 확인)
  if (e.target == modal || e.target == span) {
    modal.classList.remove("show-modal");
  }
});

// 로그인 버튼 클릭 시 입력값이 아무것도 없으면 alert 창 띄우기
const form = document.querySelector("form");
const userid = document.querySelector("#userid");
const password = document.querySelector("#password");

form.addEventListener("submit", function (e) {
  e.preventDefault();
  if (userid.value == "") {
    alert("아이디를 입력하세요.");
    userid.focus();
    return;
  } else if (password.value.length < 6 || !/[A-Z]/.test(password.value)) {
    // 비밀번호의 길이가 6보다 작거나 대문자가 하나도 없다면 경고창 띄우기
    alert("비밀번호를 확인하세요.");
    password.focus();
    return;
  }

  form.submit();
});

// 이미지 carousel
// transform: translateX(0);
// next 한 번 클릭 transform: translateX(-100vw)
// next 두 번 클릭 transform: translateX(-200vw)
// prev 한 번 클릭 transform: translateX(-100vw)
// prev 두 번 클릭 transform: translateX(0vw)

// carousel.style.transform = "translateX(-100vw)"

let index = 0;
const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
const carousel = document.querySelector(".carousel");

// next 버튼 누를 때마다 index(+1)
next.addEventListener("click", () => {
  if (index == 2) return;
  index += 1;

  carousel.style.transform = `translateX(-${index * 100}vw)`;
});
// prev 버튼 누를 때마다 index(-1)
prev.addEventListener("click", () => {
  if (index == 0) return;
  index -= 1;

  carousel.style.transform = `translateX(-${index * 100}vw)`;
});
