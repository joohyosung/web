// 각 li탭을 클릭하면 해당 div 보이기
// 탭 클릭 해당 div에 show 클래스명 추가
// 다른 div show 클래스명 제거
let allLi = document.querySelectorAll("li.tab-button");
let allDiv = document.querySelectorAll("div.tab-content");

allLi.forEach((li, idx) => {
  li.addEventListener("click", (e) => {
    // 모든 li orange 클래스명 제거
    allLi.forEach((item) => item.classList.remove("orange"));
    // 모든 div show 클래스명 제거
    allDiv.forEach((item) => item.classList.remove("show"));

    // 현재 이벤트 대상 orange클래스명과 div show 추가
    e.target.classList.add("orange");
    allDiv[idx].classList.add("show");
  });
});

// select 동작
// 셔츠 클릭 시 form-hide 제거
document.querySelector(".form-select").addEventListener("change", (e) => {
  const productDetail = document.querySelector(
    "form .form-select:nth-child(3)"
  );

  let value = e.target.value;
  let options = "";
  if (value == "셔츠") {
    options += "<option>90</option>";
    options += "<option>95</option>";
    options += "<option>100</option>";
    options += "<option>105</option>";
    options += "<option>110</option>";
  } else if (value == "바지") {
    options += "<option>26</option>";
    options += "<option>28</option>";
    options += "<option>30</option>";
    options += "<option>32</option>";
    options += "<option>34</option>";
  } else if (value == "신발") {
    options += "<option>240</option>";
    options += "<option>245</option>";
    options += "<option>250</option>";
    options += "<option>260</option>";
    options += "<option>270</option>";
  } else if (value == "모자") {
    options += "<option>S</option>";
    options += "<option>M</option>";
    options += "<option>L</option>";
    options += "<option>XL</option>";
    options += "<option>XXL</option>";
  }

  productDetail.innerHTML = "";
  // options를 productDetail 안에 삽입
  productDetail.innerHTML = options;

  // form-hide 제거
  productDetail.classList.remove("form-hide");
});
